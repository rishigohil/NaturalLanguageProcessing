#to run "pip install tika"
import tika
tika.initVM()
from tika import parser
import nltk.data



def find_paragraphs(text):
    paragraphs_with_fragments = text.split("\n\n")
    return filter(lambda k: '.' in k , paragraphs_with_fragments)

def find_sentences(text):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    return tokenizer.tokenize(text)

parsed_1_column = parser.from_file('SampleLetter1.pdf')
#print(parsed_1_column["metadata"])
#print(parsed_1_column["content"])
paragraphs_1_column = find_paragraphs(parsed_1_column["content"])
for item in paragraphs_1_column:
    print("\n\n Paragraph:" + item)
    for sent in find_sentences(item):
        print('\n Sentence: ' + sent)

parsed_2_column = parser.from_file('2ColumnPaper.pdf')
#print(parsed_2_column["metadata"])
#print(parsed_2_column["content"])
paragraphs_2_column = find_paragraphs(parsed_2_column["content"])

for item in paragraphs_2_column:
    print("\n\n Paragraph: " + item)
    for sent in find_sentences(item):
        print('\n Sentence:' + sent)