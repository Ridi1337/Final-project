from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import Image


root=Tk()
root.geometry("400x400")
root.title("Alatoo capybara's file converter")


def jpg_to_png():
    filename=fd.askopenfilename()
    if filename.endswith(".jpg"):
        Image.open(filename).save("flopp.png")
    else:
        Label_2=Label(root,text="Error, something went wrong...", width=30,fg="blue", font=("bold",15))
        Label_2.place(x=50,y=280)

def jpg_to_pdf():
    filename=fd.askopenfilename()
    if filename.endswith(".jpg"):
        Image.open(filename).save("sample1.pdf", resolution=100.0)
    else:
        Label_2=Label(root,text="Error, something went wrong...", width=20,fg="blue", font=("bold",15))
        Label_2.place(x=50,y=280)

Label_1=Label(root,text="Browse A File", width=20, font=("bold",15))
Label_1.place(x=80,y=80)

Label_3=Label(root, text="copyright(c)2022, Alatoo International University. All rights reserved.", width=0, font=("bold",8))
Label_3.place(x=65,y=383)

root.iconbitmap('D:\python img/logo.ico')













Button(root,text="JPG to PNG", width=20, height=2, bg="brown",fg="white",command=jpg_to_png).place(x=120,y=120)
Button(root,text="JPG to PDF", width=20, height=2, bg="brown",fg="white", command=jpg_to_pdf).place(x=120,y=220)

root.mainloop()