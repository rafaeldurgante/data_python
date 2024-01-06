import copy

d1 = {1:'valor da chave 1',
      2:'valor da chave 2',
      'chave 3': 'valor da chave 3',
      (1,2,3): 'valor da chave 4'
}

v = d1.copy()
v[1] = 'Rafael'
v[1,2,3] = (4,5,6)

d2 = {
    1:2,
    2:3,
    4:5,
}
d3 = {
    'a':'b',
    'c':'d',
    'e':'f',
}
print(d2)
print(d3)
d1.update(d2)
d2.update(d3)
print(d1)
print(v)
for x, v in d1.items():
    print(x, v)


