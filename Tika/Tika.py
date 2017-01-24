#to run "pip install tika"
import tika
tika.initVM()
from tika import parser



def find_paragraphs(text):
    paragraphs_with_fragments = text.split("\n\n")
    return filter(lambda k: '.' in k , paragraphs_with_fragments)

parsed_1_column = parser.from_file('SampleLetter1.pdf')
#print(parsed_1_column["metadata"])
#print(parsed_1_column["content"])
paragraphs_1_column = find_paragraphs(parsed_1_column["content"])
for item in paragraphs_1_column:
    print("\n\n" + item)

parsed_2_column = parser.from_file('2ColumnPaper.pdf')
#print(parsed_2_column["metadata"])
#print(parsed_2_column["content"])
paragraphs_2_column = find_paragraphs(parsed_2_column["content"])

for item in paragraphs_2_column:
    print("\n\n" + item)