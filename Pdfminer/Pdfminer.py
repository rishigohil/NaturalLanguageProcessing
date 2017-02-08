#to run "pip install pdfminer"
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.pdfdocument import PDFDocument, PDFNoOutlines
from pdfminer.layout import LTPage, LTChar, LTAnno, LAParams, LTTextBox, LTTextLine
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import HTMLConverter
from pdfminer.pdfparser import PDFParser
from bs4 import BeautifulSoup
from cStringIO import StringIO
import nltk.data
import os
import re
PDF_DIR = "pdfs/"

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    #laparams = LAParams()
    laparams = LAParams(char_margin=3.5, all_texts=True)
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

def convert_pdf_to_html(path):
    rsrcmgr = PDFResourceManager()
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    #laparams = LAParams()
    laparams = LAParams(char_margin=3.5, all_texts=True)
    device = HTMLConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0  # is for all
    caching = True
    pagenos = set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str

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

def find_sections(text):
    planSections = list()
    soup = BeautifulSoup(text, "html.parser")
    sections = soup.findAll('span',text=re.compile("[A-Z]+:"))
    for section in sections:
        try:
            heading = str(section.findAll(text=True))
            sectionText = section.next_sibling.findAll(text=True)
            if str(sectionText) <> "":
                aTempDict = {}
                aTempDict[heading] = sectionText
                planSections.append(aTempDict)

            print("Section** : " + str(section))
        except:
           print "no sibling"
    return planSections

contracts = list()

for filename in os.listdir(PDF_DIR):
    if filename.endswith(".pdf"):
        pdfHtml_2_column = convert_pdf_to_html(os.path.join(PDF_DIR, filename))
        planCoverage = find_sections(pdfHtml_2_column)
        print("Coverage Read")
        aTempDict = {}
        aTempDict[filename] = planCoverage
        contracts.append(aTempDict)

        continue
    else:
        continue



print("EOP")