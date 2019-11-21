import tkinter as tk
import ComponentsHandler
from GraphUtils import bfs, minimalTree

# http://effbot.org/tkinterbook/canvas.htm#Tkinter.Canvas.create_rectangle-method

GLOBAL_OBJ = {
    # Tipo {<ID_DO_VERTICE>: [<ID_DO_VIZINHO>, <ID_DO_VIZINHO>, <ID_DO_VIZINHO>, ...]}
    'graph': {},
    # Tipo {<ID_DA_LINHA}: (<ID_DO_VERTICE_SAIDA>, <ID_DO_VERTICE_CHEGADA>)}
    'lineSet': {},
    # Tipo <ID_DO_VERTICE_SAIDA>
    'from': -1,
    # Tipo <ID_DO_VERTICE_CHEGADA>
    'to': -1
}


root = tk.Tk()
canv = tk.Canvas(root, width=640, height=480)


def doBFS(event):
    global canv
    print('Got object click', event.x, event.y)
    print(event.widget.find_closest(event.x, event.y))
    bfs(GLOBAL_OBJ["graph"], next(iter(GLOBAL_OBJ["graph"])), canv)


def doMinimalTree(event):
    global canv
    global GLOBAL_OBJ
    print('Got object click', event.x, event.y)
    print(event.widget.find_closest(event.x, event.y))
    minimalTree(GLOBAL_OBJ["graph"], next(iter(GLOBAL_OBJ["graph"])), canv, GLOBAL_OBJ)


ComponentManager = ComponentsHandler.initComponents(canv, GLOBAL_OBJ)

ComponentManager.createButton(
    470, 420, 150, 40, text="BFS!", callbackFunc=doBFS)

ComponentManager.createButton(
    470, 360, 150, 40, text="Arvore!", callbackFunc=doMinimalTree)


#canv.tag_bind(buttonId, '<ButtonPress-1>', onObjectClick)

canv.pack()
root.mainloop()
