from graph_of_states.graph import graph
from graph_of_states.graph import sergipe
from graph_of_states.graph import bahia
from graph_of_states.graph import para
from graph_of_states.graph import espirito_santo
from graph_of_states.graph import *
from collections import deque

Visitado = [] # List for visited nodes.
fila = []     #Initialize a queue


def bfs(Visitado, graph, ponto_de_partida, ponto_final):
  """
 Args:
       ponto_de_partida (State): é de onde irá começar a busca, o ponto de partida.
       ponto_final (State): é o objetivo da busca, oque deve ser achado, o ponto de final

   Returns:
       State: caso ache retorna o elemento achado e caso não ache rentona None.
  """
  Visitado.append(ponto_de_partida)
  fila.append(ponto_de_partida)

  while fila:
    m = fila.pop(0)
    print (m.name)
    index = graph.index(m)
    for visinho in graph[index].adjacencies:
        print("=====> {}".format(visinho))
        if visinho == ponto_final:
          return visinho
        if visinho not in Visitado:
            Visitado.append(visinho)
            fila.append(visinho)


# Driver Code
test = bfs(Visitado, graph, mato_grosso, sergipe)    # function calling
