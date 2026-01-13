import os
from google import genai 
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")




if not api_key:
    print("WARNING: No API Key found.")
    client = None
else:
    client = genai.Client(api_key=api_key)



def get_topic_label(keywords):
    if not client:
        return "AI_Disabled"

    prompt = f"""
    You are a Market Research Analyst.
    I have a cluster of customer reviews described by these keywords: '{keywords}'.
    
    Give me a short, professional label (2-4 words) for this topic.
    Do not explain. Just give the label.
    Example Input: 'screen, crack, broken' -> Example Output: Display Quality
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-flash-latest', 
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"GenAI Error: {e}")
        return "Unknown_Topic"




if __name__ == "__main__":
    test_keywords = "slow, lag, crash, freeze"
    print("Asking Gemini (v2.0 Flash) to name this topic...")
    label = get_topic_label(test_keywords)
    print(f"Keywords: {test_keywords}")
    print(f"AI Label: {label}")