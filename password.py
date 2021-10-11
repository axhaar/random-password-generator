#importing Libraries

from tkinter import *
import pyperclip
import random
import string

#initialize window
root =Tk()
root.geometry("400x200")
root.resizable(10,10)
root.title("axhaar - PASSWORD GENERATOR")

#heading
Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
Label(root, text ='axhaar ©', font ='arial 15 bold').pack(side = BOTTOM)

#password length
pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()

#define function
pass_str = StringVar()
def Generator():
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

#button "GENERATE PASSWORD"
Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

Entry(root , textvariable = pass_str).pack()

#function to copy password to clipboard
def Copy_password():
    pyperclip.copy(pass_str.get())
Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)

#loop to run program
root.mainloop()