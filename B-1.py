__author__ = 'los'

def read_graph_as_matrix(n, m):
    graph = [[None]*n for i in range(n)]
    for j in range(1, m+1):
        a, b = map(int, input().split())
        graph[a][b] = b
    return graph

#Color — массив, в котором хранятся цвета вершин (0 — белый, 1 — серый, 2 — черный).
#Edges — массив списков смежных вершин.
#Numbers — массив, в котором сохраняются новые номера вершин.
#Stack — стек, в котором складываются вершины после их обработки.
#Cycle — принимает значение true, если в графе найден цикл.
Edges = {'a':['c'], 'c':['b'], 'd':['c', 'b', 't'], 'b':[], 't':[]}
def topologicSortDFS2(Edges):
    Stack=[]
    Color=dict()
    for i in Edges.keys():
        Color[i]=0
    def topological_sort():
        def dfs(v):
#Если вершина серая, то мы обнаружили цикл.
#Заканчиваем поиск в глубину.
            if Color[v] == 1: return True
            if Color[v] == 2: return False#Если вершина черная, то заканчиваем ее обработку.
            Color[v] = 1#Красим вершину в серый цвет.
#Обрабатываем список смежных с ней вершин.
            for i in range(len(Edges[v])-1):
                if dfs(Edges[v][i]): return True
            Stack.append(v)#Кладем вершину в стек.
            Color[v] = 2#Красим вершину в черный цвет.
            return False;

#Вызывается обход в глубину от всех вершин.
#Заканчиваем работу алгоритма, если обнаружен цикл.
        for i in Edges.keys():
            Cycle = dfs(i)
            if Cycle:
                print("!!!имеется цикл!!!")
                exit()

#Заносим в массив новые номера вершин.
        Stack.reverse()
        return Stack
    return topological_sort()