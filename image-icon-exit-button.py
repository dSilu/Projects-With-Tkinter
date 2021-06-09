from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Learning to Code')
# importing an icon
root.iconbitmap('imagegallery.ico')

# importing images
my_image = ImageTk.PhotoImage(Image.open('elephant.jpg'))
my_label = Label(image= my_image)
my_label.pack()


# adding quit buttons
button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.pack()


root.mainloop()

# to check what packages do we hav: pip freeze