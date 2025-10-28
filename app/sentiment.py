from textblob import TextBlob
from typing import Dict


def analyze_sentiment(text: str) -> Dict[str, any]:
    if not text or not text.strip():
        return {
            "label": "neutral",
            "polarity": 0.0,
            "subjectivity": 0.0
        }
    
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    if polarity > 0.1:
        label = "positive"
    elif polarity < -0.1:
        label = "negative"
    else:
        label = "neutral"
    
    return {
        "label": label,
        "polarity": round(polarity, 3),
        "subjectivity": round(subjectivity, 3)
    }
