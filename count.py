from itertools import count
contador = count(start=1, step=2)
lista =[1,2,3,4,5, 'rafael', 'durga']

lista = zip(contador, lista)
print(list(lista))