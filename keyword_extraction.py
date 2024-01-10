# Import necessary libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

# Function to perform keyword extraction
def extract_keywords(text, num_keywords=5):
    # Tokenize the text into words
    words = word_tokenize(text.lower())  # Convert to lowercase for consistency

    # Remove stop words (common words that usually don't carry much meaning)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    print(filtered_words)
    # Calculate word frequencies
    freq_dist = FreqDist(filtered_words)
    print(freq_dist)
    # Get the most common words as keywords
    keywords = freq_dist.most_common(num_keywords)

    return [word for word, _ in keywords]

# Example usage
text_to_analyze = "Natural language processing is a field of study in artificial intelligence. " \
                  "It focuses on the interaction between computers and humans using natural language."

keywords = extract_keywords(text_to_analyze, num_keywords=5)

# Print the result
print("Keywords:", keywords)
