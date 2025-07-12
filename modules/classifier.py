# modules/classifier.py

import re
from typing import Optional

# Define regex patterns for different Indian data types
# We use re.IGNORECASE to make patterns case-insensitive
PATTERNS = {
    'gstin': re.compile(r"^\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}Z[A-Z\d]{1}$", re.IGNORECASE),
    'vehicle_number': re.compile(r"^[A-Z]{2}\d{1,2}[A-Z]{1,3}\d{1,4}$", re.IGNORECASE),
    'phone_number': re.compile(r"^(?:\+91|0)?[6-9]\d{9}$")
}

def classify_input(user_input: str) -> Optional[str]:
    """
    Classifies the user input by matching it against predefined regex patterns.

    Args:
        user_input (str): The text entered by the user.

    Returns:
        Optional[str]: The type of input ('gstin', 'vehicle_number', 'phone_number') 
                       if a specific pattern is matched, otherwise None.
    """
    # Clean up input by stripping leading/trailing whitespace
    user_input = user_input.strip()

    for input_type, pattern in PATTERNS.items():
        if pattern.fullmatch(user_input):
            return input_type
    
    return None # Return None if no specific pattern matches
