# Master Supply Chain — Inbound Inventory Placement

A focused toolkit for solving **inbound inventory placement** problems using AI-guided skills and validated computational solvers.

## Problem Domain

Three core decisions for inventory inbound placement:

| Decision | Question | Solver |
|----------|----------|--------|
| **Where to send** | Which FC/DC should receive the inventory? | PuLP (MIP) |
| **How much to place** | What quantity at each node in the network? | stockpyl + PuLP |
| **When to replenish** | What timing/frequency for inbound flows? | stockpyl |

## Directory Structure

```
inventory-agent/
├── skills/                      # 16 domain skills (SKILL.md files)
│   ├── facility-location-problem/
│   ├── distribution-center-network/
│   ├── network-design/
│   ├── hub-location-problem/
│   ├── multi-echelon-inventory/
│   ├── inventory-optimization/
│   ├── retail-allocation/
│   ├── demand-supply-matching/
│   ├── newsvendor-problem/
│   ├── economic-order-quantity/
│   ├── dynamic-lot-sizing/
│   ├── lot-sizing-problems/
│   ├── replenishment-strategy/
│   ├── retail-replenishment/
│   ├── inventory-routing-problem/
│   └── demand-forecasting/
├── example_retailer_x/          # Complete case study
│   ├── Retailer_X.md            # 23-page analytical report
│   └── solve.py                 # Working implementation
├── requirements.txt             # Python dependencies
├── LICENSE                      # MIT License
├── SKILLS_README.md             # Skills documentation
└── README.md                    # This file
```

## Skills

Each skill file contains:
- **Preferred Solver section** — verified API calls with correct signatures
- **Assessment questions** — to understand the problem context
- **Frameworks** — decision logic and methodology
- **Code examples** — for scenarios beyond what the solvers cover

### Where to Send (Network/Location)

| Skill | Solves |
|-------|--------|
| `facility-location-problem` | Which facilities to open (UFLP, CFLP, p-median) |
| `distribution-center-network` | Multi-echelon DC design (plants → DCs → customers) |
| `network-design` | End-to-end network structure and flow strategy |
| `hub-location-problem` | Hub-and-spoke consolidation networks |

### How Much to Place (Allocation/Stocking)

| Skill | Solves |
|-------|--------|
| `multi-echelon-inventory` | Safety stock positioning across network tiers |
| `inventory-optimization` | (r,Q) and (s,S) policies, reorder points |
| `retail-allocation` | Push inventory to stores/FCs based on forecast |
| `demand-supply-matching` | Allocate constrained supply to demand locations |
| `newsvendor-problem` | Single-period stocking under demand uncertainty |
| `economic-order-quantity` | Optimal order quantities (EOQ, EPQ, discounts) |

### When to Replenish (Timing)

| Skill | Solves |
|-------|--------|
| `replenishment-strategy` | Policy selection and parameter optimization |
| `retail-replenishment` | Store-level min/max and DC-to-store flows |
| `dynamic-lot-sizing` | Multi-period order schedules (Wagner-Whitin) |
| `lot-sizing-problems` | Heuristic and optimal lot-sizing methods |
| `inventory-routing-problem` | Joint delivery routing + inventory decisions |

### Supporting

| Skill | Solves |
|-------|--------|
| `demand-forecasting` | Demand estimation (feeds all three decisions) |

## Solvers

### stockpyl (Inventory Math)

Validated algorithms for inventory theory:

```python
from stockpyl.eoq import economic_order_quantity
from stockpyl.wagner_whitin import wagner_whitin
from stockpyl.newsvendor import newsvendor_normal
from stockpyl.rq import r_q_loss_function_approximation
from stockpyl.ss import s_s_power_approximation
from stockpyl.ssm_serial import optimize_base_stock_levels
from stockpyl.gsm_tree import optimize_committed_service_times
from stockpyl.meio_general import meio_by_coordinate_descent
from stockpyl.sim import simulation
```

### PuLP (Optimization)

Mixed-Integer Programming for network and allocation decisions:

```python
import pulp
prob = pulp.LpProblem("FacilityLocation", pulp.LpMinimize)
# Binary variables for facility open/close
# Continuous variables for flow allocation
# Solve with included CBC solver
prob.solve(pulp.PULP_CBC_CMD(msg=0))
```

### scikit-learn (Clustering)

Store/location clustering for allocation tiers:

```python
from sklearn.cluster import KMeans
```

## Usage

A Claude agent working in this directory will:
1. Match the user's problem to the relevant skill(s)
2. Use the skill's assessment questions to understand context
3. Apply the preferred solver to compute the answer
4. Fall back to the skill's custom code for edge cases

## Installation

```bash
# Clone the repository
git clone https://github.com/JainShekhar/inventory-agent.git
cd inventory-agent

# Install Python dependencies
pip install -r requirements.txt
```

### Requirements

- Python 3.7+
- stockpyl - Inventory optimization algorithms
- PuLP - Linear/Mixed-Integer Programming
- NumPy/SciPy - Numerical computing
- scikit-learn - Machine learning (optional, for clustering)
- pandas - Data manipulation (optional)
