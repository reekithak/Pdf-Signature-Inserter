import os
import time
import argparse
import tempfile
import PyPDF2
import datetime
from reportlab.pdfgen import canvas
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
import time

def clean_all():
    try:
        os.remove(r"Others\b_f1.pdf")
        os.remove(r"Others\b_f2.pdf")
        os.remove(r"Others/b_f3.pdf")
    except:
        pass

    try:

        os.remove(r"Others\b1.pdf")
        os.remove(r"Others\b2.pdf")
        os.remove(r"Others\b3.pdf")
        os.remove(r"Others\b4.pdf")
    except:
        pass
    
    try:
        os.rename(r"Others\b_f4.pdf",r"Signed_Form\signed_form.pdf")
    except:
        pass
clean_all()


def pass_pdf(pdf_fh,args,image,name,f_name):
    sig_tmp_fh = None
    pdf = PyPDF2.PdfFileReader(pdf_fh)
    writer = PyPDF2.PdfFileWriter()
    sig_tmp_filename = None
    page_num, x1, y1, width, height = [int(a) for a in args.split("x")]
    page_num = [int(x) for x in str(page_num)]
    k = 0
    for i in range(0, pdf.getNumPages()):
        page = pdf.getPage(i)
        #print(page)
        if i in page_num:
            k = 1
            #print("True")
            sig_tmp_filename = name
            c = canvas.Canvas(sig_tmp_filename, pagesize=page.cropBox)
            c.drawImage(image, x1, y1, width, height, mask='auto')
            c.showPage()
            c.save()
            #print("Done-1")
            sig_tmp_fh = open(sig_tmp_filename, 'rb')
            sig_tmp_pdf = PyPDF2.PdfFileReader(sig_tmp_fh)
            #print("Done-2")
            sig_page = sig_tmp_pdf.getPage(0)
            sig_page.mediaBox = page.mediaBox
            page.mergePage(sig_page)
            print("Finish")
            
        writer.addPage(page)
        if(k==1):
            #print("added page")
            k=0
    with open(f_name, 'wb') as fh:
            writer.write(fh)            



#Reading images
b_im = ImageReader(r"Signatures\buyer_sign.png")
s_im = ImageReader(r"Signatures\seller_sign.png")

def run_signature():
    #Buyer
    #1st
    pdf_fh = open(r"forms\forms.pdf", 'rb')
    args = "7x125x220x100x40"
    pass_pdf(pdf_fh,args,b_im,r"Others\b1.pdf",r"Others\b_f1.pdf")   
    #2nd
    pdf_fh = open(r"Others\b_f1.pdf", 'rb')
    args = "7x125x150x100x40"
    pass_pdf(pdf_fh,args,b_im,r"Others\b2.pdf",r"Others\b_f2.pdf")
    
    #seller
    #1st
    pdf_fh = open(r"Others\b_f2.pdf", 'rb')
    args = "7x340x220x100x40"
    pass_pdf(pdf_fh,args,s_im,r"Others\b3.pdf",r"Others\b_f3.pdf")   
    #2nd
    pdf_fh = open(r"Others\b_f3.pdf", 'rb')
    args = "7x340x150x100x40"
    pass_pdf(pdf_fh,args,s_im,r"Others\b4.pdf",r"Others\b_f4.pdf")
    clean_all()
    print("File saved as signed_form.pdf in Signed_Form Directory :) ")


run_signature()
clean_all()