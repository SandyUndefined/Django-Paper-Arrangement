import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from fpdf import FPDF
import json

title = ''
logo_data = ''
json_data = ''
text_file = []


def values(json_file, txt_file, logo, header):
    json_data = json_file
    for i in txt_file:
        text_file.append(i)
    logo_data = logo
    title = header
    filenames = print_data(json_data)
    data(filenames,logo_data, title)


def print_data(json_data):
    # Json to Dict
    with open(os.path.join(settings.MEDIA_ROOT, json_data), 'r',encoding="utf8") as jf:
        data_dict = json.load(jf)

    # Sorting Dict and Saving them in List
    sorted_values = dict(sorted(data_dict.items(), key=lambda item: item[1]))
    filenames = []
    for i in sorted_values:
        filenames.append(f'{i}.txt')
    return filenames


# Convert text file into pdf

class PDF(FPDF):
    def __init__(self,logo_name,header):
        super(PDF,self).__init__()
        self.logo = logo_name
        self.title = header

    def header(self):
        self.image(os.path.join(settings.MEDIA_ROOT, self.logo), x=14, y=4, h=18, w=18)
        self.set_font('Arial', 'B', 21)
        self.set_text_color(r=5, g=57, b=107)
        self.text(62, 15, self.title)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def section(self, name):
        self.set_top_margin(25)
        self.set_font('Arial', 'B', 16)
        self.cell(0, 6, name[:-4], 0, 0, 'C', 0)
        self.ln(4)

    def question(self, name):
        with open(os.path.join(settings.MEDIA_ROOT, name), 'r') as fh:
            txt = fh.read()
        self.set_font("Arial", '', size=12)
        self.multi_cell(0, 6, txt)
        self.ln()

    def print_paper(self, name):
        self.add_page()
        self.section(name)
        self.question(name)


def data(filenames,logo,title):
    pdf = PDF(logo,title)
    pdf.set_margins(left=15, top=25, right=15)
    for x in filenames:
        pdf.print_paper(x)
    pdf.output("paper.pdf")
