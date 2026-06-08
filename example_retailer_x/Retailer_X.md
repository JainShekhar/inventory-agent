# Inbound Inventory Placement Study: Retailer X

**Prepared for:** Retailer X, VP Supply Chain Operations
**Prepared by:** Inventory Placement Analytics Team
**Date:** June 2026

---

## 1. Background

Retailer X is a mid-size consumer electronics retailer operating four large-format stores across the United States. The stores are located in New York (Northeast), Miami (Southeast), Chicago (Midwest), and Phoenix (Southwest), collectively generating over 3,000 units of weekly demand across the product portfolio.

The company operates a two-echelon distribution network. Inventory flows from overseas and domestic vendors into two distribution centers — one in Atlanta (DC-East) and one in Dallas (DC-West) — before being shipped outbound to stores. This hub-and-spoke model was designed to balance geographic coverage with consolidation economics.

Two product categories dominate the company's inbound planning complexity:

- **SKU A1 — Premium Electronics:** A high-value product ($150 unit cost, $299 retail) with moderate weekly demand of 540 units across all stores. This product carries significant obsolescence risk, reflected in a 30% annual holding cost rate. Demand variability is moderate (coefficient of variation ~25%).

- **SKU A2 — Consumer Accessories:** A high-volume, low-value accessory ($25 unit cost, $49.99 retail) with weekly demand of 2,550 units network-wide. Holding cost is lower at 20% annually, but the sheer volume creates capacity pressure on the distribution centers.

---

## 2. Problem Statement

The supply chain team faces an immediate operational constraint: **DC-East in Atlanta is limited to processing 1,400 units per week** due to an ongoing labor shortage that has reduced shift coverage. Under normal geographic routing — where DC-East serves the Northeast and Southeast stores, and DC-West serves the Midwest and Southwest — DC-East would need to handle 1,700 units weekly. This creates a 300-unit overflow that must be rerouted without disrupting store service levels.

Beyond this immediate constraint, the team needs answers to three fundamental questions that recur every planning cycle:

**Question 1 — Where should we send inventory?**
Given the capacity limitation at DC-East, which DC should serve which store for each SKU? Is a clean geographic split still optimal, or should some flows be rerouted? What is the cost of the capacity constraint?

**Question 2 — How much inventory should we hold at each location?**
What are the right stocking levels at each store and each DC? How do we balance the risk of stockouts (lost sales of $75 per unit on A1, $12 per unit on A2) against the cost of holding excess inventory? What is the total working capital tied up in the network?

**Question 3 — When should we place replenishment orders?**
How frequently should DCs ship to stores? When should vendor purchase orders be placed, given that demand will ramp significantly over the next 12 weeks as the holiday season approaches? Can we save money by batching orders without creating stockout risk?

---

## 3. Network Data

### 3.1 Store Demand Profiles

Weekly demand at each store follows a normal distribution. The table below summarizes the mean and standard deviation based on 52 weeks of historical sales data.

| Store | Region | SKU A1 (units/week) | SKU A2 (units/week) |
|-------|--------|---------------------|---------------------|
| Store-NE (New York) | Northeast | 180 ± 45 | 800 ± 160 |
| Store-SE (Miami) | Southeast | 120 ± 35 | 600 ± 130 |
| Store-MW (Chicago) | Midwest | 150 ± 40 | 700 ± 150 |
| Store-SW (Phoenix) | Southwest | 90 ± 25 | 450 ± 100 |
| **Network Total** | | **540** | **2,550** |

Store-NE carries the highest demand and the highest variability for both SKUs, reflecting the dense urban market. Store-SW has the lowest demand but also the most predictable sales patterns.

### 3.2 Distribution Center Characteristics

| DC | Location | Weekly Capacity | Fixed Cost/Month | Vendor Lead Time |
|----|----------|-----------------|------------------|------------------|
| DC-East | Atlanta, GA | 1,400 units (constrained) | $120,000 | 14 days |
| DC-West | Dallas, TX | 2,200 units | $95,000 | 12 days |

DC-East's capacity constraint is the result of a labor shortage affecting the second shift. Management expects this to persist for at least 6 months.

### 3.3 Transportation Costs

Per-unit shipping costs from each DC to each store, reflecting distance, carrier rates, and product weight (A1 weighs 2.5 lbs; A2 weighs 0.5 lbs).

| Route | A1 ($/unit) | A2 ($/unit) |
|-------|-------------|-------------|
| DC-East → Store-NE (Atlanta → New York) | $3.50 | $1.20 |
| DC-East → Store-SE (Atlanta → Miami) | $2.80 | $0.95 |
| DC-East → Store-MW (Atlanta → Chicago) | $4.50 | $1.50 |
| DC-East → Store-SW (Atlanta → Phoenix) | $6.20 | $2.10 |
| DC-West → Store-NE (Dallas → New York) | $5.80 | $1.95 |
| DC-West → Store-SE (Dallas → Miami) | $4.90 | $1.65 |
| DC-West → Store-MW (Dallas → Chicago) | $3.20 | $1.10 |
| DC-West → Store-SW (Dallas → Phoenix) | $2.50 | $0.85 |

### 3.4 Lead Times and Ordering Costs

| Leg | Transit Time | Ordering Cost |
|-----|--------------|---------------|
| Vendor → DC-East | 14 days | $500 per purchase order |
| Vendor → DC-West | 12 days | $500 per purchase order |
| DC-East → Store-NE | 3 days | $150 per shipment |
| DC-East → Store-SE | 2 days | $150 per shipment |
| DC-West → Store-MW | 3 days | $150 per shipment |
| DC-West → Store-SW | 2 days | $150 per shipment |

### 3.5 Cost Parameters

| Parameter | SKU A1 | SKU A2 |
|-----------|--------|--------|
| Unit cost | $150 | $25 |
| Selling price | $299 | $49.99 |
| Gross margin | 50% | 50% |
| Annual holding cost rate | 30% | 20% |
| Holding cost ($/unit/week) | $0.865 | $0.096 |
| Stockout cost ($/unit) | $75 | $12 |

---

## 4. Solution: Where to Send

### 4.1 Approach

We formulate the DC-to-store assignment as a linear program (LP). The decision variables represent the weekly flow of each SKU from each DC to each store. The objective is to minimize total transportation cost subject to two constraints: all store demand must be met, and no DC can exceed its throughput capacity.

### 4.2 Results

The optimizer determines that the lowest-cost feasible assignment splits Store-SE's A2 volume between both distribution centers:

| SKU | Source DC | → Store-NE | → Store-SE | → Store-MW | → Store-SW |
|-----|-----------|------------|------------|------------|------------|
| A1 | DC-East | 180 | 120 | — | — |
| A1 | DC-West | — | — | 150 | 90 |
| A2 | DC-East | 800 | 300 | — | — |
| A2 | DC-West | — | 300 | 700 | 450 |

**DC utilization after optimization:**

- DC-East: 1,400 / 1,400 units = **100%** (fully saturated)
- DC-West: 1,690 / 2,200 units = **77%** (absorbs the overflow)

### 4.3 Interpretation

The geographic assignment (DC-East serves eastern stores, DC-West serves western stores) remains optimal for all flows except one: Store-SE's A2 demand of 600 units per week must be split evenly. Half continues to ship from DC-East at $0.95/unit, while the other half is rerouted through DC-West at $1.65/unit.

This rerouting adds $0.70 per unit on 300 units, costing **$210 per week ($10,920 annually)**. This is the direct financial cost of the DC-East capacity constraint. Any investment to expand DC-East capacity that costs less than $11,000 per year would more than pay for itself.

**Weekly transport cost: $4,564**
**Annual transport cost: $237,302**

---

## 5. Solution: How Much to Place

### 5.1 Approach

For each SKU-location combination, we compute the optimal inventory policy using a continuous-review (r, Q) model. This model answers two questions simultaneously: "At what inventory level should we trigger a reorder?" (the reorder point *r*) and "How many units should we order?" (the order quantity *Q*).

The reorder point accounts for demand variability during the lead time, providing a safety stock buffer. The order quantity balances the fixed cost of placing an order against the holding cost of carrying inventory.

### 5.2 Store-Level Inventory

| SKU | Store | Weekly Demand | Reorder Point | Order Quantity | Safety Stock | Avg Inventory | Capital Tied Up |
|-----|-------|---------------|---------------|----------------|--------------|---------------|-----------------|
| A1 | Store-NE | 180 | 103 units | 264 units | 26 units | 158 units | $23,732 |
| A1 | Store-SE | 120 | 48 units | 213 units | 14 units | 121 units | $18,116 |
| A1 | Store-MW | 150 | 87 units | 241 units | 23 units | 143 units | $21,493 |
| A1 | Store-SW | 90 | 34 units | 184 units | 9 units | 100 units | $15,057 |
| A2 | Store-NE | 800 | 425 units | 1,631 units | 82 units | 898 units | $22,443 |
| A2 | Store-SE | 600 | 215 units | 1,404 units | 44 units | 746 units | $18,644 |
| A2 | Store-MW | 700 | 377 units | 1,526 units | 77 units | 840 units | $21,002 |
| A2 | Store-SW | 450 | 158 units | 1,213 units | 30 units | 636 units | $15,909 |

**Total capital in store inventory: $156,395**

**How to read this table:** Take Store-NE for SKU A1. The store sells 180 units per week with a 3-day replenishment lead time from DC-East. When on-hand inventory drops to 103 units, a replenishment order of 264 units is triggered. Of those 103 units at reorder, about 77 will be consumed during the 3-day transit, leaving 26 units as safety stock to buffer against demand spikes. On average, the store holds 158 units — worth $23,732 in tied-up capital.

### 5.3 DC-Level Inventory

The DCs face longer lead times from vendors (12-14 days) and aggregate demand from multiple stores, requiring larger buffers.

| SKU | DC | Weekly Throughput | Vendor Lead Time | Reorder Point | Order Quantity | Safety Stock | Avg Inventory | Capital Tied Up |
|-----|-----|-------------------|------------------|---------------|----------------|--------------|---------------|-----------------|
| A1 | DC-East | 300 units | 2.0 weeks | 678 units | 627 units | 78 units | 391 units | $58,702 |
| A1 | DC-West | 240 units | 1.7 weeks | 466 units | 556 units | 55 units | 333 units | $49,947 |
| A2 | DC-East | 1,100 units | 2.0 weeks | 2,426 units | 3,508 units | 226 units | 1,980 units | $49,494 |
| A2 | DC-West | 1,450 units | 1.7 weeks | 2,697 units | 4,013 units | 212 units | 2,218 units | $55,455 |

**Total capital in DC inventory: $213,597**

### 5.4 Network Inventory Summary

| Metric | SKU A1 | SKU A2 | Total |
|--------|--------|--------|-------|
| Safety stock (all locations) | 205 units | 671 units | 876 units |
| Average inventory (all locations) | 1,246 units | 6,318 units | 7,564 units |
| Weeks of supply | 2.3 weeks | 2.5 weeks | — |
| Total working capital | $187,046 | $182,947 | **$369,992** |

Despite A1 having 6x higher unit cost, the two SKUs require nearly identical capital investment. A1's investment is driven by unit value; A2's investment is driven by volume. This is a common pattern: expensive items require fewer units of safety stock (because each unit covers more demand value), while cheap high-volume items require large buffers in absolute terms.

---

## 6. Solution: When to Replenish

### 6.1 DC-to-Store Replenishment Cadence

The (r, Q) policy from Section 5 implies the following natural replenishment rhythms:

| SKU | Store | Order Size | Time Between Shipments | Shipments per Month |
|-----|-------|------------|------------------------|---------------------|
| A1 | Store-NE | 264 units | Every 10 days | 3.0 |
| A1 | Store-SE | 213 units | Every 12 days | 2.4 |
| A1 | Store-MW | 241 units | Every 11 days | 2.7 |
| A1 | Store-SW | 184 units | Every 14 days | 2.1 |
| A2 | Store-NE | 1,631 units | Every 14 days | 2.1 |
| A2 | Store-SE | 1,404 units | Every 16 days | 1.8 |
| A2 | Store-MW | 1,526 units | Every 15 days | 2.0 |
| A2 | Store-SW | 1,213 units | Every 19 days | 1.6 |

A1 ships to stores roughly every 10-14 days in smaller quantities (200-260 units). A2 ships less frequently (every 14-19 days) but in much larger drops (1,200-1,600 units). The difference arises because A2's low holding cost per unit makes it economical to batch more aggressively.

### 6.2 Vendor-to-DC Order Schedule (12-Week Planning Horizon)

The next 12 weeks cover the holiday season ramp. Demand starts at baseline levels in weeks 1-3, accelerates through weeks 4-6, peaks in weeks 7-8, and gradually returns to normal by week 12.

We use the Wagner-Whitin dynamic programming algorithm to determine exactly when to place vendor purchase orders. The algorithm finds the optimal balance between ordering frequently (more $500 PO costs) versus batching orders (more holding cost from carrying inventory earlier).

#### SKU A1 at DC-East

```
         Wk1    Wk2    Wk3    Wk4    Wk5    Wk6    Wk7    Wk8    Wk9   Wk10   Wk11   Wk12
Demand:  280    290    310    320    350    380    420    450    400    350    300    280
Order:   570     —     630     —     730     —     870     —     750     —     580     —
```

Orders every 2 weeks, with quantities increasing as the holiday peak approaches. Week 7's order of 870 units is the largest, covering the peak period.

#### SKU A1 at DC-West

```
         Wk1    Wk2    Wk3    Wk4    Wk5    Wk6    Wk7    Wk8    Wk9   Wk10   Wk11   Wk12
Demand:  220    230    250    260    280    300    330    360    320    280    240    220
Order:   450     —     510     —     580     —     690     —     600     —     460     —
```

Same biweekly rhythm as DC-East, with proportionally smaller quantities reflecting lower West-region demand for A1.

#### SKU A2 at DC-East

```
         Wk1    Wk2    Wk3    Wk4    Wk5    Wk6    Wk7    Wk8    Wk9   Wk10   Wk11   Wk12
Demand: 1,000  1,050  1,100  1,200  1,350  1,500  1,700  1,800  1,600  1,300  1,100  1,000
Order:  3,150    —      —    4,050    —      —    5,100    —      —    3,400    —      —
```

Only 4 purchase orders over 12 weeks. Because A2's holding cost is just $0.096/unit/week, it is far cheaper to place large infrequent orders than to pay $500 per PO every week. The week 7 order of 5,100 units is the largest single PO in the plan — pre-building inventory for the holiday peak.

#### SKU A2 at DC-West

```
         Wk1    Wk2    Wk3    Wk4    Wk5    Wk6    Wk7    Wk8    Wk9   Wk10   Wk11   Wk12
Demand: 1,300  1,400  1,450  1,550  1,700  1,900  2,100  2,300  2,000  1,700  1,450  1,300
Order:  4,150    —      —    3,250    —    4,000    —    4,300    —    4,450    —      —
```

DC-West needs 5 POs (one more than DC-East) because its A2 volume is 28% higher, making the cost of holding 3 weeks of inventory exceed the savings from one fewer PO.

### 6.3 Ordering Cost Comparison

| Method | Purchase Orders | Ordering Cost | Holding Cost | Total Cost |
|--------|-----------------|---------------|--------------|------------|
| **Wagner-Whitin (optimal)** | **21 POs** | **$10,500** | **$6,089** | **$16,589** |
| Lot-for-lot (weekly orders) | 48 POs | $24,000 | $0 | $24,000 |
| Fixed biweekly | 24 POs | $12,000 | ~$4,200 | ~$16,200 |

The Wagner-Whitin solution saves **$7,411 per quarter ($29,644 annually)** versus naive weekly ordering, by reducing purchase orders from 48 to 21. The algorithm naturally differentiates between SKUs: A1 (expensive to hold) orders biweekly, while A2 (cheap to hold) orders every 3 weeks.

---

## 7. Total Cost of the Recommended Plan

| Cost Category | Weekly | Annual | % of Total |
|---------------|--------|--------|------------|
| Transportation (DC → Stores) | $4,564 | $237,302 | 37% |
| DC fixed operating costs | $4,135 | $215,000 | 34% |
| Inventory holding (stores + DCs) | $2,133 | $110,916 | 17% |
| Vendor ordering (purchase orders) | $1,383 | $71,889 | 11% |
| **Total supply chain cost** | **$12,214** | **$635,107** | **100%** |

**Inventory working capital requirement: $369,992**

---

## 8. Recommendations

### Immediate Actions

1. **Implement the split-sourcing plan for Store-SE.** Begin routing 300 units/week of A2 through DC-West immediately. This resolves the DC-East capacity violation at minimal cost ($210/week). Coordinate with the Miami store to expect shipments from two origins.

2. **Set reorder points in the WMS.** Program the (r, Q) parameters from Section 5 into the warehouse management system for automated replenishment triggers. This replaces the current ad-hoc ordering that has caused both overstocks and stockouts.

3. **Place vendor POs according to the 12-week schedule.** The holiday season plan in Section 6 requires the first large A2 orders (3,150 and 4,150 units) to ship immediately. Vendor capacity should be confirmed for the week 7 peak orders (5,100 units to DC-East).

### Medium-Term Improvements

4. **Invest in DC-East capacity expansion.** The capacity constraint costs $10,920 annually in rerouting. Any labor, automation, or shift-extension investment under this threshold pays for itself immediately. A 300-unit capacity increase eliminates the need for split-sourcing entirely.

5. **Negotiate volume discounts on A2 vendor orders.** The optimal plan places orders of 3,000-5,000 units. At these volumes, even a 2% discount ($0.50/unit) would save $8,000-10,000 annually.

6. **Increase safety stock monitoring at Store-NE.** This store has the highest demand variability (A2 coefficient of variation = 20%) and the highest stockout exposure. The 82-unit safety stock covers less than one day of peak demand. Consider a targeted service level increase from 95% to 97% for this location.

### Operational Alerts

7. **DC receiving capacity for peak weeks.** Week 7 requires DC-East to receive 5,100 units of A2 plus 870 units of A1 in a single order. Ensure inbound dock scheduling and put-away labor can handle 5,970 units in the vendor lead time window.

8. **Post-holiday inventory wind-down.** Demand drops 44% from peak (week 8) to trough (week 12). The Wagner-Whitin schedule already accounts for this by reducing order sizes in weeks 9-12, but monitor actual sales to avoid overstock as the season ends.

---

## Appendix A: Methodology

| Problem | Mathematical Model | Algorithm | Software |
|---------|-------------------|-----------|----------|
| DC-to-store assignment | Linear program (transportation problem) | Simplex method | PuLP 3.3.1 + CBC solver |
| Inventory stocking levels | (r, Q) continuous review policy | Loss function approximation | stockpyl |
| Vendor order timing | Dynamic lot sizing (Wagner-Whitin) | Backward-recursion dynamic programming | stockpyl |

All models assume stationary demand distributions (Sections 4-5) except the vendor ordering model (Section 6) which uses a 12-week deterministic demand forecast. The (r, Q) policy assumes normally distributed demand during lead time and full backordering of unmet demand.

## Appendix B: Sensitivity

Key parameters that, if changed, would materially alter the recommended plan:

- **DC-East capacity:** If restored to full capacity (2,500 units), the split-sourcing disappears and transport cost drops by $10,920/year.
- **Vendor lead time:** A 1-week reduction at DC-East (14→7 days) would reduce DC safety stock by ~40%, freeing ~$25,000 in working capital.
- **Stockout cost for A1:** If true lost-sale cost is higher than $75 (e.g., customer defection), safety stocks at all stores should increase. At $150/unit stockout cost, Store-NE safety stock rises from 26 to 41 units.
- **Fixed order cost:** If vendor PO cost could be reduced from $500 to $250 (e.g., EDI automation), Wagner-Whitin would recommend more frequent smaller orders, reducing average DC inventory by ~15%.
