carrinho = []
carrinho.append(('Produto 1', 20))
carrinho.append(('Produto 2', 30))
carrinho.append(('Produto 4', 50))

total =sum([float(y) for x,y in carrinho])
print(total)