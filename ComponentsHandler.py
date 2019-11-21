from types import SimpleNamespace

import Button
import Vertex


def initComponents(canvas, GLOBAL_OBJ):
    createButton = Button.initButton(canvas).createButton
    createVertex = Vertex.initVertex(canvas, GLOBAL_OBJ).createVertex

    def getCoordinates(vertexId):
        return canvas.find_withtag(vertexId)

    counter = 0

    def vertexCreator(event):
        nonlocal counter
        createVertex(
            event.x - 15, event.y - 15, 30, tagName=counter)
        counter = counter + 1


    canvas.bind("<Button-3>", vertexCreator)

    returnMap = {
        "createButton": createButton,
        "createVertex": createVertex,
        "getCoordinates": getCoordinates
    }

    return SimpleNamespace(**returnMap)
