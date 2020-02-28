from tkinter import *
convertor= Tk()
def Dollar_in_rupee():
    rupee=float(v1_value.get())*71.04

    t1.delete('1.0',END)
    t1.insert(END,rupee)
v1_value=StringVar()
v1_value=Entry(convertor,textvariable=v1_value)
v1_value.grid(row=0,column=1)
label_1=Label(convertor,text="Input in Dollar")
label_1.grid(row=0,column=0)


b1=Button(convertor,text="Convert",command=Dollar_in_rupee)
b1.grid(row=1,column=0)

t1=Text(convertor,height=1,width=20)
t1.grid(row=1,column=1)


convertor.mainloop()

