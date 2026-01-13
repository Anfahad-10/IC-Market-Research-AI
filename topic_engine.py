from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def discover_topics(text_list, num_topics=4):



    print("Vectorizing text data...")
    vectorizer = TfidfVectorizer(max_features=1000) 
    text_matrix = vectorizer.fit_transform(text_list)
    
    print(f"Clustering into {num_topics} topics...")
    model = KMeans(n_clusters=num_topics, random_state=42)
    model.fit(text_matrix)
    
    assigned_clusters = model.labels_
    


    feature_names = vectorizer.get_feature_names_out()
    ordered_centroids = model.cluster_centers_.argsort()[:, ::-1]
    
    topic_keywords = {}
    
    for i in range(num_topics):
        top_words = [feature_names[ind] for ind in ordered_centroids[i, :4]] # Get top 4 words
        keywords_str = ", ".join(top_words)
        topic_keywords[i] = keywords_str
        


    return assigned_clusters, topic_keywords