from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

sentence = "at eight o'clock on thursday morning Mr. Arthur didn't feel very good. It seems that he had caught a cold"

print(word_tokenize(sentence))

for i in word_tokenize(sentence):
    print(i)

print(sent_tokenize(sentence))
words = word_tokenize(sentence)
filtered_sentence = []
stop_words = set(stopwords.words('english'))
for w in words:
        if w not in stop_words:
                filtered_sentence.append(w)


print(filtered_sentence)

syns = wordnet.synsets("program")
print(syns)
