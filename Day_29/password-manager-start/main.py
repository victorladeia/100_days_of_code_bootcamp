from tkinter import *
# ---------------------------- CONSTANST --------------------------------#
WHITE = "#FFFFFF"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

website_entry = Entry(bg=WHITE, width=39)
website_entry.config(highlightthickness=0)
website_entry.grid(column=1, row=1, columnspan=2)

# Username Label

username_label = Label(text="Email/Username: ", bg=WHITE, fg="#000000")
username_label.grid(column=0, row=2)

# Username entry

username_entry = Entry(bg=WHITE, width=39)
username_entry.config(highlightthickness=0)
username_entry.grid(row=2, column=1, columnspan=2)

# Password Label

password_label = Label(text="Password: ", bg=WHITE, fg="#000000")
password_label.grid(column=0, row=3)

# Password entry

password_entry = Entry(bg=WHITE, width=21)
password_entry.config(highlightthickness=0)
password_entry.grid(row=3, column=1)

# Generate Password Button

generate_password_button = Button(text="Generate Password", bg=WHITE, fg="#000000")
generate_password_button.config(highlightthickness=0, background=WHITE, highlightbackground=WHITE)
generate_password_button.grid(row=3, column=2)

# Add Button
add_button = Button(text="Add", bg=WHITE, fg="#000000", width=36)
add_button.config(highlightthickness=0, highlightbackground=WHITE)
add_button.grid(column=1, row=5, columnspan=2)



window.mainloop()
