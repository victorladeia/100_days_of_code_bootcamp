from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
#my_label.pack()
#my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

# Button 1
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Button 2
button2 = Button(text="Click Me", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid()
input.grid(column=3, row=3)

window.mainloop()