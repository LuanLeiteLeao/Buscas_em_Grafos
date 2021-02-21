from abstract_data_type.states_graph import State

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
para.adjacencies = [mato_grosso]
roraima.adjacencies = [mato_grosso]
mato_grosso.adjacencies = [roraima, para, goias]
goias.adjacencies = [mato_grosso, minas_gerais, bahia]
minas_gerais.adjacencies = [goias, sao_paulo, rio_de_janeiro, espirito_santo]
sao_paulo.adjacencies = [minas_gerais, rio_de_janeiro]
rio_de_janeiro.adjacencies = [minas_gerais, sao_paulo, espirito_santo]
espirito_santo.adjacencies = [bahia, rio_de_janeiro, minas_gerais]
bahia.adjacencies = [goias, minas_gerais, espirito_santo, sergipe]
sergipe.adjacencies = [bahia]

graph = [
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
