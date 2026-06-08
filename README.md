# Inventory Placement Agent

**An AI agent that solves supply chain inventory placement problems through natural language conversations.**

Ask questions in plain English, and the agent will understand your problem, write optimization code, execute it, and explain the results in business terms.

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/JainShekhar/inventory-agent.git
cd inventory-agent

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your Claude API key
export ANTHROPIC_API_KEY='your-api-key-here'

# 4. Run the agent
python agent.py
```

**Get your API key:** https://console.anthropic.com/

---

## 💬 Example Conversations

### Facility Location Problem

```
You: I have 3 potential warehouse locations and 5 customer cities.
     Fixed costs are: A=$50k, B=$60k, C=$45k
     Customer demands: [100, 150, 80, 120, 90] units/month
     Transport costs from A: [2, 5, 4, 7, 6] $/unit
     Transport costs from B: [6, 3, 5, 2, 4] $/unit
     Transport costs from C: [4, 6, 3, 5, 2] $/unit
     Each warehouse can handle 300 units/month.
     Which warehouses should I open?

Agent: Let me solve this facility location problem...
       [Writes and executes PuLP optimization code]
       
       SOLUTION:
       • Open Warehouse A and Warehouse C
       • Total monthly cost: $86,140
         - Fixed costs: $95,000
         - Transport costs: $1,140
       • Warehouse A serves: Cities 1, 2 (250 units)
       • Warehouse C serves: Cities 3, 4, 5 (290 units)
       • Warehouse B remains closed (saves $60k)
```

### Economic Order Quantity

```
You: Annual demand is 12,000 units, unit cost $25, holding rate 20%, order cost $100.
     What's the optimal order quantity?

Agent: [Solves using stockpyl EOQ]
       
       SOLUTION:
       • Optimal Order Quantity: 490 units
       • Orders per year: 24.5 times (about every 2 weeks)
       • Total annual cost: $2,449
         - Ordering cost: $1,225
         - Holding cost: $1,225
       
       RECOMMENDATION: Order 490 units every 15 days
```

### Newsvendor Problem

```
You: Seasonal demand: Normal(mean=500, std=100)
     Cost=$20, Price=$50, Salvage=$5
     How many should I order?

Agent: [Applies newsvendor model]
       
       SOLUTION:
       • Optimal order quantity: 584 units
       • Expected profit: $13,200
       • Service level: 80%
       • Risk: ~20% chance of stockout, ~20% chance of excess
       
       This balances the $30 profit margin against the $15 salvage loss.
```

---

## 🎯 What Problems Does It Solve?

The agent solves three types of inventory placement decisions:

### 1. WHERE to Send Inventory
- **Facility Location**: Which warehouses/DCs to open?
- **Network Design**: How to structure distribution networks?
- **Assignment**: Which DC serves which store?

**Skills:** `facility-location-problem`, `distribution-center-network`, `network-design`, `hub-location-problem`

### 2. HOW MUCH to Stock
- **Safety Stock**: Buffer inventory levels
- **Order Quantities**: EOQ, newsvendor, reorder points
- **Allocation**: How much at each location?

**Skills:** `inventory-optimization`, `economic-order-quantity`, `newsvendor-problem`, `multi-echelon-inventory`, `retail-allocation`, `demand-supply-matching`

### 3. WHEN to Replenish
- **Order Timing**: When to place orders?
- **Lot Sizing**: Batch sizes over time
- **Frequency**: How often to replenish?

**Skills:** `dynamic-lot-sizing`, `lot-sizing-problems`, `replenishment-strategy`, `retail-replenishment`, `inventory-routing-problem`

**Supporting:** `demand-forecasting`

---

## 🏗️ How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│  USER QUESTION (Natural Language)                               │
│  "I have 3 warehouses and 5 customers. Which should I open?"    │
└────────────────┬────────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────────┐
│  AGENT UNDERSTANDS                                              │
│  • Problem type: Facility location (WHERE to send)              │
│  • Missing data: costs, demands, capacities                     │
└────────────────┬────────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────────┐
│  LOADS RELEVANT SKILLS                                          │
│  • Reads: skills/facility-location-problem/SKILL.md             │
│  • Learns: PuLP solver, CFLP formulation, code examples         │
└────────────────┬────────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────────┐
│  ASKS CLARIFYING QUESTIONS (if needed)                          │
│  "What are the fixed costs? Customer demands? Capacities?"      │
└────────────────┬────────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────────┐
│  WRITES PYTHON CODE                                             │
│  import pulp                                                     │
│  prob = pulp.LpProblem("FacilityLocation", pulp.LpMinimize)    │
│  # ... complete optimization model ...                          │
│  prob.solve()                                                   │
└────────────────┬────────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────────┐
│  EXECUTES CODE SAFELY                                           │
│  • Runs in subprocess with 30-second timeout                    │
│  • Captures output and errors                                   │
└────────────────┬────────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────────┐
│  EXPLAINS RESULTS                                               │
│  "Open warehouses A and C. Total cost: $86,140.                 │
│   Warehouse A serves Cities 1,2. Warehouse C serves 3,4,5."     │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📦 Project Structure

```
inventory-agent/
├── agent.py                     # 🤖 Main AI agent (Claude SDK)
├── tools.py                     # 🔧 Agent tools (read skills, execute code)
├── example_questions.py         # 📝 6 pre-built test cases
│
├── skills/                      # 📚 16 optimization skills (SKILL.md files)
│   ├── facility-location-problem/
│   ├── inventory-optimization/
│   ├── economic-order-quantity/
│   ├── newsvendor-problem/
│   ├── dynamic-lot-sizing/
│   ├── multi-echelon-inventory/
│   └── ... (10 more)
│
├── example_retailer_x/          # 📊 Complete manual case study
│   ├── Retailer_X.md            # 23-page analytical report
│   └── solve.py                 # Direct Python implementation
│
├── requirements.txt             # Python dependencies
├── LICENSE                      # MIT License
└── README.md                    # This file
```

---

## 🎮 Usage Modes

### Interactive Mode (Recommended)

Ask multiple questions in a conversation:

```bash
python agent.py
```

Example session:
```
Your question: I have annual demand of 10,000 units. What's the optimal order quantity?

[Agent asks for: unit cost, holding rate, order cost]

Your question: Unit cost is $50, holding rate 20%, order cost $200

[Agent solves and explains EOQ]

Your question: What if demand increases to 15,000?

[Agent recalculates]

Your question: exit
Goodbye!
```

### Single Question Mode

Quick one-off questions:

```bash
python agent.py "What's the EOQ for demand=10000, cost=$50, holding=20%, order_cost=$200?"
```

### Pre-Built Examples

Test with 6 example questions:

```bash
# See available examples
python example_questions.py

# Run specific example
python example_questions.py 1    # Facility location
python example_questions.py 2    # Economic order quantity
python example_questions.py 3    # Newsvendor problem
python example_questions.py 4    # Reorder point (r,Q)
python example_questions.py 5    # Wagner-Whitin lot sizing
python example_questions.py 6    # Network optimization

# Run all examples
python example_questions.py all
```

---

## 🧠 Agent Architecture

### Core Components

**1. agent.py** - Conversation orchestrator
- Claude SDK integration with tool use
- Multi-turn conversation loop
- Interactive and command-line modes
- Max 15 turns to prevent infinite loops

**2. tools.py** - Three agent tools
- `list_available_skills()` - Returns all 16 skills with descriptions
- `read_skill(skill_name)` - Loads skill methodology and code examples
- `execute_python_code(code)` - Safely runs code in subprocess (30s timeout)

**3. example_questions.py** - Test suite
- 6 pre-built questions covering all problem types
- Can run individually or all at once
- Good templates for formatting your own questions

### Agent Workflow

1. **Understanding Phase**
   - Analyzes user question
   - Identifies problem type (WHERE/HOW MUCH/WHEN)
   - Lists available skills

2. **Learning Phase**
   - Reads relevant skill files
   - Studies preferred solvers (PuLP, stockpyl)
   - Reviews code examples and algorithms

3. **Data Gathering Phase**
   - Identifies missing information
   - Asks clarifying questions
   - Validates data completeness

4. **Code Generation Phase**
   - Writes complete Python script
   - Imports required libraries
   - Defines data structures
   - Implements optimization model

5. **Execution Phase**
   - Runs code in safe subprocess
   - Captures stdout/stderr
   - Handles timeouts and errors

6. **Interpretation Phase**
   - Explains numerical results
   - Provides business recommendations
   - Answers follow-up questions

---

## 🛠️ Technical Details

### Optimization Libraries

**PuLP** - Mixed-Integer Programming
```python
import pulp
prob = pulp.LpProblem("FacilityLocation", pulp.LpMinimize)
# Binary variables for open/close decisions
# Continuous variables for flow allocation
prob.solve(pulp.PULP_CBC_CMD(msg=0))
```

**stockpyl** - Inventory Algorithms
```python
from stockpyl.eoq import economic_order_quantity
from stockpyl.wagner_whitin import wagner_whitin
from stockpyl.newsvendor import newsvendor_normal
from stockpyl.rq import r_q_loss_function_approximation
from stockpyl.ss import s_s_power_approximation
from stockpyl.meio_general import meio_by_coordinate_descent
```

### Skills System

Each of the 16 skills contains:
- **Frontmatter**: Name and trigger keywords
- **Assessment Questions**: What data is needed
- **Preferred Solver**: Which library to use
- **Algorithms**: Mathematical formulations
- **Code Examples**: Working Python implementations
- **Frameworks**: Decision methodologies

Skills are stored in `skills/[skill-name]/SKILL.md` and loaded dynamically by the agent.

---

## 📚 Example Case Study: Retailer X

The `example_retailer_x/` folder contains a complete manual implementation:

**Scenario:** Mid-size electronics retailer
- 4 stores across the US
- 2 distribution centers (Atlanta, Dallas)
- 2 product SKUs with different demand patterns
- DC capacity constraint (labor shortage)

**Problems Solved:**
1. **WHERE** - Optimal DC-to-store assignment (PuLP transportation LP)
2. **HOW MUCH** - Inventory policies at all locations (stockpyl r,Q optimization)
3. **WHEN** - 12-week vendor order schedule (stockpyl Wagner-Whitin DP)

**Files:**
- `Retailer_X.md` - 23-page analytical report with full methodology
- `solve.py` - Complete Python implementation

**Run it:**
```bash
cd example_retailer_x
python solve.py
```

This demonstrates how to solve problems manually without the agent.

---

## 🔑 Requirements

### System Requirements
- Python 3.7+
- Internet connection (for Claude API)

### Python Dependencies

Install all at once:
```bash
pip install -r requirements.txt
```

Or individually:
```bash
pip install anthropic      # Claude SDK (required for agent)
pip install pulp           # Linear/Mixed-Integer Programming
pip install stockpyl       # Inventory optimization algorithms
pip install numpy scipy    # Numerical computing
pip install scikit-learn   # Optional: for clustering
pip install pandas         # Optional: for data manipulation
```

### API Key

Get your Anthropic API key from: https://console.anthropic.com/

Set it as an environment variable:
```bash
# Temporary (current session)
export ANTHROPIC_API_KEY='sk-ant-...'

# Permanent (add to ~/.bashrc or ~/.zshrc)
echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.bashrc
source ~/.bashrc
```

---

## 💡 Tips for Best Results

### 1. Provide Complete Data Upfront

❌ Vague: "Help me with warehouse location"

✅ Specific: "I have 3 warehouses with fixed costs [50k, 60k, 45k], 5 customers with demands [100, 150, 80, 120, 90], and transport costs [[2,5,4,7,6], [6,3,5,2,4], [4,6,3,5,2]]. Which warehouses should I open?"

### 2. Use Structured Formats

- Arrays: `[100, 150, 80]`
- Matrices: `[[1,2,3], [4,5,6]]`
- Units: "units/week", "$/unit", "days"

### 3. Mention Problem Type

Speeds up skill selection:
- "This is a facility location problem..."
- "I need to calculate EOQ..."
- "This is a newsvendor situation..."

### 4. Reference Examples

"Similar to example 1 in example_questions.py but with..."

### 5. Ask Follow-up Questions

The agent maintains context:
- "What if demand doubles?"
- "How sensitive is this to ordering cost?"
- "What's the impact of opening warehouse B?"

---

## 🚨 Troubleshooting

### API Key Issues

```bash
# Check if set
echo $ANTHROPIC_API_KEY

# Test connection
python -c "from anthropic import Anthropic; print(Anthropic().messages.create(model='claude-sonnet-4-20250514', max_tokens=10, messages=[{'role':'user','content':'hi'}]).content)"
```

### Import Errors

```bash
# Verify installations
python -c "import pulp; import stockpyl; import anthropic; print('✓ All imports OK')"

# Reinstall if needed
pip install --upgrade -r requirements.txt
```

### Code Execution Fails

- Check that PuLP and stockpyl are installed
- Look at STDERR in the output for error details
- Verify data format matches the skill examples
- Try the same code manually: `python -c "your code here"`

### Skill Not Found

```bash
# Verify skills directory
ls skills/

# Should show 16 folders
# If empty, you're in wrong directory or skills weren't cloned
```

---

## 📊 Cost & Performance

### API Costs (Claude Sonnet 4)

- **Simple question**: ~50K tokens → ~$0.15
- **Complex question**: ~100K tokens → ~$0.30
- **Multi-turn conversation**: Varies by complexity

### Performance

- **Understanding**: < 5 seconds
- **Code generation**: 10-20 seconds
- **Execution**: 1-30 seconds (depends on problem size)
- **Total per question**: Typically 30-60 seconds

### Limitations

- Code execution timeout: 30 seconds
- Max conversation turns: 15
- Cannot access external data (files, databases)
- Text output only (no charts/visualizations)
- Requires all data from user

---

## 🌟 Skills Reference

The agent uses 16 specialized skills:

### Network & Location (WHERE)
- `facility-location-problem` - UFLP, CFLP, p-median, p-center
- `distribution-center-network` - Multi-echelon DC design
- `network-design` - End-to-end network strategy
- `hub-location-problem` - Hub-and-spoke networks

### Inventory & Stocking (HOW MUCH)
- `inventory-optimization` - (r,Q) and (s,S) policies
- `economic-order-quantity` - EOQ, EPQ, quantity discounts
- `newsvendor-problem` - Single-period stocking
- `multi-echelon-inventory` - Safety stock positioning
- `retail-allocation` - Store-level allocation
- `demand-supply-matching` - Constrained allocation

### Timing & Replenishment (WHEN)
- `dynamic-lot-sizing` - Wagner-Whitin, time-varying demand
- `lot-sizing-problems` - Silver-Meal, POQ, LUC
- `replenishment-strategy` - Policy selection
- `retail-replenishment` - Store replenishment rules
- `inventory-routing-problem` - Joint inventory + routing

### Supporting
- `demand-forecasting` - Demand estimation

**Detailed documentation:** See [SKILLS_REFERENCE.md](SKILLS_REFERENCE.md)

---

## 🤝 Acknowledgments

### Source Material

This project is derived from:
- **[awesome-supply-chain](https://github.com/kishorkukreja/awesome-supply-chain)** by Kishor Kukreja - Original 132 supply chain skills collection (MIT License)
- **[stockpyl](https://github.com/LarrySnyder/stockpyl)** by Larry Snyder - Inventory optimization algorithms library (MIT License)

We focused on the 16 inventory placement skills and built the AI agent on top.

### Technologies

- **Claude 4 Sonnet** by Anthropic - AI reasoning and code generation
- **PuLP** - Linear programming (BSD License)
- **NumPy/SciPy** - Scientific computing
- Operations research literature and validated methodologies

### Community

Thank you to the supply chain and operations research community for the foundational work in inventory optimization and network design.

---

## 📄 License

MIT License - Copyright (c) 2026 JainShekhar

See [LICENSE](LICENSE) file for details.

This project incorporates work from:
- awesome-supply-chain (MIT License, Kishor Kukreja)
- stockpyl (MIT License, Larry Snyder)

---

## 🔗 Links

- **Repository**: https://github.com/JainShekhar/inventory-agent
- **Issues**: https://github.com/JainShekhar/inventory-agent/issues
- **Claude API**: https://console.anthropic.com/
- **PuLP Documentation**: https://coin-or.github.io/pulp/
- **stockpyl Documentation**: https://stockpyl.readthedocs.io/

---

## 🚀 Next Steps

1. **Try it now**: `export ANTHROPIC_API_KEY='...' && python agent.py`
2. **Run examples**: `python example_questions.py`
3. **Read case study**: `example_retailer_x/Retailer_X.md`
4. **Explore skills**: `ls skills/`
5. **Ask your question**: Start with your real inventory problem!

---

**Built with Claude 4 Sonnet** 🤖
