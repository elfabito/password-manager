from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
 # ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


password_letters = [ random.choice(letters) for char in range(nr_letters)]
password_symbols = [ random.choice(symbols) for symbol in range(nr_symbols)]
password_numbers = [ random.choice(numbers) for num in range(nr_numbers)]

password_list = password_letters + password_symbols + password_numbers
# for char in range(nr_letters):
#   password_list.append(random.choice(letters))
#
# for char in range(nr_symbols):
#   password_list += random.choice(symbols)
#
# for char in range(nr_numbers):
#   password_list += random.choice(numbers)


def generate():
    input_pass.delete(0, END)
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    input_pass.insert(string=password, index=0)

# ---------------------------- SAVE PASSWORD ------------------------------- #




def search():
    web = input_web.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file Found.")
    else:

        if web in data:
            em = data[web]['email']
            ps = data[web]['password']
            messagebox.showinfo(title=f"{input_web.get()}", message=f"Email:  {em} \nPassword:  {ps}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {web} exists.")


def add():
    web = input_web.get()
    email = input_email.get()
    pas = input_pass.get()
    new_data = {
        web: {
            "email": email,
            "password": pas,
        }
    }

    if len(web) == 0 or len(pas) == 0:
        messagebox.showinfo(title="oops", message="Please don't leave blank")

    else:
        try:
            with open("data.json","r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            new_data.update(data)
            with open("data.json", "w") as file:
                json.dump(new_data, file,indent=4)
        finally:
            input_web.delete(0, END)
            input_pass.delete(0, END)
            input_web.focus()




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(pady=20, padx=20)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1,row=0)


web = Label(text='Website: ')
web.grid(column=0, row=2)

input_web = Entry(width=33)
input_web.grid(row=2,column=1,columnspan=1)
input_web.focus()

email = Label(text='Email/Username: ')
email.grid(column=0,row=3)

input_email = Entry(width=52)
input_email.grid(column=1, row=3,columnspan=2)
input_email.insert(0, 'youremail@email.com')

gen_pass = Label(text='Password: ')
gen_pass.grid(column=0,row=4)

input_pass = Entry(width=33)
input_pass.grid(column=1,row=4)

gen_pass_button = Button(text="Generate Password", command=generate)
gen_pass_button.grid(column=2,row=4)

add = Button(text='Add', command=add, width=44)
add.grid(column=1, row=5, columnspan=2)

search = Button(text="Search", command=search, width= 15)
search.grid(column=2,row=2)



window.mainloop()