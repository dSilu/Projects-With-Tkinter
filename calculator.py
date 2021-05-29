# project 2: Let's build a calculator

from tkinter import *

root = Tk()
e = Entry(root, width=40, borderwidth=4)
e.grid(row=0, column=0, columnspan=3, padx=50, pady=40)

# giving buttons a life
def button_add(number):
    # e.delete(0, END)
    current= e.get()
    button_clear()
    e.insert(0, str(current) + str(number)) 
    # this function takes the input and linked to the number butoons, lambda activates the buttons

def button_clear():
    e.delete(0, END)

def aDD_button():
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    button_clear()

def button_equal():
    second_num = e.get()
    button_clear()

    if math == "addition":
        e.insert(0, f_num + int(second_num))
    
    if math == "substraction":
        e.insert(0, f_num - int(second_num))

    if math == "multiplication":
        e.insert(0, f_num * int(second_num))
    
    if math == "division":
        e.insert(0, f_num / int(second_num))

def multiply_Button():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    button_clear()

def substract_Button():
    first_num = e.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(first_num)
    button_clear()

def divide_Butoon():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    button_clear()
    

# creating Buttons: number button and additional buttons
button_1 = Button(root, text=1, padx= 40, pady=20, command=lambda:button_add(1))
button_2 = Button(root, text=2, padx= 40, pady=20, command=lambda:button_add(2))
button_3 = Button(root, text=3, padx= 40, pady=20, command=lambda:button_add(3))
button_4 = Button(root, text=4, padx= 40, pady=20, command=lambda:button_add(4))
button_5 = Button(root, text=5, padx= 40, pady=20, command=lambda:button_add(5))
button_6 = Button(root, text=6, padx= 40, pady=20, command=lambda:button_add(6))
button_7 = Button(root, text=7, padx= 40, pady=20, command=lambda:button_add(7))
button_8 = Button(root, text=8, padx= 40, pady=20, command=lambda:button_add(8))
button_9 = Button(root, text=9, padx= 40, pady=20, command=lambda:button_add(9))
button_0 = Button(root, text=0, padx= 40, pady=20, command=lambda:button_add(0))

add_button = Button(root, text="+", padx=40, pady=20, command=aDD_button)
substract_button = Button(root, text="-", padx=40, pady=20, command=substract_Button)
multiple_button = Button(root, text="*", padx=40, pady=20, command=multiply_Button)
divide_button = Button(root, text="/", padx=40, pady=20, command=divide_Butoon)
clear_button = Button(root, text="Clear", padx=30, pady=20, bg='red', fg='white', command=button_clear)
equal_button = Button(root, text="=", padx=60, pady=12, borderwidth=3, fg='white', bg='blue', command=button_equal)


# putting butoons to the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
multiple_button.grid(row=4, column=1)
divide_button.grid(row=4, column=2)

add_button.grid(row=5, column=0)
substract_button.grid(row=5, column=1)
clear_button.grid(row=5, column=2)

equal_button.grid(row=6, columnspan=120)



root.mainloop()

"""
-----------------------------------------------------------------
NOTE:
1- build intake box
2- first build the buttons and deploy them
3- make functions to give life to the buttons

*
- Every function except the the function linked equal and clear: contains two global variables
f_num and math, and the function linked to cleat button

- Equal function performs the operation via global variable math

- Another function has defiened to take the input
"""