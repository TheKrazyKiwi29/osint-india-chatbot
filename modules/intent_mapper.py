
# modules/intent_mapper.py

from typing import Optional

# A basic keyword mapping from intent phrases to actual tool-related keywords
INTENT_KEYWORDS = {
    # GST
    "check gst": "gst",
    "gst number": "gst",
    "verify gstin": "gst",

    # Vehicle
    "track vehicle": "vehicle",
    "vehicle info": "vehicle",
    "lookup plate": "vehicle",
    "license plate": "vehicle",
    "vehicle number": "vehicle",
    "vehicle plate": "vehicle",
    "plate number": "vehicle",
    "rto": "vehicle",

    # Phone
    "phone number": "phone",
    "trace mobile": "phone",
    "mobile number": "phone",
    "imei check": "imei",
    "locate device": "imei",

    # Court
    "court record": "court",
    "judgment": "court",
    "case record": "court",
    "legal case": "court",

    # Criminal
    "criminal record": "prison",
    "jail": "prison",
    "fir": "prison",

    # Voter ID
    "voter id": "voter",
    "check voter": "voter",
    "election search": "voter",

    # Missing
    "missing person": "missing",
    "report child": "missing",
    "lost child": "missing",

    # Weather
    "weather": "climate",
    "forecast": "climate",
    "rain": "climate",

    # Transport
    "train status": "train",
    "train info": "train",
    "bus schedule": "bus",
    "bus route": "bus",
    "metro timings": "bus",
    "flight": "flight",
    "flight tracker": "flight",

    # Business
    "company info": "business",
    "corporate": "business",
    "company search": "business",

    # News
    "news": "news",
    "cyber crime": "cyber",
    "cyber news": "cyber",

    # People
    "aadhar": "aadhar",
    "ration card": "ration",
    "uidai": "aadhar",

    # Forums
    "forums": "forums",
    "reddit": "forums",
    "askindia": "forums",
    "india subreddit": "forums",
    "quora": "forums",
}

def detect_intent(text: str) -> Optional[str]:
    """
    Attempts to infer a keyword based on natural language intent.

    Args:
        text (str): User's natural language input.

    Returns:
        Optional[str]: A keyword to search tools with, or None if not found.
    """
    text = text.lower()
    for phrase, keyword in INTENT_KEYWORDS.items():
        if phrase in text:
            return keyword
    return None
