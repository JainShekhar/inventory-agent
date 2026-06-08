# Inventory Placement Skills

A focused collection of 16 AI agent skills for solving inbound inventory placement problems. These skills work as a plugin for Claude Code and other AI coding assistants.

## Table of Contents

- [Overview](#overview)
- [Skills Plugin](#skills-plugin)
- [Solver Libraries](#solver-libraries)
- [Example Case Study](#example-case-study)
- [Usage](#usage)

## Overview

This directory contains 16 domain-specific skills designed to help solve the three critical questions of inventory placement:

1. **WHERE to send** - Which facilities should receive inventory?
2. **HOW MUCH to place** - What are optimal stocking levels?
3. **WHEN to replenish** - What timing and frequency for orders?

## Skills Plugin

The 16 skills provide AI assistants with expert knowledge in:

- **Network & Location** - Facility location, DC network design, hub location
- **Inventory Optimization** - Multi-echelon, safety stock, reorder points
- **Allocation** - Retail allocation, demand-supply matching
- **Replenishment** - Lot sizing, replenishment strategy, inventory routing
- **Supporting** - Demand forecasting

### Quick Start

```bash
# Install skills to Claude Code
cd Inventory-Placement
cp -r skills/* ~/.claude/skills/
```

**Full Skills Documentation:** [skills/README.md](./skills/README.md)

## Solver Libraries

This project uses validated computational solvers (install via `pip`):

### **stockpyl** (Inventory Math)
Provides validated algorithms for inventory theory:

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

### **PuLP** (Optimization)
Mixed-Integer Programming for network and allocation decisions:

```python
import pulp
prob = pulp.LpProblem("FacilityLocation", pulp.LpMinimize)
# Binary variables for facility open/close
# Continuous variables for flow allocation
# Solve with included CBC solver
prob.solve(pulp.PULP_CBC_CMD(msg=0))
```

### **scikit-learn** (Clustering)
Store/location clustering for allocation tiers:

```python
from sklearn.cluster import KMeans
```

## Example Case Study

The `example_retailer_x/` directory contains a complete worked example:

- **Retailer_X.md** - 23-page analytical report
- **solve.py** - Python implementation solving all three problems

**Scenario:** Mid-size electronics retailer with 4 stores, 2 DCs, 2 SKUs, and a DC capacity constraint.

**Results:**
- Optimal DC-to-store assignments
- Inventory policies (reorder points and order quantities)
- 12-week vendor order schedule
- Total annual cost analysis: $635,107

## Usage

An AI agent working in this directory will:
1. Match the user's problem to relevant skill(s)
2. Use assessment questions to understand context
3. Apply the preferred solver to compute answers
4. Fall back to custom code for edge cases

### Installation

```bash
# From the repository root
pip install -r requirements.txt

# Or install individually
pip install stockpyl pulp scikit-learn numpy scipy
```

## Skills Overview

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

## Contributing

Contributions welcome! Ways to improve this project:

1. **New case studies** - Add examples from different industries
2. **Enhanced skills** - Improve existing skill documentation
3. **Additional solvers** - Integrate other optimization libraries
4. **Visualization tools** - Add plotting and reporting capabilities
5. **Integration guides** - Connect with ERP/WMS systems

### Contributing Skills

Each skill follows this structure:
1. YAML frontmatter with name and description
2. Assessment questions
3. Preferred solver with verified API calls
4. Frameworks and methodologies
5. Python code examples

See [skills/README.md](./skills/README.md) for detailed guidelines.

## Acknowledgments

This skills collection is derived from the [awesome-supply-chain](https://github.com/kishorkukreja/awesome-supply-chain) repository by Kishor Kukreja. The original repository contains 132 comprehensive supply chain skills covering a broader range of topics including:

- Core supply chain functions (planning, forecasting, warehouse operations)
- Domain-specific verticals (CPG, retail, manufacturing, energy, healthcare)
- Operations research problems (routing, packing, scheduling, cutting stock)
- Advanced optimization and AI/ML techniques

This repository focuses specifically on the **16 inventory placement skills** that solve the core inbound placement questions (where/how much/when). We're grateful to Kishor Kukreja for creating and sharing this comprehensive knowledge base with the supply chain community.

**Original Repository:** https://github.com/kishorkukreja/awesome-supply-chain

## License

Educational and research use. Component licenses:
- Skills framework: Derived from awesome-supply-chain (MIT License)
- stockpyl: Check [original repository](https://github.com/LarrySnyder/stockpyl) (MIT License)
- PuLP: BSD License
- This repository and modifications: MIT License (Copyright 2026 JainShekhar)

---

**Last Updated**: June 2026
