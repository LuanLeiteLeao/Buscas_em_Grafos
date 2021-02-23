from abstract_data_type.states_graph import State
from abstract_data_type.distancebetween import DistanceBetween
# Estados
test = State('test')
para = State('Pará')
roraima = State('Roraima')
mato_grosso = State('Mato Grosso')
goias = State('Goiás')
minas_gerais = State('Minas Gerais')
sao_paulo = State('São Paulo')
rio_de_janeiro = State('Rio de Janeiro')
espirito_santo = State('Espirito Santo')
bahia = State('Bahia')
sergipe = State('Sergipe')

# Listas de adjacencias entre estados
para.adjacencies = [DistanceBetween(mato_grosso,1380) ]

roraima.adjacencies = [DistanceBetween(mato_grosso,1805)]

mato_grosso.adjacencies = [DistanceBetween(roraima,1706)
    ,DistanceBetween(para,1380)
    ,DistanceBetween(goias,758.5)]

goias.adjacencies = [DistanceBetween(mato_grosso,758.5),
                     DistanceBetween(minas_gerais,883.2),
                     DistanceBetween(bahia, 1302.09)]

minas_gerais.adjacencies = [ DistanceBetween(goias,883.2),
                             DistanceBetween(sao_paulo,691.08),
                             DistanceBetween(rio_de_janeiro,635.6),
                             DistanceBetween(espirito_santo,740.9)]

sao_paulo.adjacencies = [DistanceBetween(minas_gerais,691.08),
                         DistanceBetween(rio_de_janeiro,435.7)]

rio_de_janeiro.adjacencies = [ DistanceBetween(minas_gerais,635.6),
                               DistanceBetween(sao_paulo,435.7),
                               DistanceBetween(espirito_santo,704)]

espirito_santo.adjacencies = [DistanceBetween(bahia,1034.2),
                              DistanceBetween(rio_de_janeiro,704),
                              DistanceBetween(minas_gerais,740.9)]

bahia.adjacencies = [DistanceBetween(goias,1302.09),
                         DistanceBetween(minas_gerais,991.4 ),
                     DistanceBetween(espirito_santo,1034.2),
                     DistanceBetween(sergipe,694)]

sergipe.adjacencies = [DistanceBetween(bahia,694)]


graph_with_distance_between_states = [
    para,
    roraima,
    mato_grosso,
    goias,
    minas_gerais,
    sao_paulo,
    rio_de_janeiro,
    espirito_santo,
    bahia,
    sergipe
]
