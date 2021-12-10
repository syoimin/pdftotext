from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def pdf2txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    laparams.detect_vertical = True
    device = TextConverter(rsrcmgr, retstr, codec='utf-8', laparams=laparams)
    with open(path, 'rb') as file:
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        pagenos=set()
        for page in PDFPage.get_pages(file, pagenos, check_extractable=True):
        # for page in range(5):
            interpreter.process_page(page)

    text = retstr.getvalue()
    device.close()
    retstr.close()
    return text

text = pdf2txt('sap.pdf')
print(text)