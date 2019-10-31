from tkinter import *
from tkinter import filedialog

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
print(PdfToConvert)
