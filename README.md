# Inteligencia Artificial :  Buscas em Grafos
Irá  ser aborda os seguintes tipos de buscas:
* Largura 
* Profundidade
* A*

# Problema Abordado
> Desenvolver um algoritmo que possibilite sair de qualquer ponto inicial e ir até qualquer objetivo (semelhante GPS)
> 
Para implementar as buscas foi escolhido um grafo de 20 nós, este grafo é uma representação dos estados Brasileiro,  a implementação do código foi feita em Python.



# Grafo
```mermaid
graph LR
Pará((Pará)) --> Mato_Grosso((Mato Grosso))
Roraima((Roraima)) --> Mato_Grosso
Mato_Grosso -->Roraima
Mato_Grosso --> Pará
Mato_Grosso --> Goiás((Goiás))
Goiás --> Mato_Grosso
Goiás --> Minas_Gerais((Minas Gerais))
Goiás --> Bahia((Bahia))
Minas_Gerais --> Goiás
Minas_Gerais --> São_Paulo((São Paulo))
Minas_Gerais --> Rio_de_Janeiro((Rio de Janeiro))
Minas_Gerais --> Espírito_Santo((Espírito Santo))
São_Paulo --> Minas_Gerais
São_Paulo --> Rio_de_Janeiro
Rio_de_Janeiro --> Minas_Gerais
Rio_de_Janeiro --> São_Paulo
Rio_de_Janeiro --> Espírito_Santo
Espírito_Santo --> Bahia
Espírito_Santo --> Rio_de_Janeiro
Espírito_Santo --> Minas_Gerais
Bahia --> Goiás
Bahia --> Minas_Gerais
Bahia --> Espírito_Santo
Bahia --> Sergipe((Sergipe))
Sergipe --> Bahia
```