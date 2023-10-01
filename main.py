from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

l = random.randint(4, 8)
s = random.randint(2, 4)
n = random.randint(2, 4)


def generate():
    EPP.delete(0, END)
    uwu_l = [random.choice(letters) for _ in range(l)]
    uwu_s = [random.choice(symbols) for _ in range(s)]
    uwu_n = [random.choice(numbers) for _ in range(n)]

    password_list = uwu_l + uwu_n + uwu_s

    random.shuffle(password_list)

    psw = "".join(password_list)
    EPP.insert(0, psw)
    pyperclip.copy(psw)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = EWW.get()
    new_data = {
        website: {
            'email': EEM.get(),
            'password': EPP.get(),
        }
    }

    if len(EWW.get()) == 0 or len(EEM.get()) == 0 or len(EPP.get()) == 0:
        messagebox.showwarning(title='Ooooooopsss',
                               message='You left one of the fields empty!\nDO NOT DO THAT AGAIN!')
        is_okay = False
    else:
        is_okay = messagebox.askokcancel(title=EWW.get(), message=f'Are you sure about the information?'
                                                                  f'\nEmail: {EEM.get()}\nPassword:{EPP.get()}')


    # JSON FUNC //////////////////////


    if is_okay:
        try:
            with open('passwords.json', mode='r') as data:

                # Reading old data
                dat = json.load(data)
                # Updating old data with new shit
                dat.update(new_data)
            with open('passwords.json', 'w') as data:
                # Saving updated data
                json.dump(dat, data, indent=4)

                EWW.delete(0, 'end')
                EPP.delete(0, 'end')
        except FileNotFoundError:
            with open('passwords.json', mode='w') as data:
                json.dump(new_data, data, indent=4)
                EWW.delete(0, 'end')
                EPP.delete(0, 'end')


def search():
    try:
        with open("passwords.json") as data:
            patt = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No data_file found, you stupid bitch')
    else:
        if EWW.get() in patt:
            newe = patt[EWW.get()]['email']
            newp = patt[EWW.get()]['password']
            messagebox.showinfo(title=EWW.get(), message=f'Email: {newe}\nPassword: {newp}')
        else:
            messagebox.showinfo(title='Error', message='No such website found, you stupid bitch')


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Keeper')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

label_website = Label(text='Website:')
label_website.grid(column=0, row=1, padx=10, pady=10)

EWW = entry_website = Entry(width=35)
EWW.focus()
EWW.grid(column=1, row=1, columnspan=2, padx=0, pady=10)

label_email = Label(text='Email / Username:')
label_email.grid(column=0, row=2, padx=10, pady=10)

EEM = entry_email = Entry(width=35)
EEM.insert(0, 'riptmy@gmail.com')
EEM.grid(column=1, row=2, columnspan=2, padx=10, pady=10)

label_pass = Label(text='Password:')
label_pass.grid(column=0, row=3, padx=10, pady=10)

EPP = entry_pass = Entry(width=16)
EPP.grid(column=1, row=3, padx=0, pady=10)

button_gen = Button(text='Generate Password', command=generate)
button_gen.grid(column=2, row=3, padx=10, pady=10)

button_add = Button(text='Add', width=35, command=save)
button_add.grid(column=1, row=4, columnspan=2, padx=10, pady=10)

button_search = Button(text='Search', command=search)
button_search.grid(column=3, row=1, padx=0, pady=10)

window.mainloop()
