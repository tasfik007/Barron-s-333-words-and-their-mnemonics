from tabula import read_pdf
from tabulate import tabulate
import csv
from tkinter import *
from tkinter import filedialog
from bs4 import BeautifulSoup
import requests


csv_file = open('Barrons333_words.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Word', 'Meaning', 'Mnemonic1', 'Mnemonic2', 'Mnemonic3'])


root = Tk()
root.title('GRE Word Lists PDF to Excel Sheets')

PdfToConvert = 'null'


def open():
    global PdfToConvert
    root.filename = filedialog.askopenfilename(
        initialdir='C:/Users/Acer/Desktop/GRE words war', title='Select a PDF file')
    PdfToConvert = root.filename
    root.destroy()


btn = Button(root, text='Open a pdf file', width=50, command=open)


btn.pack(side="top", fill='both', expand=True, padx=40, pady=100)
root.mainloop()

df = read_pdf(PdfToConvert,
              pages='all', output_format='json')
words = 0


def getMnemonics(word, meaning, no_of_mnemonics):
    global csv_writer
    total_mn = 0
    md = []
    src = requests.get('https://mnemonicdictionary.com/?word='+word).text
    data = BeautifulSoup(src, 'lxml')
    for mnemonic in data.find_all('div', class_='card mnemonic-card'):
        for content in mnemonic.find_all('div', class_='card-text'):
            md.append(content.text)
        total_mn = total_mn+1
        if(total_mn >= no_of_mnemonics):
            break
    print(word+'     '+meaning+'     '+md[0]+'    '+md[1]+'    '+md[2])
    csv_writer.writerow([word, meaning, md[0].replace(
        '\n', ''),  md[1].replace('\n', ''), md[2].replace('\n', '')])


for pages in df:
    for rows in pages['data']:
        words = words+1
        try:
            getMnemonics(rows[0]['text'], rows[1]['text'], 3)
        except:
            pass

    print()

print(words)
csv_file.close()
