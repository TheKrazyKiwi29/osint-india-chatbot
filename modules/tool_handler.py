# modules/tool_handler.py

import json
from typing import List, Dict, Set

# Define the path to the JSON file
# Using a relative path makes the code more portable
TOOLS_FILE_PATH = 'data/tools.json'

def load_tools() -> List[Dict]:
    """
    Loads the OSINT tools from the JSON file.
    
    Returns:
        List[Dict]: A list of tool dictionaries.
                    Returns an empty list if the file is not found or is invalid.
    """
    try:
        with open(TOOLS_FILE_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: The file {TOOLS_FILE_PATH} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file {TOOLS_FILE_PATH} contains invalid JSON.")
        return []

def list_categories(tools: List[Dict]) -> List[str]:
    """
    Extracts a sorted list of unique categories from the tools data.

    Args:
        tools (List[Dict]): The list of tool dictionaries.

    Returns:
        List[str]: A sorted list of unique category names.
    """
    categories: Set[str] = set()
    for tool in tools:
        if 'category' in tool:
            categories.add(tool['category'])
    return sorted(list(categories))

def search_by_keyword(tools: List[Dict], keyword: str) -> List[Dict]:
    """
    Searches for tools by a keyword in their name or description.

    Args:
        tools (List[Dict]): The list of tool dictionaries.
        keyword (str): The keyword to search for (case-insensitive).

    Returns:
        List[Dict]: A list of tools matching the keyword.
    """
    keyword = keyword.lower()
    results = []
    for tool in tools:
        name = tool.get('name', '').lower()
        description = tool.get('description', '').lower()
        if keyword in name or keyword in description:
            results.append(tool)
    return results


def display_tools(tools: List[Dict]):
    """
    Prints a list of tools in a formatted way.
    """
    if not tools:
        print("❌ No matching tools found.")
    else:
        print(f"🔍 Found {len(tools)} tool(s):\n")
        for tool in tools:
            print(f"🧰 {tool['name']}\n📎 {tool['url']}\n🗂️ Category: {tool['category']}\n📖 {tool['description']}\n")


from difflib import get_close_matches

def search_by_fuzzy_keyword(tools: List[Dict], keyword: str) -> List[Dict]:
    """
    Performs a fuzzy keyword search on tool names, categories, and descriptions.
    """
    keyword = keyword.lower()
    results = []

    for tool in tools:
        content = f"{tool.get('name', '')} {tool.get('description', '')} {tool.get('category', '')}".lower()
        if keyword in content:
            results.append(tool)

    # If no direct matches, try fuzzy matching against all searchable fields
    if not results:
        all_texts = [f"{tool['name']} {tool['description']} {tool['category']}" for tool in tools]
        matches = get_close_matches(keyword, all_texts, n=5, cutoff=0.5)
        for match in matches:
            for tool in tools:
                text = f"{tool['name']} {tool['description']} {tool['category']}"
                if match in text:
                    results.append(tool)
                    break

    return results
