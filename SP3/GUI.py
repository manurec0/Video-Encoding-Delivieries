from tkinter import *
from ffmpeg_python import change_res

# script to create a very simple GUI using tkinter in order to use the method of changing resolution to a video using
# ffmpeg
# INSTRUCTIONS: enter the path of the input file, width and height of the desired resolution and click GO to create new
# video file with the desired specifications. To exit you can just close the window.

m = Tk()
m.title('Change Resolution')

Label(m, text='Input File: ').grid(row=0)
Label(m, text='New Width: ').grid(row=1)
Label(m, text='New Height: ').grid(row=2)

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

input_file = Entry(m, textvariable=v1)
w = Entry(m, textvariable=v2)
h = Entry(m, textvariable=v3)


def print_input(*args):
    print(v1.get(), v2.get(), v3.get())


def create_variables(*args):
    v = v1.get()
    r = v2.get() + ":" + v3.get()
    return v, r


button = Button(m, text='Go!', command=lambda: change_res(v1.get(), v2.get() + ":" + v3.get()))

input_file.grid(row=0, column=1)
w.grid(row=1, column=1)
h.grid(row=2, column=1)
button.grid(row=3, column=1)

m.mainloop()

