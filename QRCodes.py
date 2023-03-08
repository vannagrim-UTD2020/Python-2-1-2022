from tkinter import *
from tkinter import messagebox
import pyqrcode
# do the studysession to create the script environment. 
# create the root again. 
ws = Tk()
ws.title("QR CODE GENERATOR")
ws.config(bg='#DFDEDF')


def generate_QR():
    if len(user_input.get()) != 0:
        global qr, img
        qr = pyqrcode.create(user_input.get())
        img = BitmapImage(data=qr.xbm(scale=10))
    else:
        messagebox.showwarning('warning', 'All Fields are Required!')
    try:
        display_code()
    except:
        pass


def display_code():
    img_lbl.config(image=img)
    output.config(
        text="Successfully generated the QR code for: " + user_input.get())


lbl = Label(
    ws,
    text="Enter the Web Address to Generate Unique QR: ",
    bg='#DFDEDF'
)
lbl.pack()

user_input = StringVar()
entry = Entry(
    ws,
    textvariable=user_input
)
entry.pack(padx=20)

button = Button(
    ws,
    text="Generate my QRCode",
    width=25,
    command=generate_QR
)
button.pack(pady=30)

img_lbl = Label(
    ws,
    bg='#DFDEDF')
img_lbl.pack()
output = Label(
    ws,
    text="",
    bg='#DFDEDF'
)
output.pack()

ws.mainloop()
