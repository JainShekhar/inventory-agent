# Inventory Placement Agent - Usage Guide

An AI-powered agent built with Claude SDK that understands inventory placement questions, finds relevant optimization skills, writes Python code, and provides natural language answers.

## What It Does

The agent can solve three types of inventory placement problems:

1. **WHERE to send** - Facility location, network design, DC assignment
2. **HOW MUCH to place** - Safety stock, EOQ, reorder points, newsvendor
3. **WHEN to replenish** - Lot sizing, order schedules, Wagner-Whitin

## How It Works

```
User Question
     ↓
Agent understands problem type
     ↓
Loads relevant skills from skills/
     ↓
Writes Python code (PuLP/stockpyl)
     ↓
Executes code and gets results
     ↓
Explains answer in natural language
```

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install Anthropic SDK

```bash
pip install anthropic
```

### 3. Set API Key

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Get your API key from: https://console.anthropic.com/

## Usage

### Interactive Mode

Ask multiple questions in a conversation:

```bash
python agent.py
```

Example session:
```
Your question: I have 3 warehouses and 5 customers. Which warehouses should I open?

[Agent asks clarifying questions about costs, demands, capacities]

Your question: [Provide data...]

[Agent writes code, solves problem, explains results]

Your question: exit
```

### Single Question Mode

Ask one question via command line:

```bash
python agent.py "What's the optimal order quantity for annual demand of 10,000 units, unit cost $50, holding rate 20%, and order cost $200?"
```

### Example Questions

Run pre-built examples:

```bash
# See available examples
python example_questions.py

# Run specific example (1-6)
python example_questions.py 1

# Run all examples
python example_questions.py all
```

## Example Questions

### 1. Facility Location
```
I have 3 potential warehouses and 5 customers.
Fixed costs: A=$50k, B=$60k, C=$45k
Demands: [100, 150, 80, 120, 90]
Transport costs: A=[2,5,4,7,6], B=[6,3,5,2,4], C=[4,6,3,5,2]
Capacities: 300 units each
Which warehouses should I open?
```

### 2. Economic Order Quantity
```
Annual demand: 12,000 units
Unit cost: $25
Holding rate: 20% per year
Order cost: $100
What's the optimal order quantity?
```

### 3. Newsvendor Problem
```
Seasonal demand: Normal(mean=500, std=100)
Cost: $20, Price: $50, Salvage: $5
How many units should I order?
```

### 4. Reorder Point
```
Weekly demand: Normal(mean=100, std=20)
Lead time: 2 weeks
Unit cost: $30, Holding rate: 25%
Stockout cost: $50/unit, Order cost: $200
What's my reorder point and order quantity?
```

### 5. Dynamic Lot Sizing
```
6-month forecast: [500, 600, 550, 700, 650, 600]
Unit cost: $20, Holding: $2/unit/month, Order: $500
When and how much should I order?
```

### 6. Network Optimization
```
2 DCs, 4 stores
Store demands: [200, 150, 180, 120]
DC capacities: [350, 300]
Shipping costs: DC1=[3,5,4,7], DC2=[6,3,5,4]
How to assign stores to DCs?
```

## Agent Architecture

### Core Components

**agent.py** - Main agent loop
- Handles conversation with Claude
- Processes tool calls
- Manages multi-turn interactions

**tools.py** - Tool implementations
- `list_available_skills()` - Lists 16 available skills
- `read_skill(name)` - Reads skill methodology
- `execute_python_code(code)` - Runs optimization code

**example_questions.py** - Pre-built test cases
- 6 example questions covering all problem types
- Can run individually or all at once

### Agent Workflow

1. **Understanding Phase**
   - Agent analyzes user question
   - Identifies problem type (WHERE/HOW MUCH/WHEN)
   - Lists available skills

2. **Skill Loading Phase**
   - Reads relevant skill files
   - Understands preferred solvers
   - Reviews code examples

3. **Data Gathering Phase**
   - Identifies missing information
   - Asks clarifying questions
   - Validates data completeness

4. **Code Generation Phase**
   - Writes complete Python script
   - Uses PuLP for network/location problems
   - Uses stockpyl for inventory problems
   - Includes all imports and data

5. **Execution Phase**
   - Runs code in subprocess
   - Captures output and errors
   - Handles timeouts

6. **Interpretation Phase**
   - Explains results in business terms
   - Provides recommendations
   - Answers follow-up questions

## Advanced Usage

### Programmatic API

```python
from agent import run_agent

question = "What's the EOQ for demand=10000, cost=$50, holding=20%, order_cost=$200?"
answer = run_agent(question)
print(answer)
```

### Custom Tools

Add new tools in `tools.py`:

```python
def my_custom_tool(param):
    # Your implementation
    return result

# Add to TOOLS list
TOOLS.append({
    "name": "my_custom_tool",
    "description": "...",
    "input_schema": {...}
})
```

### Modify Agent Behavior

Edit `SYSTEM_PROMPT` in `agent.py` to:
- Change tone or style
- Add domain-specific knowledge
- Customize workflow steps
- Add validation rules

## Troubleshooting

### API Key Issues
```bash
# Check if key is set
echo $ANTHROPIC_API_KEY

# Set temporarily
export ANTHROPIC_API_KEY='sk-ant-...'

# Set permanently (add to ~/.bashrc or ~/.zshrc)
echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.bashrc
```

### Import Errors
```bash
# Make sure all dependencies are installed
pip install -r requirements.txt
pip install anthropic

# Check installations
python -c "import pulp; import stockpyl; import anthropic; print('All imports OK')"
```

### Code Execution Errors

The agent runs code in a subprocess with a 30-second timeout. If code fails:
- Check that PuLP/stockpyl are installed
- Verify data format in the question
- Look at stderr output for error messages

### Skill Not Found

If agent can't find a skill:
```bash
# Verify skills directory exists
ls skills/

# Should show 16 skill folders
# If empty, skills/ was not properly copied
```

## Performance Tips

1. **Be Specific**: Provide all data upfront to reduce back-and-forth
2. **Use Examples**: Reference the example questions for formatting
3. **Structured Data**: Use clear formats like arrays or lists
4. **Problem Type**: Mention the problem type (EOQ, facility location, etc.)

## Cost Estimation

Using Claude Sonnet 4:
- Simple question: ~50K tokens (~$0.15)
- Complex question: ~100K tokens (~$0.30)
- With multiple tool calls and iterations

## Limitations

- Code execution timeout: 30 seconds
- Max conversation turns: 15
- Cannot access external data sources
- No visualization generation (text output only)
- Requires all data provided by user

## Future Enhancements

- [ ] Add visualization generation (plots, charts)
- [ ] Support CSV/Excel file uploads
- [ ] Multi-period simulation
- [ ] Sensitivity analysis
- [ ] Integration with ERP systems
- [ ] Web UI interface
- [ ] Caching of skill files
- [ ] Parallel problem solving

## Support

- Issues: https://github.com/JainShekhar/inventory-agent/issues
- Skills Documentation: See [SKILLS_README.md](SKILLS_README.md)
- Example Case Study: See [example_retailer_x/](example_retailer_x/)

## License

MIT License - See [LICENSE](LICENSE)
