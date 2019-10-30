from types import SimpleNamespace

import Button

def initComponents(canvas):
    createButton = Button.initButton(canvas).createButton

    returnMap = {
        "createButton": createButton
    }

    return SimpleNamespace(**returnMap)
