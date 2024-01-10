# Install SpaCy and download the Spanish model
# pip install spacy
# python -m spacy download es_core_news_sm

import spacy

# Load the Spanish language model
nlp = spacy.load('es_core_news_sm')

# Example text in Spanish
text = "El procesamiento del lenguaje natural es fascinante."

# Process the text using SpaCy
doc = nlp(text)

# Print named entities
print("Named Entities:")
for ent in doc.ents:
    print(ent.text, "-", ent.label_)

# Print part-of-speech tags
print("\nPart-of-Speech Tags:")
for token in doc:
    print(token.text, "-", token.pos_)
