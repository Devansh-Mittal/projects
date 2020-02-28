from tkinter import *

window = Tk()


# def km_to_miles():
#     try:
#         miles = float(e1_value.get()) * 1.6
#     except ValueError:
#         miles = "Enter a number please"
#         return miles
#     t1.insert(END, miles)
#
#
# b1 = Button(window, text = "execute", command = km_to_miles)
# b1.grid(row=0, column=0)
#
# e1_value = StringVar()
# e1 = Entry(window, textvariable=e1_value)
# e1.grid(row=0, column=1)
#
# t1 = Text(window, height=1, width=20)
# t1.grid(row=0, column=2)

def kg_to_value():
    grams = float(e1_value.get()) * 1000
    pounds = float(e1_value.get()) * 2.20462
    ounces = float(e1_value.get()) * 35.274

    t1.delete('1.0', END)
    t2.delete('1.0', END)
    t3.delete('1.0', END)

    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)


e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

e2 = Label(window,text="Kg")
e2.grid(row=0,column=0)

b1 = Button(window, text="Convert", command=kg_to_value)
b1.grid(row=0, column=2)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()
