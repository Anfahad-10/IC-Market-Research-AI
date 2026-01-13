import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: API Key not found.")
else:
    client = genai.Client(api_key=api_key)
    print("\n--- Raw Model List ---")
    
    try:


        for m in client.models.list():
            print(f"ID: {m.name}")
            
    except Exception as e:
        print(f"Error: {e}")