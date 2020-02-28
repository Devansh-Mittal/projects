import tkinter as tk

top = tk.Tk()

tk.Label(top, text="Name").grid(row=0)
tk.Label(top, text="Password").grid(row=1)
tk.Label(top, text="City").grid(row=2)

e1 = tk.Entry(top)
e2 = tk.Entry(top)
e3 = tk.Entry(top)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

tk.Button(top,
         text='Quit',
         command=top.quit).grid(row=3,
                                column=1,
                                sticky=tk.W,
                                pady=4)
tk.Button(top,
         text='Submit',
         command=top.quit).grid(row=3,
                                column=2,
                                sticky=tk.W,
                                pady=4)
tk.Checkbutton(top, text = "Keep Me Logged In").grid(columnspan = 2)
top.mainloop()
