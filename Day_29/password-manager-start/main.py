from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- CONSTANST --------------------------------#
WHITE = "#FFFFFF"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_symbols = [choice(symbols) for _ in range(randint(8, 10))]
    password_letter = [choice(letters) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_number + password_letter + password_symbols

    shuffle(password_list)

    password = ''.join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == '' or password == '' or username == '':
        messagebox.showwarning(title="Ooops", message="Please, don't leave any fields empty!")
        is_all_fields_fullfilled = False
    else:
        is_all_fields_fullfilled = True
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:"
                                                              f"\nEmail: {username}"
                                                              f"\nPassword{password}"
                                                              f"\n\nIs it ok to save?")

        if is_ok and is_all_fields_fullfilled:
            with open("data.txt", "a") as password_file:
                password_file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)  # The 100s are the x and y positions on canvas
canvas.grid(column=1, row=0)
canvas.config(highlightthickness=.1)

# Website Label

website_label = Label(text="Website: ", bg=WHITE, fg="#000000")
website_label.grid(column=0, row=1)

# Website entry

website_entry = Entry(bg=WHITE, width=39, fg='#000000')
website_entry.config(highlightthickness=0)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Username Label

username_label = Label(text="Email/Username: ", bg=WHITE, fg="#000000")
username_label.grid(column=0, row=2)

# Username entry

username_entry = Entry(bg=WHITE, width=39)
username_entry.config(highlightthickness=0, fg='#000000')
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(END, "ladeiavictor@gmail.com")

# Password Label

password_label = Label(text="Password: ", bg=WHITE, fg="#000000")
password_label.grid(column=0, row=3)

# Password entry

password_entry = Entry(bg=WHITE, width=21, fg='#000000')
password_entry.config(highlightthickness=0)
password_entry.grid(row=3, column=1)

# Generate Password Button

generate_password_button = Button(text="Generate Password", bg=WHITE, fg="#000000", command=generate_password)
generate_password_button.config(highlightthickness=0, background=WHITE, highlightbackground=WHITE)
generate_password_button.grid(row=3, column=2)

# Add Button
add_button = Button(text="Add", bg=WHITE, fg="#000000", width=36, command=save_password)
add_button.config(highlightthickness=0, highlightbackground=WHITE)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
