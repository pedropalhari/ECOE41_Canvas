import collections
import time


def minimalTree(graph, root, canvas, GLOBAL_OBJ):
    visited, queue = set(), collections.deque([root])
    visited.add(root)

    visitedLineArray = []

    for vertex in list(graph):
        canvas.itemconfig(vertex, fill="black", outline="black")

    while queue:
        vertex = queue.popleft()
        print("EXPLORANDO VIZINHOS DE " + str(vertex))
        canvas.itemconfig(vertex, fill="red", outline="black")
        canvas.update()
        # time.sleep(1)

        for neighbour in graph[vertex]:
            print
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

                # O identificador dessa linha é um par que saiu do vertex e foi para neighbour
                visitedLineArray.append((vertex, neighbour))

                print("VIZINHO " + str(neighbour))
                canvas.itemconfig(neighbour, fill="green", outline="black")
                canvas.update()
                # time.sleep(1)

        canvas.itemconfig(vertex, fill="green", outline="black")

    # Rotina para limpar todos os caminhos não andados
    globalLineSet = GLOBAL_OBJ["lineSet"]

    linesThatShouldKeepExisting = []

    # Visitei esses vértices
    for lineVerts in visitedLineArray:
        for lineId, verts in globalLineSet.items():
            if(lineVerts == verts):
                # A linha que representa essa ligação tem esse par (x, y) de vértices
                linesThatShouldKeepExisting.append(lineId)

    # Se a linha não está nas linhas que montam a árvore, deleta ela
    for lineId in globalLineSet.keys():
        if(lineId not in linesThatShouldKeepExisting):
            canvas.delete(lineId)

    allVertex = GLOBAL_OBJ["graph"].keys()
    vertexThatShouldKeepExisting = {}

    #for lineId, verts in globalLineSet.items():






    


def bfs(graph, root, canvas):
    visited, queue = set(), collections.deque([root])
    visited.add(root)

    for vertex in list(graph):
        canvas.itemconfig(vertex, fill="black", outline="black")

    while queue:
        vertex = queue.popleft()
        print("EXPLORANDO VIZINHOS DE " + str(vertex))
        canvas.itemconfig(vertex, fill="red", outline="black")
        canvas.update()
        time.sleep(1)

        for neighbour in graph[vertex]:
            print
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                print("VIZINHO " + str(neighbour))
                canvas.itemconfig(neighbour, fill="green", outline="black")
                canvas.update()
                time.sleep(1)

        canvas.itemconfig(vertex, fill="green", outline="black")


if __name__ == '__main__':
    graph = {0: [1, 2, 4], 1: [2], 2: [3], 3: [1, 2], 4: []}
    bfs(graph, 0)
