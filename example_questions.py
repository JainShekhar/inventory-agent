"""
Example questions to test the Inventory Placement Agent

Run with: python example_questions.py
"""

from agent import run_agent

# Example questions covering different types of problems
EXAMPLE_QUESTIONS = [
    # Facility Location Problem
    {
        "category": "WHERE to send (Facility Location)",
        "question": """I have 3 potential warehouse locations and 5 customer cities.
The fixed costs to open warehouses are: Location A: $50,000, B: $60,000, C: $45,000.
Customer demands per month: City 1: 100 units, City 2: 150, City 3: 80, City 4: 120, City 5: 90.
Transportation costs per unit from each warehouse to each city:
- From A: [2, 5, 4, 7, 6]
- From B: [6, 3, 5, 2, 4]
- From C: [4, 6, 3, 5, 2]
Each warehouse can handle up to 300 units per month.
Which warehouses should I open to minimize total cost?"""
    },

    # Economic Order Quantity
    {
        "category": "HOW MUCH to order (EOQ)",
        "question": """I sell a product with annual demand of 12,000 units.
Each unit costs $25, and my holding cost rate is 20% per year.
The fixed cost to place an order is $100.
What's the optimal order quantity, and how often should I order?"""
    },

    # Newsvendor Problem
    {
        "category": "HOW MUCH to stock (Newsvendor)",
        "question": """I'm ordering seasonal items for the holiday season.
Demand is normally distributed with mean 500 units and standard deviation 100 units.
Each unit costs me $20 and sells for $50.
Unsold items can be salvaged for $5 each.
How many units should I order to maximize profit?"""
    },

    # Reorder Point (r,Q) Policy
    {
        "category": "HOW MUCH safety stock (r,Q policy)",
        "question": """My weekly demand is normally distributed with mean 100 units and std dev 20 units.
Lead time from supplier is 2 weeks. Unit cost is $30, holding cost rate is 25% per year.
Stockout cost is $50 per unit (lost sales). Fixed ordering cost is $200.
What should my reorder point and order quantity be?"""
    },

    # Wagner-Whitin (Dynamic Lot Sizing)
    {
        "category": "WHEN to order (Wagner-Whitin)",
        "question": """I have a 6-month demand forecast: [500, 600, 550, 700, 650, 600] units.
Each unit costs $20, holding cost is $2 per unit per month, and ordering cost is $500.
When should I place orders and how much should I order each time?"""
    },

    # Multi-location problem
    {
        "category": "Network optimization",
        "question": """I have 2 DCs and 4 stores. Weekly demands at stores: [200, 150, 180, 120].
DC capacities: DC1 can handle 350 units/week, DC2 can handle 300 units/week.
Shipping costs per unit:
- DC1 to stores: [3, 5, 4, 7]
- DC2 to stores: [6, 3, 5, 4]
How should I assign stores to DCs to minimize shipping costs?"""
    }
]


def run_all_examples():
    """Run all example questions."""
    print("\n" + "="*80)
    print("RUNNING ALL EXAMPLE QUESTIONS")
    print("="*80)

    for i, example in enumerate(EXAMPLE_QUESTIONS, 1):
        print(f"\n\n{'='*80}")
        print(f"EXAMPLE {i}/{len(EXAMPLE_QUESTIONS)}: {example['category']}")
        print(f"{'='*80}\n")

        answer = run_agent(example['question'])

        print(f"\n{'─'*80}")
        print("DONE")
        print(f"{'─'*80}\n")

        # Wait for user to continue (optional)
        # input("Press Enter to continue to next example...")


def run_single_example(index: int):
    """Run a single example by index (1-based)."""
    if 1 <= index <= len(EXAMPLE_QUESTIONS):
        example = EXAMPLE_QUESTIONS[index - 1]
        print(f"\nRunning example {index}: {example['category']}\n")
        answer = run_agent(example['question'])
    else:
        print(f"Error: Example index must be between 1 and {len(EXAMPLE_QUESTIONS)}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        # Run specific example
        try:
            index = int(sys.argv[1])
            run_single_example(index)
        except ValueError:
            print(f"Usage: python example_questions.py [1-{len(EXAMPLE_QUESTIONS)}]")
    else:
        # Show menu
        print("\nAvailable example questions:")
        for i, example in enumerate(EXAMPLE_QUESTIONS, 1):
            print(f"  {i}. {example['category']}")

        print(f"\nUsage:")
        print(f"  python example_questions.py [1-{len(EXAMPLE_QUESTIONS)}]  # Run specific example")
        print(f"  python example_questions.py all                             # Run all examples")

        choice = input("\nEnter example number (or 'all'): ").strip()

        if choice.lower() == 'all':
            run_all_examples()
        else:
            try:
                run_single_example(int(choice))
            except ValueError:
                print("Invalid input")
