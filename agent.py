"""
Inventory Placement Agent - Claude SDK Implementation

An AI agent that:
1. Understands user questions about inventory placement
2. Finds relevant skills from the skills/ directory
3. Writes Python code using PuLP and stockpyl
4. Executes the code and provides natural language answers
"""

import os
import json
from anthropic import Anthropic
from tools import (
    list_available_skills,
    read_skill,
    execute_python_code,
    TOOLS
)

# Initialize Claude client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# System prompt that defines the agent's role and capabilities
SYSTEM_PROMPT = """You are an expert supply chain optimization agent specializing in inventory placement problems.

Your role is to help users solve three critical inventory decisions:
1. WHERE to send inventory - Which facilities should receive inventory?
2. HOW MUCH to place - What are optimal stocking levels?
3. WHEN to replenish - What timing and frequency for orders?

## Your Workflow:

1. **Understand the Problem**: When a user asks a question, identify:
   - What type of problem (facility location, inventory optimization, lot sizing, etc.)
   - What data they have (locations, demands, costs, constraints)
   - What they want to optimize (cost, service level, etc.)

2. **Find Relevant Skills**: Use the `list_available_skills` tool to see available skills, then use `read_skill` to load the relevant skill(s) that match the problem.

3. **Extract Methodology**: From the skill file, understand:
   - The preferred solver (PuLP, stockpyl, etc.)
   - Assessment questions to clarify problem details
   - Code examples and algorithms

4. **Gather Required Data**: Ask the user for any missing information needed to solve the problem (demands, costs, capacities, lead times, etc.)

5. **Write Python Code**: Create a complete, executable Python script that:
   - Imports required libraries (pulp, stockpyl, numpy, etc.)
   - Defines the data from user input
   - Implements the optimization model
   - Solves the problem
   - Returns results

6. **Execute and Interpret**: Use `execute_python_code` to run the script, then interpret the results in clear, business-friendly language.

## Available Libraries:
- **pulp**: Linear/Mixed-Integer Programming
- **stockpyl**: Inventory optimization (EOQ, Wagner-Whitin, newsvendor, (r,Q), (s,S), multi-echelon)
- **numpy, scipy**: Numerical computing
- **pandas**: Data manipulation

## Important Guidelines:
- Always use the skills as reference for correct solver usage
- Write complete, self-contained Python code that can execute independently
- Handle errors gracefully and explain what went wrong
- Provide results in business terms (costs, quantities, schedules) not just numbers
- If data is missing, ask clarifying questions before writing code
- Test your understanding of the problem before jumping to code

You have access to these tools to help you:
- list_available_skills: See all 16 available inventory placement skills
- read_skill: Read a specific skill file for detailed methodology
- execute_python_code: Run Python code and get results
"""


def process_tool_call(tool_name: str, tool_input: dict) -> str:
    """Execute a tool call and return the result."""
    if tool_name == "list_available_skills":
        return list_available_skills()
    elif tool_name == "read_skill":
        return read_skill(tool_input["skill_name"])
    elif tool_name == "execute_python_code":
        return execute_python_code(tool_input["code"])
    else:
        return f"Error: Unknown tool {tool_name}"


def run_agent(user_question: str, max_turns: int = 15) -> str:
    """
    Run the inventory placement agent with a user question.

    Args:
        user_question: The user's inventory placement question
        max_turns: Maximum conversation turns (to prevent infinite loops)

    Returns:
        The agent's final answer
    """
    messages = [{"role": "user", "content": user_question}]

    print(f"\n{'='*80}")
    print(f"USER QUESTION: {user_question}")
    print(f"{'='*80}\n")

    for turn in range(max_turns):
        # Call Claude with tools
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages
        )

        print(f"\n--- Turn {turn + 1} ---")

        # Process the response
        if response.stop_reason == "end_turn":
            # Agent provided final answer
            final_text = ""
            for block in response.content:
                if block.type == "text":
                    final_text += block.text

            print(f"\nAGENT FINAL ANSWER:\n{final_text}\n")
            return final_text

        elif response.stop_reason == "tool_use":
            # Agent wants to use tools
            assistant_message = {"role": "assistant", "content": response.content}
            messages.append(assistant_message)

            # Process each tool call
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    print(f"Tool Call: {block.name}")
                    if block.name == "execute_python_code":
                        print("  (Executing Python code...)")
                    else:
                        print(f"  Input: {block.input}")

                    result = process_tool_call(block.name, block.input)

                    if block.name == "execute_python_code":
                        # Show abbreviated output for code execution
                        result_preview = result[:500] + "..." if len(result) > 500 else result
                        print(f"  Result: {result_preview}")
                    else:
                        print(f"  Result: {result[:200]}...")

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })

            # Add tool results to conversation
            messages.append({"role": "user", "content": tool_results})

        else:
            # Unexpected stop reason
            print(f"Unexpected stop reason: {response.stop_reason}")
            break

    return "Error: Maximum turns reached without final answer"


def interactive_mode():
    """Run the agent in interactive mode where users can ask multiple questions."""
    print("\n" + "="*80)
    print("INVENTORY PLACEMENT AGENT - Interactive Mode")
    print("="*80)
    print("\nI can help you solve inventory placement problems:")
    print("  • WHERE to send inventory (facility location, network design)")
    print("  • HOW MUCH to stock (safety stock, reorder points, EOQ)")
    print("  • WHEN to replenish (lot sizing, order schedules)")
    print("\nType 'exit' to quit\n")

    while True:
        try:
            question = input("\nYour question: ").strip()

            if question.lower() in ['exit', 'quit', 'q']:
                print("\nGoodbye!")
                break

            if not question:
                continue

            answer = run_agent(question)

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            print("Please try again.")


if __name__ == "__main__":
    import sys

    # Check for API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        print("\nSet it with:")
        print("  export ANTHROPIC_API_KEY='your-api-key-here'")
        sys.exit(1)

    # Check if question provided as command line argument
    if len(sys.argv) > 1:
        # Single question mode
        question = " ".join(sys.argv[1:])
        answer = run_agent(question)
    else:
        # Interactive mode
        interactive_mode()
