from tkinter import *

root = Tk()

def initcal():
    calc = Toplevel()
    root.withdraw()

    def on_closing():
        calc.destroy()
        root.deiconify()

    calc.protocol("WM_DELETE_WINDOW", on_closing)

myButton2 = Button(root, text="delete", command=initcal)
myButton2.pack()

root.mainloop()
