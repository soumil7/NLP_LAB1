# Import necessary libraries
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon (Sentiment Analysis Lexicon)
nltk.download('vader_lexicon')

# Create a SentimentIntensityAnalyzer object
sid = SentimentIntensityAnalyzer()

# Function to perform sentiment analysis
def analyze_sentiment(text):
    # Get the sentiment scores
    sentiment_scores = sid.polarity_scores(text)
    
    # Determine the sentiment based on the compound score
    if sentiment_scores['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Example usage
text_to_analyze = "I love using Python for sentiment analysis. It's amazing!"
sentiment_result = analyze_sentiment(text_to_analyze)

# Print the result
print(f"Sentiment: {sentiment_result}")
