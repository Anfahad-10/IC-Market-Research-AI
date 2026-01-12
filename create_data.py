import pandas as pd
import random

# 1. Define the "Building Blocks" of our reviews.
# We want a mix of topics (Battery, Screen, App) and sentiments (Good, Bad).
topics = {
    "battery": [
        "battery life is amazing", 
        "battery drains too fast", 
        "charges very slowly", 
        "lasts all day long"
    ],
    "screen": [
        "screen is blurry", 
        "display is crisp and bright", 
        "touchscreen is unresponsive", 
        "colors are vivid"
    ],
    "app": [
        "app crashes constantly", 
        "user interface is intuitive", 
        "cannot sync with my phone", 
        "app features are helpful"
    ],
    "price": [
        "too expensive for the features",
        "great value for money",
        "overpriced",
        "affordable and good quality"
    ]
}

# 2. Generate 500 fake reviews
data = []

print("Generating synthetic market research data...")

for i in range(500):
    # Randomly pick a category (e.g., "battery")
    category = random.choice(list(topics.keys()))
    # Randomly pick a specific feedback text
    text = random.choice(topics[category])
    
    # We add some "Noise" (random punctuation/case) to make it realistic
    # Real users don't type perfectly.
    if random.random() > 0.5:
        text = text.upper() # User shouting
    if random.random() > 0.7:
        text = text + "!!!" # User excited/angry
        
    data.append({
        "Review_ID": i + 1,
        "Customer_Feedback": text,
        "Category": category # We keep this for checking our accuracy later
    })

# 3. Save to CSV
df = pd.DataFrame(data)
df.to_csv('survey_data.csv', index=False)

print(f"Success! Created 'survey_data.csv' with {len(df)} rows.")
print(df.head())