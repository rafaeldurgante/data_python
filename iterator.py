# listas, tuples, strings ---> Iteráveis Sequences

nome = 'Rafael Durgante'
for v in nome:
    print(v)

print('#'* 80)
iterador= iter(nome)
gerador = (v for v in nome)
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
for letra in gerador:
    print(letra)