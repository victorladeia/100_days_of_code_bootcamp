from tkinter import *


def convert_mi_to_km():
    mi = float(input.get())
    outputLabel.config(text= f"{mi * 1.609}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Entry - get input
input = Entry(width=10)
input.grid(column=1 , row=0)

# Label - "Miles"
miles_label = Label(text="Miles")
miles_label.grid(column=2 , row=0)

# Label - "is equal to"
equal_label = Label(text="is equal to")
equal_label.grid(column=0 , row=1)

# Label - "km"
km_label = Label(text="km")
km_label.grid(column=2, row=1)

# Label - [output]
outputLabel = Label(text="0")
outputLabel.grid(column=1, row=1)

# button - [Calculate]
button = Button(text="Calculate", command=convert_mi_to_km)
button.grid(column=1, row=2)

window.mainloop()
