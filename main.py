from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate():
    entryPass.delete(0, END)
    passwordLetters = [choice(letters) for index in range(randint(8, 10))]
    passwordNumbers = [choice(numbers) for index in range(randint(2, 4))]
    passwordSymbols = [choice(symbols) for index in range(randint(2, 4))]

    passwordList = passwordLetters + passwordNumbers + passwordSymbols
    shuffle(passwordList)
    passFinal = ''.join(passwordList)
    entryPass.insert(0, passFinal)
    pyperclip.copy(passFinal)


def saveInfo():
    web = entryWeb.get().lower()
    email = entryEmail.get()
    password = entryPass.get()
    newData = {
        web: {
            "email": email,
            "password": password
        }
    }

    if len(web) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showinfo("Oops", "Please don't leave any fields empty!")
    else:
        saveIt = messagebox.askokcancel(web, "Are you sure to save?")
        if saveIt:
            try:
                with open("data.json", "r") as fileWrite:
                    # Read Data
                    data = json.load(fileWrite)
                    # Update
                    data.update(newData)
            except FileNotFoundError:
                with open("data.json", "w") as fileWrite:
                    # Read Data
                    json.dump(newData, fileWrite, indent=4)
            else:
                with open("data.json", "w") as fileWrite:
                    # Save
                    json.dump(data, fileWrite, indent=4)
            entryWeb.delete(0, END)
            entryPass.delete(0, END)


def search():
    web = entryWeb.get().lower()
    try:
        with open("data.json", "r") as fileWrite:
            dataRead = json.load(fileWrite)
    except FileNotFoundError:
        messagebox.showinfo("Oops", "No data yet")
    else:
        if web in dataRead:
            webCari = web
            emailCari = dataRead[web]["email"]
            passwordCari = dataRead[web]["password"]
            messagebox.showinfo(webCari, f"email : {emailCari}\n password: {passwordCari}")
        else:
            messagebox.showinfo("Oops", f"No details for the website exists!")


# Screen
screen = Tk()
screen.title("Password Manager")
screen.config(padx=50, pady=50, bg="White")

# Image
canvas = Canvas(width=200, height=200, bg="White", highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

labelWeb = Label(text="Website:", bg="White")
labelWeb.grid(column=0, row=1)

entryWeb = Entry(width=21)
entryWeb.focus()
entryWeb.grid(column=1, row=1)

buttonGenerate = Button(text="Search", command=search, width=14)
buttonGenerate.grid(column=2, row=1)

labelEmail = Label(text="Email/Username:", bg="White")
labelEmail.grid(column=0, row=2)

entryEmail = Entry(width=38)
entryEmail.insert(0, "mamang@gmail.com")
entryEmail.grid(column=1, row=2, columnspan=2)

labelPass = Label(text="Password:", bg="White")
labelPass.grid(column=0, row=3)

entryPass = Entry(width=21)
entryPass.grid(column=1, row=3)

buttonGenerate = Button(text="Generate", command=generate, width=14)
buttonGenerate.grid(column=2, row=3)

buttonAdd = Button(text="Add", width=36, command=saveInfo)
buttonAdd.grid(column=1, row=4, columnspan=2)

screen.mainloop()
