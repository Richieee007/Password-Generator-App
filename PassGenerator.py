from tkinter import *
import string
import random
import pyperclip

def generator():

    # Clear the current password field
    passwordField.delete(0, END)

    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all = small_alphabets+capital_alphabets+numbers+special_characters
    password_length = int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets, password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets, password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all, password_length))

    # password = random.sample(all, password_length)
    # passwordField.insert(0,password)

def copy():
    random_password = passwordField.get()
    pyperclip.copy(random_password)


root = Tk()
root.config(bg="MediumOrchid1")
choice = IntVar()
Font = ("arial", 13, "bold")

passwordLabel = Label(root, text = "Password Generator", font = ("times New Roman", 20, "bold"), bg = "MediumOrchid1", fg = "white")
passwordLabel.grid(pady=10)
weakButton = Radiobutton(root, text = "Weak", value = 1, variable = choice,  font = Font)
weakButton.grid(pady=8)

MedButton = Radiobutton(root, text = "Medium", value = 2, variable = choice, font = Font)
MedButton.grid(pady=8)

StrButton = Radiobutton(root, text = "Strong", value = 3, variable = choice, font = Font)
StrButton.grid(pady=8)

lengthLabel = Label(root, text = "Password Length", font = ("times New Roman", 16, "bold"), bg = "MediumOrchid1", fg = "white")
lengthLabel.grid()

length_Box=Spinbox(root, from_=6,to_=18, width=5, font=Font)
length_Box.grid()

generateButton = Button(root, text="Generate", font=Font, command=generator)
generateButton.grid(pady=8)

passwordField = Entry(root, width=25, bd=2, font=Font)
passwordField.grid(pady=8)

CopyButton = Button(root, text="Copy", font=Font, command=copy)
CopyButton.grid(pady=8)


root.mainloop()