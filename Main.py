import tkinter as tk
import ComponentsHandler
from BFS import bfs

# http://effbot.org/tkinterbook/canvas.htm#Tkinter.Canvas.create_rectangle-method

GLOBAL_OBJ = {
    'graph': {},
    'from': -1,
    'to': -1
}




root = tk.Tk()
canv = tk.Canvas(root, width=640, height=480)

def onObjectClick(event):
    global canv
    print('Got object click', event.x, event.y)
    print(event.widget.find_closest(event.x, event.y))
    bfs(GLOBAL_OBJ["graph"], next(iter(GLOBAL_OBJ["graph"])), canv)

ComponentManager = ComponentsHandler.initComponents(canv, GLOBAL_OBJ)

ComponentManager.createButton(
    470, 420, 150, 40, text="Rodar!", callbackFunc=onObjectClick)


#canv.tag_bind(buttonId, '<ButtonPress-1>', onObjectClick)

canv.pack()
root.mainloop()
