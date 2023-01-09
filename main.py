from tkinter import *

window = Tk()
window.title("Miles to Kilometer converter")
window.config(height=300, width=500)
window.config(padx=30, pady=30)


def calculate_result():
    result.config(text=round(int(entry.get())*1.609, 2))


# entry
entry = Entry()
entry.insert(END, "0")
entry.grid(column=1, row=0)

# 4 labels > Miles, Km, and "is equal to", and the result
miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

# 1 button to show the result of inputting the miles into the function that calculates the KM.
button = Button(activebackground="red", text="Calculate", command=calculate_result)
button.grid(column=1, row=2)

window.mainloop()
