from textblob import TextBlob

def get_sentiment(text):


    if not isinstance(text, str):
        return 0.0

    analysis = TextBlob(text)    
    score = analysis.sentiment.polarity
    
    return score

def categorize_sentiment(score):

    if score > 0.1:
        return "Positive"
    elif score < -0.1:
        return "Negative"
    else:
        return "Neutral"

# --- DEBUGGING BLOCK ---
if __name__ == "__main__":
    test_reviews = [
        "I LOVE this product, it works perfectly!", 
        "This is the worst garbage I ever bought.",
        "The case is blue." 
    ]
    
    print("--- Testing Sentiment Engine ---")
    for review in test_reviews:
        s_score = get_sentiment(review)
        label = categorize_sentiment(s_score)
        print(f"Review: '{review}'\nScore: {s_score} -> Label: {label}\n")