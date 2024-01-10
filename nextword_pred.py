import random

def train_model(text):
    words = text.split()
    model = {}

    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]

        if current_word in model:
            model[current_word].append(next_word)
        else:
            model[current_word] = [next_word]

    return model

def generate_next_word(model, seed_word):
    possible_next_words = model.get(seed_word, [])
    return random.choice(possible_next_words) if possible_next_words else None

# Example usage
text_corpus = "This is a simple example for next word prediction using a basic model in Python."

# Train the model
word_model = train_model(text_corpus)

# User input
seed_word = input("Enter a word or sentence: ").split()[-1]

# Generate next word
next_word = generate_next_word(word_model, seed_word)

# Display prediction
if next_word:
    print(f"Predicted next word: {next_word}")
else:
    print("No prediction available for the given word.")
