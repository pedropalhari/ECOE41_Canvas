import tkinter as tk
import ComponentsHandler

# http://effbot.org/tkinterbook/canvas.htm#Tkinter.Canvas.create_rectangle-method


def onObjectClick(event):
    print('Got object click', event.x, event.y)
    print(event.widget.find_closest(event.x, event.y))


root = tk.Tk()
canv = tk.Canvas(root, width=640, height=480)

ComponentManager = ComponentsHandler.initComponents(canv)

ComponentManager.createButton(
    10, 10, 150, 100, text="Opa", callbackFunc=onObjectClick)


#canv.tag_bind(buttonId, '<ButtonPress-1>', onObjectClick)
canv.pack()
root.mainloop()
