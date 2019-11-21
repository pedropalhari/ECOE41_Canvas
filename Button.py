from types import SimpleNamespace

def initButton(canvas):
    def createButton(x, y, width, height, text, callbackFunc):
        nonlocal canvas
        shadow = canvas.create_rectangle(
            x + 3, y + 3, x + width + 3, y + height + 3, width=5, outline="grey", fill="grey")
        button = canvas.create_rectangle(
            x, y, x + width, y + height, width=5, fill="black")
        text = canvas.create_text(
            x + width/2, y + height/2, fill="white", text=text)

        def clickFeedback(event):
            nonlocal button
            nonlocal text
            canvas.itemconfig(button, fill="white", outline="white")
            canvas.itemconfig(text, fill="black")
            callbackFunc(event)

        def clickRelease(event):
            nonlocal button
            nonlocal text
            canvas.itemconfig(button, fill="black",  outline="black")
            canvas.itemconfig(text, fill="white")

        canvas.tag_bind(button, '<ButtonPress-1>', clickFeedback)
        canvas.tag_bind(text, '<ButtonPress-1>', clickFeedback)

        canvas.tag_bind(button, '<ButtonRelease-1>', clickRelease)
        canvas.tag_bind(text, '<ButtonRelease-1>', clickRelease)

        def deleteButton():
            nonlocal button
            nonlocal text
            nonlocal shadow

            canvas.delete(button)
            canvas.delete(text)
            canvas.delete(shadow)

        return text, button, shadow, deleteButton

    returnMap = {
        "createButton": createButton
    }

    return SimpleNamespace(**returnMap)
