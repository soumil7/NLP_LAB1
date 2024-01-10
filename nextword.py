import nltk
from nltk import bigrams, trigrams
from nltk.corpus import reuters
from nltk.probability import FreqDist, ConditionalFreqDist

# Download the "reuters" corpus if not already downloaded
nltk.download('reuters')

# Get the words from the reuters corpus
corpus_words = reuters.words()

# Create trigrams
trigram_model = list(trigrams(corpus_words))

# Build conditional frequency distribution
cfd = ConditionalFreqDist(((bigram[0], bigram[1]), word) for bigram, word in zip(trigram_model, corpus_words[2:]))

def predict_next_word(word1, word2):
    # Predict the next word based on the trigram model
    predictions = cfd[word1][word2]
    if predictions:
        # Use max with a custom key function to get the word with maximum probability
        print(predictions)
        return max(predictions, key=lambda x: predictions[x])
    else:
        return "No prediction available."

# Example usage
word1 = "the"
word2 = "price"
predicted_word = predict_next_word(word1, word2)

print(f"Predicted next word after '{word1} {word2}': {predicted_word}")
