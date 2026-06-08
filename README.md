# Inventory Placement Agent

An AI-powered toolkit for solving **inbound inventory placement** problems using Claude SDK, specialized skills, and validated computational solvers.

## 🚀 NEW: AI Agent

Ask questions in natural language and get optimized solutions! The agent:
- Understands your inventory placement questions
- Finds relevant optimization skills
- Writes and executes Python code (PuLP/stockpyl)
- Explains results in business terms

**Quick Start:**
```bash
export ANTHROPIC_API_KEY='your-key'
pip install -r requirements.txt
python agent.py
```

See [AGENT_README.md](AGENT_README.md) for full documentation.

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
├── agent.py                     # 🤖 AI Agent - Ask questions in natural language
├── tools.py                     # Agent tools (skill reading, code execution)
├── example_questions.py         # Pre-built example questions to test agent
├── skills/                      # 16 domain skills (SKILL.md files)
│   ├── facility-location-problem/
│   ├── inventory-optimization/
│   ├── economic-order-quantity/
│   ├── newsvendor-problem/
│   └── ... (12 more)
├── example_retailer_x/          # Manual case study
│   ├── Retailer_X.md            # 23-page analytical report
│   └── solve.py                 # Direct Python implementation
├── requirements.txt             # Python dependencies
├── LICENSE                      # MIT License
├── AGENT_README.md              # 🤖 Agent documentation
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

## Acknowledgments

The 16 supply chain skills in this repository are derived from the [awesome-supply-chain](https://github.com/kishorkukreja/awesome-supply-chain) project by Kishor Kukreja, which provides a comprehensive collection of 132+ supply chain optimization skills. This repository focuses specifically on inventory placement problems.

We also acknowledge:
- **stockpyl** library by [Larry Snyder](https://github.com/LarrySnyder/stockpyl) for inventory optimization algorithms
- The operations research and supply chain community for validated methodologies

## License

MIT License - Copyright (c) 2026 JainShekhar

See [LICENSE](LICENSE) file for full details. This project incorporates work from awesome-supply-chain (MIT License) and uses stockpyl (MIT License).
