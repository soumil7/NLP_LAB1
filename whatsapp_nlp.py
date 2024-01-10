import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Download NLTK resources (if not already downloaded)
nltk.download('vader_lexicon')

# Function to analyze sentiment and plot results
def analyze_sentiments(sentences):
    sid = SentimentIntensityAnalyzer()

    # Analyze sentiment for each sentence
    sentiment_scores = [sid.polarity_scores(sentence)['compound'] for sentence in sentences]
    print(sentiment_scores)
    # Plot sentiment scores
    plt.plot(sentiment_scores, marker='o', linestyle='-', color='b')
    plt.xlabel('Sentence')
    plt.ylabel('Sentiment Score')
    plt.title('Sentiment Analysis of WhatsApp Chat')
    plt.show()

# Example usage
whatsapp_chat = """Hello! How are you?
I'm doing great, thanks!
That's awesome to hear.
Can't wait for the weekend!
Me neither! It's going to be fun."""

# Split the chat into sentences (assuming each line is a sentence)
whatsapp_sentences = whatsapp_chat.split('\n')

# Analyze and plot sentiment scores
analyze_sentiments(whatsapp_sentences)
