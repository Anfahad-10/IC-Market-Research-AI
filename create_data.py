import pandas as pd
import random

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

data = []

print("Generating synthetic market research data...")

for i in range(500):
    category = random.choice(list(topics.keys()))
    text = random.choice(topics[category])
    
    if random.random() > 0.5:
        text = text.upper()
    if random.random() > 0.7:
        text = text + "!!!" 
        
    data.append({
        "Review_ID": i + 1,
        "Customer_Feedback": text,
        "Category": category
    })


df = pd.DataFrame(data)
df.to_csv('survey_data.csv', index=False)

print(f"Success! Created 'survey_data.csv' with {len(df)} rows.")
print(df.head())