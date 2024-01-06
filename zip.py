import itertools

cidades = ['Porto Alegre','São Paulo', 'Belo Horizonte',]
estados = ['RS', 'SP', 'MG']
cidades_estados = zip(cidades,estados)

print(list(cidades_estados))