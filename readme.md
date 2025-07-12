🇮🇳 Indian OSINT Chatbot

A lightweight terminal-based chatbot that helps users discover Indian OSINT (Open Source Intelligence) tools through keyword queries or natural language questions. Supports structured input detection (e.g., GSTIN, phone number, vehicle number) and smart category-based intent mapping.
🧠 Features

    🔍 Natural language detection (e.g., "What do we have for court cases?")

    🧾 Structured input classification (GSTIN, vehicle plates, phone numbers)

    📂 Search across categorized tools (People Search, Transport, Court Records, etc.)

    🛠️ Easily extensible tool database via tools.json

    🇮🇳 Focused exclusively on Indian OSINT platforms

    📦 Zero dependencies (only uses Python standard library)

📁 Folder Structure

osint-chatbot/
├── data/
│   └── tools.json             # Your main OSINT database
├── modules/
│   ├── classifier.py          # Regex classifier for structured inputs
│   ├── tool_handler.py        # Tool loading, searching, and displaying logic
│   └── intent_mapper.py       # Natural language keyword extractor
├── .gitignore
├── requirements.txt
├── README.md
└── main.py                    # Entry point chatbot interface

🚀 How to Run
1. Clone the Repository

git clone https://github.com/your-username/osint-chatbot.git
cd osint-chatbot

2. (Optional) Set up a Virtual Environment

python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

3. Install Dependencies

pip install -r requirements.txt

4. Start the Chatbot

python main.py

💬 Sample Commands

    MH04DN7712 → Vehicle plate

    9876543210 or +91... → Phone number

    27AAFCE2018A1Z5 → GSTIN

    "what forums do we have?" → Natural language

    "show all" or "list all tools" → Show everything

🧩 Add or Edit Tools

Edit the data/tools.json file to add, update, or remove tools. Each entry follows this format:

{
  "name": "Tool Name",
  "url": "https://example.com",
  "category": "Category Name",
  "description": "Short summary of what the tool does."
}

You can add new categories freely—no code change needed.
✅ Requirements

    Python 3.7+

    Only uses json, re, and typing from the Python standard library

📄 .gitignore

Ensure the following are ignored:

__pycache__/
*.py[cod]
venv/
.env/
.vscode/
.DS_Store

📚 Credits

Built with ❤️ by TheKrazyKiwi29
