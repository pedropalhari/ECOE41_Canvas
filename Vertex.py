from types import SimpleNamespace

import math


def angleBetweenTwoPoints(x1, y1, x2, y2):
    deltaX = x2 - x1
    deltaY = y2 - y1
    return math.atan2(deltaY, deltaX)


def initVertex(canvas, GLOBAL_OBJ):
    def createVertex(x, y, r, tagName):
        nonlocal canvas
        nonlocal GLOBAL_OBJ

        # Carinha do vertice
        vertex = canvas.create_oval(
            x, y, x + r, y + r, fill="black", width=5, tag=tagName)
        text = canvas.create_text(
            x + r/2, y + r/2, fill="white", text=tagName)

        def onPress(event):
            nonlocal GLOBAL_OBJ
            nonlocal vertex
            nonlocal r

            fromVertexId = GLOBAL_OBJ['from']
            toVertexId = GLOBAL_OBJ['to']
            globalGraph = GLOBAL_OBJ["graph"]
            globalLineSet = GLOBAL_OBJ["lineSet"]

            # Usando objetos globais, seta o FROM e o TO. Ambos referências de elementos canvas
            # Com as referências, pega as posições dos vértices e traça uma linha entre elas
            # Lembrei do primário e meti uma continha de seno/cosseno pra ficar na bordinha
            if(fromVertexId == -1):
                GLOBAL_OBJ['from'] = vertex
            else:
                toVertexId = vertex
                print(
                    "DO VERTICE " + str(fromVertexId) + " ATE O VERTICE " + str(toVertexId))

                print(canvas.coords(fromVertexId))
                print(canvas.coords(toVertexId))

                fromCoords = canvas.coords(fromVertexId)
                toCoords = canvas.coords(toVertexId)

                # Cálculo do ângulo na criação da linha para deixar a setinha na bordinha
                angle = angleBetweenTwoPoints(
                    fromCoords[0], fromCoords[1], toCoords[0], toCoords[1])

                lineId = canvas.create_line(
                    fromCoords[0] + r/2 + math.cos(angle) * r/2, fromCoords[1] + r/2 + math.sin(angle) * r/2, toCoords[0] + r/2 - math.cos(angle) * r/2, toCoords[1] + r/2 - math.sin(angle) * r/2, width=5, arrow="last")

                # Adicionando no grafo que vai ser passado para o BFS
                if(globalGraph.get(fromVertexId) == None):
                    globalGraph[fromVertexId] = []

                if(globalGraph.get(toVertexId) == None):
                    globalGraph[toVertexId] = []

                globalGraph[fromVertexId].append(
                    toVertexId)

                # Adiciona em um dicionário global com as linhas, para poder remover as ligações
                # do vértice caso ele seja deletado
                globalLineSet[lineId] = (fromVertexId, toVertexId)

                print(globalGraph)

                GLOBAL_OBJ['from'] = -1
                GLOBAL_OBJ['to'] = -1

        #Deletando o vértice
        def onPressMiddle(event):
            nonlocal GLOBAL_OBJ
            nonlocal vertex
            nonlocal canvas

            globalLineSet = GLOBAL_OBJ["lineSet"]

            # Deleta todas as linhas associadas a ele
            for lineId, verts in globalLineSet.items():
                # O vértice que estou deletando tá nessa linha
                if(vertex in verts):
                    canvas.delete(lineId)

            # Deleta o vértice
            canvas.delete(vertex)   
            canvas.delete(text)   

        # Animaçõezinhas de press
        def onEnter(event):
            nonlocal vertex
            canvas.itemconfig(vertex, fill="white",  outline="black")
            canvas.itemconfig(text, fill="black")

        def onLeave(event):
            nonlocal vertex
            canvas.itemconfig(vertex, fill="black",  outline="black")
            canvas.itemconfig(text, fill="white")

        canvas.tag_bind(vertex, '<Enter>', onEnter)
        canvas.tag_bind(text, '<Enter>', onEnter)

        canvas.tag_bind(vertex, '<Leave>', onLeave)
        canvas.tag_bind(text, '<Leave>', onLeave)

        canvas.tag_bind(vertex, '<ButtonPress-1>', onPress)
        canvas.tag_bind(text, '<ButtonPress-1>', onPress)

        canvas.tag_bind(vertex, '<ButtonPress-2>', onPressMiddle)
        canvas.tag_bind(text, '<ButtonPress-2>', onPressMiddle)

        # canvas.tag_bind(text, '<ButtonPress-1>', clickFeedback)

        # canvas.tag_bind(button, '<ButtonRelease-1>', clickRelease)
        # canvas.tag_bind(text, '<ButtonRelease-1>', clickRelease)

        # def deleteButton():
        #     nonlocal button
        #     nonlocal text
        #     nonlocal shadow

        #     canvas.delete(button)
        #     canvas.delete(text)
        #     canvas.delete(shadow)

        return vertex  # , button, shadow, deleteButton

    returnMap = {
        "createVertex": createVertex
    }

    return SimpleNamespace(**returnMap)
