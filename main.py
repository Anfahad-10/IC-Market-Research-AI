import pandas as pd
from preprocessor import clean_and_tokenize
from sentiment_engine import get_sentiment, categorize_sentiment
from topic_engine import discover_topics
from genai_labeler import get_topic_label 



def run_pipeline():
    print("\n=== InsightCoder AI Pipeline Started ===")
    


    try:
        df = pd.read_csv('survey_data.csv')
        print(f"Loaded {len(df)} rows.")
    except FileNotFoundError:
        print("Error: Data not found.")
        return



    print("Step 1: Cleaning text...")
    df['Cleaned_Data'] = df['Customer_Feedback'].apply(clean_and_tokenize)
    
    print("Step 2: Analyzing Sentiment...")
    df['Sentiment_Score'] = df['Cleaned_Data'].apply(get_sentiment)
    df['Sentiment_Label'] = df['Sentiment_Score'].apply(categorize_sentiment)
    

    print("Step 3: Discovering Topics (Clustering)...")
    cluster_ids, topic_keywords_dict = discover_topics(df['Cleaned_Data'], num_topics=4)
    df['Topic_Cluster_ID'] = cluster_ids
    
    print("Step 4: Sending Topics to GenAI for Naming...")
    


    cluster_name_map = {}
    
    for cluster_id, keywords in topic_keywords_dict.items():
        print(f"   -> Naming Cluster {cluster_id} (Keywords: {keywords})...")
        human_label = get_topic_label(keywords)
        print(f"      AI Name: {human_label}")
        cluster_name_map[cluster_id] = human_label
        
    df['Topic_Category'] = df['Topic_Cluster_ID'].map(cluster_name_map)
    



    output_file = 'final_market_report.csv'
    df.to_csv(output_file, index=False)
    
    print(f"\nSUCCESS! Processed data saved to {output_file}")
    print("Preview of Final Data:")
    print(df[['Customer_Feedback', 'Sentiment_Label', 'Topic_Category']].head(10))

if __name__ == "__main__":
    run_pipeline()