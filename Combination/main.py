from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import cv2 as cv
import tkinter as tk


event2canvas = lambda e, c: (c.canvasx(e.x), c.canvasy(e.y))

File = "stop.jpg"

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

if __name__ == "__main__":
    root = Tk()
    
        # #setting up a tkinter canvas with scrollbars
    frame = Frame(root)
    canvas = Canvas(frame)
    canvas.grid(row=1, column=0, sticky=N+S+E+W)
    frame.pack(fill=BOTH,expand=1)

    # #adding the image
    # File = askopenfilename(parent=root, initialdir="M:/",title='Choose an image.')
    # print("opening %s" % File)
    im = Image.open(File)
    img = ImageTk.PhotoImage(im)
    canvas.create_image(0,0,image=img,anchor="nw")

    root.title("Color Picker")
        
        #functions
    def printcolor(event):
        #outputting x and y coords to console
        cx, cy = event2canvas(event, canvas)
        colors = im.getpixel((cx,cy))
        Label(root, text = " Location: (" + str(cx) + ", " + str(cy) + ") = (Red, Green, Blue): " + str(colors)).pack()

    def color_detect(image_path, lower, upper):
        bounderies = [([0, 0, lower], [75, 75, upper])]
        image = cv.imread(image_path)
        for(lower, upper) in bounderies:
            lower = np.array(lower, dtype = "uint8")
            upper = np.array(upper, dtype = "uint8")
            mask = cv.inRange(image, lower, upper)
            output = cv.bitwise_and(image, image, mask = mask)
            cv.imshow("Red Detection", np.hstack([image, output, ]))
            cv.waitKey(0)

    def changeLimit():
        lowLimit = lower.get()
        highLimit = upper.get()
        return lowLimit, highLimit
    

    #events & variables
    lowLimit = 0
    highLimit = 255
    upper = Entry(root, width= 10)
    upper.pack()
    upper.insert(0, "Upper Limit for Red Range: ")
    lower = Entry(root, width= 10)
    lower.pack()
    lower.insert(1, "Lower Limit for Red Range: ")
    canvas.bind("<ButtonPress-1>",printcolor)
    tk.Button(root, text = "Enter Range", command = changeLimit)
    #tk.Button(root, text = "Red", command = color_detect(File, lowLimit, highLimit)).pack()
    app = FullScreenApp(root)
    root.mainloop()