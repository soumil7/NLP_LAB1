import nltk
#download the Punkt tokenizer 
nltk.download('punkt')
from nltk.tokenize import word_tokenize
sample_text = "this is a text ready to tokenize"
tokens = word_tokenize(sample_text)
print(tokens)

from nltk.tokenize import TweetTokenizer
tweet_tokenizer = TweetTokenizer()
sample_text = "This is a tweet @jack #NLP"
tokens = tweet_tokenizer.tokenize(sample_text)
print(tokens)

from nltk.tokenize import sent_tokenize
sample_text = "This is a sentence. This is another one!\nAnd this is the last one."
sentences = sent_tokenize(sample_text)
print(sentences)

import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")

stopwords_ = set(stopwords.words("english"))
sample_text = "this is a sample text"
tokens = sample_text.split()
clean_tokens = [t for t in tokens if not t in stopwords_]
clean_text = " ".join(clean_tokens)
print(sample_text, clean_text)