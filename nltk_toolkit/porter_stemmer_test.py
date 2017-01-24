from nltk.stem.porter import *
from nltk import word_tokenize

ps = PorterStemmer()

sample_words = ['Beauty', 'Beautiful', 'Beautifully']

for w in sample_words:
    print(ps.stem(w))


sentence = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once"

words = word_tokenize(sentence)
for w in words:
    print(ps.stem(w))
