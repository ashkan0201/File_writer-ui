
# Required library
from tkinter import *

with open("data.txt", "w")as file:
    file.write("")

list1 = []
root = Tk()
root.configure(bg='black') 
i_title = root.title("Ashkan file writer")
text_input = StringVar()

# Enter
def d_Button_1():
    list1.append(text_input.get())
    text_box.delete(0, 'end')

# Save
def d_Button_2():
    with open("data.txt", "a") as file:
        if list1 == []:
            file.write("") 

        else:
            temp = "\n".join(list1)
            file.write(temp+"\n")
            list1.clear()
            file.close()

#Clear all
def d_Button_3():
    with open("data.txt", "w")as file:
        file.write("")

#Save and Exit
def d_Button_4():
    with open("data.txt", "a")as file:
        if list1 == []:
            file.write("") 

        else:
            temp = "\n".join(list1)
            file.write(temp+"\n")
            list1.clear()
            file.close()
    root.quit()

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

# Text box
text_box = Entry(
    root,
    width= 25,
    bg = "black",
    fg = "white",

    textvariable = text_input
)
text_box.grid(row=1, column=0)

# Enter button
Button_1 = Button(
    root,
    text = "Enter",
    bg = "black",
    fg = "green",
    command = d_Button_1
)
Button_1.grid(row=1, column=1)

# Save button
Button_2 = Button(
    root,
    text = "Save Changes",
    bg = "black",
    fg = "green",
    command = lambda:d_Button_2()
)
Button_2.grid(row=1, column=2)

# Clear all button
Button_3 = Button(
    root,
    text = "Clear All",
    bg = "black",
    fg = "green",
    command = lambda:d_Button_3()
)
Button_3.grid(row=1, column=3)

# Save and exit button
Button_4 = Button(
    root,
    text = "Save and Exit",
    bg = "black",
    fg = "green",
    command = lambda:d_Button_4()
)
Button_4.grid(row=1, column=4)

root.mainloop()
