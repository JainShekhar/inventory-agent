# Skills Reference

Complete reference for all 16 inventory placement skills used by the agent.

---

## Network & Location Skills (WHERE to send)

### facility-location-problem
**Solves:** Which facilities/warehouses to open and how to assign customers

**Problems:**
- Uncapacitated Facility Location (UFLP)
- Capacitated Facility Location (CFLP)
- p-Median Problem (locate exactly p facilities)
- p-Center Problem (minimize maximum distance)

**Solver:** PuLP (Mixed-Integer Programming)

**Input Needed:**
- Potential facility locations and fixed costs
- Customer locations and demands
- Transportation costs (per unit)
- Facility capacities (if capacitated)

**Example:** "I have 3 potential warehouses with costs [$50k, $60k, $45k], 5 customers with demands [100, 150, 80, 120, 90]. Transport costs are... Which should I open?"

---

### distribution-center-network
**Solves:** Multi-echelon distribution network design (plants → DCs → customers)

**Problems:**
- Number and location of DCs
- Flow allocation across network tiers
- Consolidation vs. direct shipping trade-offs

**Solver:** PuLP + stockpyl (for inventory positioning)

**Input Needed:**
- Plant locations and capacities
- Potential DC locations and costs
- Store/customer locations and demands
- Transportation costs between tiers

---

### network-design
**Solves:** End-to-end supply chain network structure

**Problems:**
- Overall network configuration
- Echelon structure (direct, single-tier, multi-tier)
- Strategic flow decisions

**Solver:** PuLP

**Input Needed:**
- All facility types and locations
- Costs (fixed, variable, transport)
- Demands and capacities
- Strategic constraints

---

### hub-location-problem
**Solves:** Hub-and-spoke consolidation networks

**Problems:**
- Which nodes become hubs
- Hub-to-hub connections
- Spoke assignment to hubs

**Solver:** PuLP

**Input Needed:**
- Node locations
- Hub costs and capacities
- Discount factor for hub-to-hub transport
- Origin-destination demands

---

## Inventory & Stocking Skills (HOW MUCH to place)

### inventory-optimization
**Solves:** Optimal inventory policies and parameters

**Problems:**
- (r,Q) continuous review policies
- (s,S) periodic review policies
- Base stock levels
- Safety stock calculations

**Solver:** stockpyl (`rq`, `ss` modules)

**Input Needed:**
- Demand mean and standard deviation
- Lead time
- Unit cost and holding rate
- Stockout/backorder cost
- Fixed ordering cost

**Example:** "Weekly demand is Normal(mean=100, std=20), lead time 2 weeks, unit cost $30, holding rate 25%, stockout cost $50, order cost $200. What's my (r,Q) policy?"

---

### economic-order-quantity
**Solves:** Optimal order quantities (EOQ family of models)

**Problems:**
- Basic EOQ
- EPQ (Economic Production Quantity)
- Quantity discounts
- Backordering allowed

**Solver:** stockpyl (`eoq` module)

**Input Needed:**
- Annual/periodic demand
- Unit cost
- Holding cost rate or absolute holding cost
- Fixed ordering/setup cost
- Discount schedule (if applicable)

**Example:** "Annual demand 12,000 units, cost $25, holding rate 20%, order cost $100. What's the EOQ?"

---

### newsvendor-problem
**Solves:** Single-period stocking under demand uncertainty

**Problems:**
- Seasonal product stocking
- Perishable goods
- Fashion/style goods
- One-time buys

**Solver:** stockpyl (`newsvendor` module)

**Input Needed:**
- Demand distribution (mean, std, or full distribution)
- Unit cost
- Selling price
- Salvage value (if unsold)
- Shortage cost (if applicable)

**Example:** "Demand is Normal(500, 100), cost $20, price $50, salvage $5. How many to order?"

---

### multi-echelon-inventory
**Solves:** Safety stock positioning across network tiers

**Problems:**
- Where to hold safety stock in the network
- Guaranteed service time models (GSM)
- Stochastic service models (SSM)
- Multi-echelon inventory optimization (MEIO)

**Solver:** stockpyl (`gsm_tree`, `ssm_serial`, `meio_general`)

**Input Needed:**
- Network structure (tree or serial)
- Demand at each node
- Lead times between echelons
- Holding costs at each echelon
- Service level targets

---

### retail-allocation
**Solves:** Push allocation of inventory to stores

**Problems:**
- Store-level allocation from DC
- Proportional vs. fair-share allocation
- Store clustering by demand patterns
- Size curve allocation (apparel)

**Solver:** Custom algorithms + scikit-learn (clustering)

**Input Needed:**
- Store-level demand forecasts
- Available inventory
- Store capacities
- Allocation rules/constraints

---

### demand-supply-matching
**Solves:** Allocating constrained supply to demand locations

**Problems:**
- Supply shortage allocation
- Priority-based allocation
- Fair-share vs. profit-maximizing
- ATP (Available to Promise)

**Solver:** PuLP or custom allocation algorithms

**Input Needed:**
- Demand by location
- Available supply
- Allocation priorities or profit margins
- Minimum/maximum allocation rules

---

## Timing & Replenishment Skills (WHEN to replenish)

### dynamic-lot-sizing
**Solves:** Multi-period order schedule with time-varying demand

**Problems:**
- Wagner-Whitin dynamic programming
- Silver-Meal heuristic
- Lot-for-lot vs. batching trade-offs

**Solver:** stockpyl (`wagner_whitin`, `finite_horizon`)

**Input Needed:**
- Demand forecast by period (e.g., 12 weeks)
- Unit cost or holding cost per period
- Fixed ordering cost
- Planning horizon

**Example:** "6-month demand [500, 600, 550, 700, 650, 600], unit cost $20, holding $2/unit/month, order cost $500. When should I order?"

---

### lot-sizing-problems
**Solves:** Various lot-sizing heuristics and algorithms

**Problems:**
- Part-period balancing (PPB)
- Least unit cost (LUC)
- Period order quantity (POQ)
- Silver-Meal

**Solver:** stockpyl or custom implementations

**Input Needed:**
- Demand by period
- Costs (holding, ordering, unit)
- Constraints (capacity, lead time)

---

### replenishment-strategy
**Solves:** Selecting and optimizing replenishment policies

**Problems:**
- Policy comparison (r,Q) vs (s,S) vs base-stock
- Parameter optimization
- Service level vs. cost trade-offs
- VMI (Vendor Managed Inventory) policies

**Solver:** stockpyl (multiple modules)

**Input Needed:**
- Demand characteristics
- Cost structure
- Service level targets
- Replenishment constraints (lead time, min order, etc.)

---

### retail-replenishment
**Solves:** Store-level replenishment from DC

**Problems:**
- Min-max policies at stores
- DC-to-store replenishment frequency
- Store ordering rules
- DRP (Distribution Requirements Planning)

**Solver:** stockpyl + custom logic

**Input Needed:**
- Store demand patterns
- DC-to-store lead times
- Store shelf capacity
- Replenishment costs

---

### inventory-routing-problem
**Solves:** Joint inventory and routing decisions

**Problems:**
- VMI with delivery routing
- When to deliver and how much
- Route optimization with inventory costs
- Delivery frequency optimization

**Solver:** PuLP (for joint optimization) or heuristics

**Input Needed:**
- Customer locations and demand rates
- Vehicle capacities
- Routing costs
- Inventory holding costs
- Customer storage capacities

---

## Supporting Skill

### demand-forecasting
**Solves:** Demand estimation for inventory planning

**Problems:**
- Time series forecasting
- Trend and seasonality
- Demand sensing
- Forecast accuracy metrics

**Solver:** Statistical methods, statsmodels, scikit-learn

**Input Needed:**
- Historical demand data
- Seasonality patterns
- External factors (if available)
- Forecast horizon

---

## How Skills Work with the Agent

1. **Agent lists available skills** using `list_available_skills()`
2. **Identifies relevant skill(s)** based on user question
3. **Reads skill file** using `read_skill(skill_name)`
4. **Extracts methodology:**
   - Preferred solver
   - Required input data
   - Code examples
   - Assessment questions
5. **Generates code** based on skill templates
6. **Executes and interprets** results

---

## Skill File Structure

Each skill is stored as `skills/[skill-name]/SKILL.md` with:

```markdown
---
name: skill-name
description: When to use this skill and trigger keywords
---

# Skill Title

Expert role definition

## Preferred Solver
Code example with correct API usage

## Initial Assessment
Questions to understand problem context

## Frameworks & Methodologies
Industry approaches

## Algorithms & Models
Mathematical formulations

## Python Code Examples
Working implementations

## Common Challenges
Real-world issues and solutions
```

---

## Adding Your Own Skills

To add a new skill:

1. Create folder: `skills/my-new-skill/`
2. Create file: `skills/my-new-skill/SKILL.md`
3. Follow structure above
4. Include working Python code examples
5. Test with the agent

The agent will automatically discover and use new skills!

---

For more details on each skill, read the actual SKILL.md files in the `skills/` directory.
