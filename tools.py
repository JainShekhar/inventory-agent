"""
Tool definitions for the Inventory Placement Agent

These tools allow the Claude agent to:
1. List available skills
2. Read skill files
3. Execute Python code to solve problems
"""

import os
import json
import subprocess
import tempfile
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent
SKILLS_DIR = PROJECT_ROOT / "skills"


def list_available_skills() -> str:
    """
    List all available inventory placement skills.

    Returns:
        JSON string with skill names and descriptions
    """
    skills = []

    if not SKILLS_DIR.exists():
        return json.dumps({"error": "Skills directory not found"})

    for skill_dir in SKILLS_DIR.iterdir():
        if skill_dir.is_dir():
            skill_file = skill_dir / "SKILL.md"
            if skill_file.exists():
                # Read the frontmatter to get description
                with open(skill_file, 'r') as f:
                    content = f.read()

                    # Extract description from frontmatter
                    if content.startswith('---'):
                        parts = content.split('---', 2)
                        if len(parts) >= 3:
                            frontmatter = parts[1]
                            for line in frontmatter.split('\n'):
                                if line.startswith('description:'):
                                    description = line.replace('description:', '').strip()
                                    skills.append({
                                        "name": skill_dir.name,
                                        "description": description
                                    })
                                    break

    return json.dumps({
        "total_skills": len(skills),
        "skills": skills
    }, indent=2)


def read_skill(skill_name: str) -> str:
    """
    Read a specific skill file.

    Args:
        skill_name: Name of the skill (e.g., 'facility-location-problem')

    Returns:
        Content of the skill file
    """
    skill_file = SKILLS_DIR / skill_name / "SKILL.md"

    if not skill_file.exists():
        return f"Error: Skill '{skill_name}' not found. Use list_available_skills to see available skills."

    with open(skill_file, 'r') as f:
        content = f.read()

    return content


def execute_python_code(code: str) -> str:
    """
    Execute Python code in a safe subprocess and return the output.

    Args:
        code: Python code to execute

    Returns:
        Output of the code execution (stdout + stderr)
    """
    # Create a temporary file for the code
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(code)
        temp_file = f.name

    try:
        # Execute the code
        result = subprocess.run(
            ['python', temp_file],
            capture_output=True,
            text=True,
            timeout=30  # 30 second timeout
        )

        output = ""
        if result.stdout:
            output += "STDOUT:\n" + result.stdout
        if result.stderr:
            output += "\nSTDERR:\n" + result.stderr
        if result.returncode != 0:
            output += f"\n\nExit code: {result.returncode}"

        return output if output else "Code executed successfully with no output"

    except subprocess.TimeoutExpired:
        return "Error: Code execution timed out after 30 seconds"
    except Exception as e:
        return f"Error executing code: {str(e)}"
    finally:
        # Clean up temporary file
        try:
            os.unlink(temp_file)
        except:
            pass


# Tool definitions for Claude API
TOOLS = [
    {
        "name": "list_available_skills",
        "description": "List all available inventory placement skills. Use this to see what skills are available before reading a specific skill. Returns a JSON object with skill names and descriptions.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "read_skill",
        "description": "Read the content of a specific skill file. Use this to understand the methodology, algorithms, and code examples for solving a particular type of inventory placement problem. The skill file contains assessment questions, preferred solvers, frameworks, and Python code examples.",
        "input_schema": {
            "type": "object",
            "properties": {
                "skill_name": {
                    "type": "string",
                    "description": "The name of the skill to read (e.g., 'facility-location-problem', 'inventory-optimization', 'economic-order-quantity')"
                }
            },
            "required": ["skill_name"]
        }
    },
    {
        "name": "execute_python_code",
        "description": "Execute Python code to solve the inventory placement problem. The code should be complete and self-contained, importing all necessary libraries (pulp, stockpyl, numpy, etc.) and defining all data. Returns the output of the code execution.",
        "input_schema": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "Complete Python code to execute. Should include imports, data definitions, problem solving, and print statements to show results."
                }
            },
            "required": ["code"]
        }
    }
]
