#to run "pip install tika"
import tika
tika.initVM()
from tika import parser
import nltk.data
from bs4 import BeautifulSoup
from cStringIO import StringIO
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def find_paragraphs(text):
    paragraphs_with_fragments = text.split("\n\n")
    return filter(lambda k: '.' in k , paragraphs_with_fragments)

def find_paragraphs(text):
    paragraphs_with_fragments = text.split("\n\n")
    return filter(lambda k: '.' in k , paragraphs_with_fragments)

def find_sentences(text):
    try:
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        return tokenizer.tokenize(text)
    except:
        return ""

def find_headings(text):
    soup = BeautifulSoup(text, "html.parser")
    headings = soup.find('span', style=lambda value: value and 'font-size:15px' in value or 'font-size:15px' in value)
    for heading in headings:
        print("Heading: "+ str(heading))


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

pdfHtml_1_column = parser.from_file('SampleLetter1.pdf',xmlContent=True)
text_file = open("pdf_html_1_column.txt", "w")
text_file.write(str(pdfHtml_1_column["content"]))
text_file.close()

pdfHtml_2_column = parser.from_file('2ColumnPaper.pdf',xmlContent=True)
#find_headings(pdfHtml_2_column)
for item in paragraphs_2_column:
    print("\n\nParagraph: " + item)
    for sent in find_sentences(item):
        print('\nSentence ' + sent)

text_file = open("pdf_html_2_column.txt", "w")
text_file.write(str(pdfHtml_2_column["content"]))
text_file.close()


