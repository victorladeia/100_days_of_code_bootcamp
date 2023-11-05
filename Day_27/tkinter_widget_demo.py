from tkinter import *

# Creating a new window and configuration
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

# Calls action() when pressed
button = Button()
button.config(text="Click Me", command=action)
button.pack()

# Entries
entry = Entry(width=30)
## Add some text to begin with
entry.insert(END, string="Some text to begin with.")
## Gets test in entry
print(entry.get())
entry.pack()

# Text
text = Text(height=5, width=30)
## Puts cursor in textbox.
text.focus()
## Adds some text to begin with
text.insert(END, "Exemple of multi-line text entry.")
print(text.get("1.0", END)) # 1.0 means getting text from first line at charactere 0.
text.pack()

# Scale
## Called with current scale value
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radiobutton
def radio_used():
    print(radio_state.get())
# variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banaa"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()