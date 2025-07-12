
# main.py

from modules.tool_handler import load_tools, search_by_keyword, display_tools, search_by_fuzzy_keyword  
from modules.classifier import classify_input
from modules.intent_mapper import detect_intent  # NEW IMPORT

def suggest_tools(input_type: str):
    suggestions = {
        'gstin': ['gst'],
        'vehicle_number': ['vehicle'],
        'phone_number': ['phone', 'imei'],
    }
    return suggestions.get(input_type, [])

def display_tools(tools):
    if not tools:
        print("❌ No matching tools found.")
    else:
        print(f"🔍 Found {len(tools)} tool(s):\n")
        for tool in tools:
            print(f"🧰 {tool['name']}\n📎 {tool['url']}\n🗂️ Category: {tool['category']}\n📖 {tool['description']}\n")

def chatbot():
    tools = load_tools()
    if not tools:
        print("⚠️ Error loading tools.json. Exiting.")
        return

    print("\n🤖 Namaste!!! Welcome to the Indian OSINT Chatbot!")
    print("Type your query (GST number, phone, vehicle plate, or ask in plain English). Type 'exit' to quit.\n")

    while True:
        user_input = input("👤 You: ").strip()
         
        if user_input.lower() in ("show all", "list all tools", "all tools", "show tools", "everything" , "show everything", "show all the tools", "what tools do we have"):
            display_tools(tools)
            continue
        if user_input.lower() in ('exit', 'quit'):
            print("👋 Exiting... Stay safe online!")
            break

        input_type = classify_input(user_input)
        if input_type:
            print(f"🧠 Detected input type: {input_type}")
            keywords = suggest_tools(input_type)
        else:
            keyword = detect_intent(user_input)
            if keyword:
                print(f"💡 Detected intent keyword: '{keyword}'")
                keywords = [keyword]
            else:
                keywords = [user_input]

        results = []
        for kw in keywords:
            results.extend(search_by_fuzzy_keyword(tools, kw))

        display_tools(results)

if __name__ == "__main__":
    chatbot()
