import tkinter as tk
import ComponentsHandler

# http://effbot.org/tkinterbook/canvas.htm#Tkinter.Canvas.create_rectangle-method

GLOBAL_OBJ = {
    'graph': {},
    'from': -1,
    'to': -1
}

def onObjectClick(event):
    print('Got object click', event.x, event.y)
    print(event.widget.find_closest(event.x, event.y))


root = tk.Tk()
canv = tk.Canvas(root, width=640, height=480)

ComponentManager = ComponentsHandler.initComponents(canv, GLOBAL_OBJ)

ComponentManager.createButton(
    100, 100, 150, 40, text="Opa", callbackFunc=onObjectClick)


#canv.tag_bind(buttonId, '<ButtonPress-1>', onObjectClick)

canv.pack()
root.mainloop()
