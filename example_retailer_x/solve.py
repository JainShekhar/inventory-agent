"""
Retailer X — Inventory Placement Optimization
Solves: Where to send | How much to place | When to replenish
"""
import numpy as np
import pulp
from stockpyl.rq import r_q_loss_function_approximation
from stockpyl.wagner_whitin import wagner_whitin

# ═══════════════════════════════════════════════════════════════════════════════
# DATA
# ═══════════════════════════════════════════════════════════════════════════════

STORES = ['Store-NE', 'Store-SE', 'Store-MW', 'Store-SW']
DCS = ['DC-East', 'DC-West']
SKUS = ['A1', 'A2']

SKU_PARAMS = {
    'A1': {'unit_cost': 150, 'holding_rate': 0.30, 'stockout_cost': 75},
    'A2': {'unit_cost': 25,  'holding_rate': 0.20, 'stockout_cost': 12},
}

WEEKLY_DEMAND = {
    ('A1', 'Store-NE'): {'mean': 180, 'std': 45},
    ('A1', 'Store-SE'): {'mean': 120, 'std': 35},
    ('A1', 'Store-MW'): {'mean': 150, 'std': 40},
    ('A1', 'Store-SW'): {'mean': 90,  'std': 25},
    ('A2', 'Store-NE'): {'mean': 800, 'std': 160},
    ('A2', 'Store-SE'): {'mean': 600, 'std': 130},
    ('A2', 'Store-MW'): {'mean': 700, 'std': 150},
    ('A2', 'Store-SW'): {'mean': 450, 'std': 100},
}

TRANSPORT_COST = {
    ('DC-East', 'Store-NE'): {'A1': 3.50, 'A2': 1.20},
    ('DC-East', 'Store-SE'): {'A1': 2.80, 'A2': 0.95},
    ('DC-East', 'Store-MW'): {'A1': 4.50, 'A2': 1.50},
    ('DC-East', 'Store-SW'): {'A1': 6.20, 'A2': 2.10},
    ('DC-West', 'Store-NE'): {'A1': 5.80, 'A2': 1.95},
    ('DC-West', 'Store-SE'): {'A1': 4.90, 'A2': 1.65},
    ('DC-West', 'Store-MW'): {'A1': 3.20, 'A2': 1.10},
    ('DC-West', 'Store-SW'): {'A1': 2.50, 'A2': 0.85},
}

DC_CAPACITY = {'DC-East': 1400, 'DC-West': 2200}

LEAD_TIMES_DAYS = {
    ('DC-East', 'Store-NE'): 3, ('DC-East', 'Store-SE'): 2,
    ('DC-West', 'Store-MW'): 3, ('DC-West', 'Store-SW'): 2,
}

VENDOR_LEAD_TIMES_DAYS = {'DC-East': 14, 'DC-West': 12}
VENDOR_ORDER_COST = 500
STORE_ORDER_COST = 150

SEASONAL_DEMAND_12WK = {
    ('A1', 'DC-East'): [280, 290, 310, 320, 350, 380, 420, 450, 400, 350, 300, 280],
    ('A1', 'DC-West'): [220, 230, 250, 260, 280, 300, 330, 360, 320, 280, 240, 220],
    ('A2', 'DC-East'): [1000, 1050, 1100, 1200, 1350, 1500, 1700, 1800, 1600, 1300, 1100, 1000],
    ('A2', 'DC-West'): [1300, 1400, 1450, 1550, 1700, 1900, 2100, 2300, 2000, 1700, 1450, 1300],
}


# ═══════════════════════════════════════════════════════════════════════════════
# PROBLEM 1: WHERE TO SEND
# ═══════════════════════════════════════════════════════════════════════════════

def solve_where_to_send():
    """Solve DC-to-Store assignment via transportation LP."""
    prob = pulp.LpProblem("DC_Assignment", pulp.LpMinimize)

    x = {(sku, dc, store): pulp.LpVariable(f"x_{sku}_{dc}_{store}", lowBound=0)
         for sku in SKUS for dc in DCS for store in STORES}

    prob += pulp.lpSum(
        TRANSPORT_COST[dc, store][sku] * x[sku, dc, store]
        for sku in SKUS for dc in DCS for store in STORES
    )

    for sku in SKUS:
        for store in STORES:
            prob += pulp.lpSum(x[sku, dc, store] for dc in DCS) == WEEKLY_DEMAND[sku, store]['mean']

    for dc in DCS:
        prob += pulp.lpSum(
            x[sku, dc, store] for sku in SKUS for store in STORES
        ) <= DC_CAPACITY[dc]

    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    flows = {}
    for sku in SKUS:
        for dc in DCS:
            for store in STORES:
                val = x[sku, dc, store].value()
                if val > 0.5:
                    flows[sku, dc, store] = val

    return flows, pulp.value(prob.objective)


# ═══════════════════════════════════════════════════════════════════════════════
# PROBLEM 2: HOW MUCH TO PLACE
# ═══════════════════════════════════════════════════════════════════════════════

def solve_how_much(flows):
    """Compute (r,Q) inventory policy at each store and DC."""
    store_results = {}

    # Determine which DC serves each store (primary assignment from Problem 1)
    store_dc_map = {}
    for (sku, dc, store), val in flows.items():
        if sku == 'A1':  # use A1 to determine primary DC
            store_dc_map[store] = dc

    for sku in SKUS:
        h = SKU_PARAMS[sku]['unit_cost'] * SKU_PARAMS[sku]['holding_rate'] / 52
        p = SKU_PARAMS[sku]['stockout_cost']

        for store in STORES:
            dc = store_dc_map[store]
            lt_weeks = LEAD_TIMES_DAYS[dc, store] / 7
            d_mean = WEEKLY_DEMAND[sku, store]['mean']
            d_std = WEEKLY_DEMAND[sku, store]['std']

            r, Q = r_q_loss_function_approximation(
                holding_cost=h, stockout_cost=p, fixed_cost=STORE_ORDER_COST,
                demand_mean=d_mean, demand_sd=d_std, lead_time=lt_weeks
            )

            safety_stock = r - d_mean * lt_weeks
            avg_inv = Q / 2 + safety_stock
            investment = avg_inv * SKU_PARAMS[sku]['unit_cost']

            store_results[sku, store] = {
                'r': r, 'Q': Q, 'safety_stock': safety_stock,
                'avg_inv': avg_inv, 'investment': investment
            }

    # DC-level inventory
    dc_results = {}
    dc_demands = {
        ('A1', 'DC-East'): {'mean': 300, 'std': np.sqrt(45**2 + 35**2)},
        ('A1', 'DC-West'): {'mean': 240, 'std': np.sqrt(40**2 + 25**2)},
        ('A2', 'DC-East'): {'mean': 1100, 'std': np.sqrt(160**2 + 85**2)},
        ('A2', 'DC-West'): {'mean': 1450, 'std': np.sqrt(150**2 + 100**2 + 95**2)},
    }

    for sku in SKUS:
        h = SKU_PARAMS[sku]['unit_cost'] * SKU_PARAMS[sku]['holding_rate'] / 52
        p = SKU_PARAMS[sku]['stockout_cost']

        for dc in DCS:
            lt_weeks = VENDOR_LEAD_TIMES_DAYS[dc] / 7
            d = dc_demands[sku, dc]

            r, Q = r_q_loss_function_approximation(
                holding_cost=h, stockout_cost=p, fixed_cost=VENDOR_ORDER_COST,
                demand_mean=d['mean'], demand_sd=d['std'], lead_time=lt_weeks
            )

            safety_stock = r - d['mean'] * lt_weeks
            avg_inv = Q / 2 + safety_stock
            investment = avg_inv * SKU_PARAMS[sku]['unit_cost']

            dc_results[sku, dc] = {
                'r': r, 'Q': Q, 'safety_stock': safety_stock,
                'avg_inv': avg_inv, 'investment': investment
            }

    return store_results, dc_results


# ═══════════════════════════════════════════════════════════════════════════════
# PROBLEM 3: WHEN TO REPLENISH
# ═══════════════════════════════════════════════════════════════════════════════

def solve_when_to_replenish():
    """Solve vendor order schedule using Wagner-Whitin DP."""
    results = {}

    for sku in SKUS:
        h = SKU_PARAMS[sku]['unit_cost'] * SKU_PARAMS[sku]['holding_rate'] / 52
        for dc in DCS:
            dems = SEASONAL_DEMAND_12WK[sku, dc]
            Q, cost, theta, s = wagner_whitin(
                num_periods=12, holding_cost=h,
                fixed_cost=VENDOR_ORDER_COST, demand=dems
            )
            results[sku, dc] = {
                'orders': Q[1:],
                'demand': dems,
                'cost': cost,
                'n_pos': sum(1 for q in Q if q > 0)
            }

    return results


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("Solving Retailer X Inventory Placement...\n")

    # Problem 1
    flows, transport_cost = solve_where_to_send()
    print(f"[1] WHERE TO SEND — Weekly transport cost: ${transport_cost:,.2f}")
    for (sku, dc, store), val in sorted(flows.items()):
        print(f"      {sku}: {dc} → {store}: {val:.0f} units/wk")

    # Problem 2
    store_inv, dc_inv = solve_how_much(flows)
    total_store_inv = sum(r['investment'] for r in store_inv.values())
    total_dc_inv = sum(r['investment'] for r in dc_inv.values())
    print(f"\n[2] HOW MUCH TO PLACE — Store investment: ${total_store_inv:,.0f}, DC investment: ${total_dc_inv:,.0f}")
    print(f"    Total network inventory: ${total_store_inv + total_dc_inv:,.0f}")

    # Problem 3
    ww_results = solve_when_to_replenish()
    total_pos = sum(r['n_pos'] for r in ww_results.values())
    total_cost = sum(r['cost'] for r in ww_results.values())
    print(f"\n[3] WHEN TO REPLENISH — {total_pos} vendor POs over 12 weeks, cost: ${total_cost:,.0f}")
    for (sku, dc), r in sorted(ww_results.items()):
        order_weeks = [i+1 for i, q in enumerate(r['orders']) if q > 0]
        print(f"      {sku} @ {dc}: order in weeks {order_weeks} ({r['n_pos']} POs, ${r['cost']:,.0f})")

    print(f"\n{'='*60}")
    print(f"TOTAL ANNUAL COSTS:")
    print(f"  Transport:      ${transport_cost * 52:>12,.0f}")
    print(f"  Inventory hold: ${(total_store_inv + total_dc_inv) * 0.25:>12,.0f}")
    print(f"  Vendor orders:  ${total_cost * (52/12):>12,.0f}")
    print(f"  {'─'*40}")
    print(f"  Total:          ${transport_cost*52 + (total_store_inv+total_dc_inv)*0.25 + total_cost*(52/12):>12,.0f}")
