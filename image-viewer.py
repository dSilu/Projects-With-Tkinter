from tkinter import *
from PIL import Image, ImageTk

root = Tk()  # mind the parethnesses
# import title
root.title('Wonders of Wild')
# import icon
root.iconbitmap('imagegallery.ico')  
#.ico file

# importing images
my_image1 = ImageTk.PhotoImage(Image.open('elephant.jpg'))
my_image2 = ImageTk.PhotoImage(Image.open('koala.jpg'))
my_image3 = ImageTk.PhotoImage(Image.open('pecock.jpg'))
# my_image4 = ImageTk.PhotoImage(Image.open('kangaroo.jpg'))
my_image5 = ImageTk.PhotoImage(Image.open('panda.jpg'))
my_image6 = ImageTk.PhotoImage(Image.open('polar bear.jpg'))
# my_image7 = ImageTk.PhotoImage(Image.open('eagle.jpg'))
my_image8 = ImageTk.PhotoImage(Image.open('wolf.jpg'))
my_image9 = ImageTk.PhotoImage(Image.open('panther.jpg'))
my_image10 = ImageTk.PhotoImage(Image.open('bengal tiger.jpg'))
my_image11 = ImageTk.PhotoImage(Image.open('Dinosaurs.jpg'))

image_list = [my_image1, my_image2, my_image3, my_image5, my_image6, my_image8, my_image9, my_image10, my_image11]

# Adding stats bar
status = Label(root, bd=1, relief=SUNKEN, anchor=E, text='Image 1 of ' + str(len(image_list)))

my_label = Label(image=my_image1)
my_label.grid(row=0, column=0, columnspan=3)



# import navigation buttons
def  forward(image_num):
    global my_label
    global forward_button
    global back_button

    my_label.grid_forget()
    my_label =Label(image= image_list[image_num -1]) # confusing!
    forward_button = Button(root, text='>>', bg='#87cefa', command=lambda: forward(image_num+1))
    back_button = Button(root, text='<<', bg='#87cefa', command=lambda: back(image_num -1))
    
    if image_num == 9:
        forward_button = Button(root, text='>>', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)

    # update status bar
    status = Label(root, bd=1, relief=SUNKEN, anchor=E, text='Image '+ str(image_num)+ ' of ' + str(len(image_list)))
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_num):
    global my_label
    global forward_button
    global back_button

    my_label =Label(image= image_list[image_num -1]) # confusing!
    forward_button = Button(root, text='>>', bg='#87cefa', command=lambda: forward(image_num+1))
    back_button = Button(root, text='<<', bg='#87cefa', command=lambda: back(image_num -1))
    
    if image_num == 1:
        back_button = Button(root, text='<<', state= DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)

    status = Label(root, bd=1, relief=SUNKEN, anchor=E, text='Image '+ str(image_num)+ ' of ' + str(len(image_list)))
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


back_button = Button(root, text='<<', bg='#87cefa', command=back, state=DISABLED)
forward_button = Button(root, text='>>', bg='#87cefa',  command=lambda:forward(2))
quit_button = Button(root, text='Exit', bg='#8b0000', fg='white', command=root.quit)

back_button.grid(row=1, column=0)
quit_button.grid(row=1, column=1)
forward_button.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)


root.mainloop()



