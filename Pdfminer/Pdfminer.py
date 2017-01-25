#to run "pip install pdfminer"
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import nltk.data

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

def find_paragraphs(text):
    paragraphs_with_fragments = text.split("\n\n")
    return filter(lambda k: '.' in k , paragraphs_with_fragments)

def find_sentences(text):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    return tokenizer.tokenize(text)

pdfText_1_column = convert_pdf_to_txt("SampleLetter1.pdf")
paragraphs_1_column = find_paragraphs(pdfText_1_column)
for item in paragraphs_1_column:
    print("\n\nParagraph: " + item)
    for sent in find_sentences(item):
        print('\nSentence: ' + sent)

pdfText_2_column = convert_pdf_to_txt("2ColumnPaper.pdf")
paragraphs_2_column = find_paragraphs(pdfText_2_column)

for item in paragraphs_2_column:
    print("\n\n" + item)
    for sent in find_sentences(item):
        print('\nSentence ' + sent)

print("EOP")