
# Required library
from tkinter import *

list1 = []
root = Tk()
root.configure(bg='black') 
i_title = root.title("Ashkan file writer")
text_input = StringVar()

label1 = Label(
    root,
    borderwidth = 4,
    relief="sunken",
    fg = "green",
    bg = "black",
    text = "YOU CAN WRITE TEXT ON THE FILE USE THIS PROGRAM!"
)
label1.config(font =("Courier", 11))
label1.grid(columnspan=5)

text_box = Entry(
    root,
    width= 25,
    bg = "black",
    fg = "white",

    textvariable = text_input
)
text_box.grid(row=1, column=0)

Button_1 = Button(
    root,
    text = "Enter",
    bg = "black",
    fg = "green",
    command = d_Button_1
)
Button_1.grid(row=1, column=1)

Button_2 = Button(
    root,
    text = "Save Changes",
    bg = "black",
    fg = "green",
    command = lambda:d_Button_2()
)
Button_2.grid(row=1, column=2)

Button_3 = Button(
    root,
    text = "Clear All",
    bg = "black",
    fg = "green",
    command = lambda:d_Button_3()
)
Button_3.grid(row=1, column=3)

Button_4 = Button(
    root,
    text = "Save and Close",
    bg = "black",
    fg = "green",
    command = lambda:d_Button_4()
)
Button_4.grid(row=1, column=4)

root.mainloop()
