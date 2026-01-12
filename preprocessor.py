import re 


STOPWORDS = set(['the', 'is', 'at', 'which', 'on', 'a', 'an', 'and', 'or', 'to', 'for', 'of'])

def clean_and_tokenize(text):

    
    if not isinstance(text, str):
        return ""

    text = text.lower()
    
    text = re.sub(r'[^\w\s]', '', text)
    
    words = text.split()
    
    meaningful_words = [w for w in words if w not in STOPWORDS]
    
    return " ".join(meaningful_words)

if __name__ == "__main__":
    test_phrase = "The Battery life is AMAZING!!!"
    print(f"Original: {test_phrase}")
    print(f"Cleaned:  {clean_and_tokenize(test_phrase)}")