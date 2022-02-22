#importing Libraries

from tkinter import *
from tkinter.ttk import *
import pyperclip
import random
import string

#initialize window
root =Tk()
root.geometry("400x300")
root.resizable(10,10)
root.title("axhaar - PASSWORD GENERATOR")
var = IntVar()
var1 = IntVar()

#heading
Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
Label(root, text ='axhaar ©', font ='arial 11').pack(side = BOTTOM)

#password length
pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 16).pack()

#define function
pass_str = StringVar()
def Generator():
    password = ''
    if var.get() == 1:
        for x in range (0,4):
            password = random.choice(string.ascii_lowercase)
        for y in range(pass_len.get()- 1):
            password = password + random.choice(string.ascii_lowercase + string.digits)

    elif var.get() == 0:
        for x in range (0,4):
            password = random.choice(string.ascii_uppercase) + random.choice(string.digits)
        for y in range(pass_len.get()- 2):
            password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) 

    elif var.get() == 3:
        for x in range (0,4):
            password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
        for y in range(pass_len.get()- 4):
            password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) 

    pass_str.set(password)

#radiobuttons for password strength
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.pack(anchor=CENTER)
#value=0 means the default will be fixed to "Medium"
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.pack(anchor=CENTER)
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.pack(anchor=CENTER)
combo = Combobox(root, textvariable=var1)

#button "GENERATE PASSWORD"
Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

Entry(root , textvariable = pass_str).pack()

#function to copy password to clipboard
def Copy_password():
    pyperclip.copy(pass_str.get())
Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)

#loop to run program
root.mainloop()
