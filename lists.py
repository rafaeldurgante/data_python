from typing import List

string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
lista = list(string)
lista2= [v for v in string]
n = 10
comp = [string[i:i+n] for i in range(0, len(string), n)]
retorno = '.'.join(comp)

print(retorno)

