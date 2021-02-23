from graph_of_states.graph_with_distance_between_states import graph_with_distance_between_states as graph
from graph_of_states.graph_with_distance_between_states import sergipe
from graph_of_states.graph_with_distance_between_states import bahia
from graph_of_states.graph_with_distance_between_states import sao_paulo
from graph_of_states.graph_with_distance_between_states import espirito_santo
from graph_of_states.graph_with_distance_between_states import minas_gerais
from graph_of_states.graph_with_distance_between_states import mato_grosso
from graph_of_states.graph_with_distance_between_states import para
from graph_of_states.graph_with_distance_between_states import roraima



def a_star(ponto_de_partida, graph, visitado):
    """
   Args:
         ponto_de_partida (State): é de onde irá começar a busca, o ponto de partida.
         ponto_final (State): é o objetivo da busca, oque deve ser achado, o ponto de final

     Returns:
         State: caso ache retorna o elemento achado e caso não ache rentona None.
    """

    if ponto_de_partida not in visitado:
        visitado.append(ponto_de_partida)
        index = graph.index(ponto_de_partida)
        # primeiro posicao
        menor = graph[index].adjacencies[0]

        for vizinho in graph[index].adjacencies:
            if vizinho.distance < menor.distance:
                menor= vizinho

        print(menor)
        a_star(menor.state, graph, visitado)




retorno =  a_star(sergipe, graph, [])
# print(retorno)
