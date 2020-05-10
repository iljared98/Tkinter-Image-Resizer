# Author : Isaiah Jared
from tkinter import *
from tkinter import filedialog, messagebox
import os
import sys
import glob
import PIL
from PIL import Image


def dirChoice():
  global path
  path = filedialog.askdirectory() + '/'

def progExit():
    sys.exit(0)

def aboutMe():
    messagebox.showinfo('About Me', 'Author: Isaiah Jared \n\nhttps://github.com/iljared98/', )

def progHelp():
    messagebox.showinfo('Help','Select your desired directory that contains\nthe images you wish to resize, enter the new dimensions\nand file extension, then click "resize your images"\n to resize them in bulk. Please note that\n the original images are saved in the directory of this\n executable.')

def main():
    def retrieveFunc():
        xDim = xDimEntry.get()
        yDim = yDimEntry.get()
        imgExt = extEntry.get()

        try:
            if xDim == "" or yDim == "" or imgExt == "":
                messagebox.showerror('Blank Input Field',
                                     'Please enter an integer value in the two dimension fields and an image file extension (PNG, JPG formats) in the last field.')
            elif '.' in imgExt:
                messagebox.showerror('Extension Input Error',
                                     'The extension input only requires (png/jpg/gif), the . delimiter is not required.')

            else:
                xDim = int(xDim)
                yDim = int(yDim)
                resizeFunc(xDim, yDim, imgExt)
        except:
            messagebox.showerror('Exception Error','You either did not select a directory or entered an invalid value for one of the dimensions. Please try again.')
    def resizeFunc(xDim, yDim, imgExt):
        imgFiles = glob.glob(f'{path}*.{imgExt}')

        images = []
        print(imgFiles)

        for image in imgFiles:
            images.append(image)
            Image.open(image)
        if len(images) >= 1:
            i = 0
            for image in range(len(images)):
                imgString = str(images[image])


                img = Image.open(imgString)
                newImg = img.resize((xDim,yDim))

                newImg.save(f'resized-{i}.{imgExt}')
                i += 1

            messagebox.showinfo('Task Complete','All selected images have been resized!')
        else:
            messagebox.showerror('No Images Detected','The directory given does not contain any images with your specified file extension. Please select a valid directory and try again.')


    window = Tk()
    window.title("Mass Image Resizer")
    window.minsize(425, 300)

    menu = Menu(window)
    window.config(menu=menu)

    fileMenu = Menu(menu,tearoff=0)
    fileMenu.add_command(label="Exit",command=progExit)
    menu.add_cascade(label="File",menu=fileMenu)

    helpMenu = Menu(menu,tearoff=0)
    helpMenu.add_command(label="About Me",command=aboutMe)
    helpMenu.add_command(label="Instructions",command=progHelp)
    menu.add_cascade(label="Help",menu=helpMenu)

    xDimLabel = Label(window, text="X-Dimension")
    xDimLabel.grid(column=0, row=1,pady=(15,0))

    xDimEntry = Entry(window)
    xDimEntry.grid(column=0, row=2, padx=10)

    yDimLabel = Label(window, text="Y-Dimension")
    yDimLabel.grid(column=1, row=1,pady=(15,0))


    yDimEntry = Entry(window)
    yDimEntry.grid(column=1, row=2, padx=10)

    extLabel = Label(window, text="Image Extension")
    extLabel.grid(column=2, row=1,pady=(15,0))


    extEntry = Entry(window)
    extEntry.grid(column=2, row=2,padx=10)

    dirChoiceBtn = Button(window, text="Choose Directory", command=dirChoice)
    dirChoiceBtn.grid(column=0, row=5, pady=(140, 5))

    resizeBtn = Button(window, text="Resize your images", command=retrieveFunc)
    resizeBtn.grid(column=2, row=5, pady=(135, 5))

    window.mainloop()
    
main()