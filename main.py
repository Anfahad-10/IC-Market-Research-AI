import pandas as pd
from preprocessor import clean_and_tokenize 

from sentiment_engine import get_sentiment, categorize_sentiment


def run_pipeline():
    print("--- InsightCoder Pipeline Started ---")
    
    try:
        df = pd.read_csv('survey_data.csv')
        print(f"Loaded {len(df)} rows of data.")
    except FileNotFoundError:
        print("ERROR: survey_data.csv not found. Did you run create_data.py?")
        return



    print("Cleaning text data...")
    df['Cleaned_Data'] = df['Customer_Feedback'].apply(clean_and_tokenize)


    

    print("Analyzing sentiment...")
    df['Sentiment_Score'] = df['Cleaned_Data'].apply(get_sentiment)

    df['Sentiment_Label'] = df['Sentiment_Score'].apply(categorize_sentiment)

    print("\nSentiment Distribution:")
    print(df['Sentiment_Label'].value_counts())
    



    
    print("\nSample Data:")
    print(df[['Customer_Feedback', 'Cleaned_Data']].head(5))
    

    df.to_csv('processed_data.csv', index=False)
    print("\nPipeline finished. Saved to processed_data.csv")





    #main Run the pipeline

if __name__ == "__main__":
    run_pipeline()