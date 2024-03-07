#Listas numéricas e ferramentas exemplos

##Usando a função range()
num_list = []
for value in range(1,5):
    print(value)
    num_list.append(value)
print(num_list)

num_list = []
for value in range(4,5):
    print(value)
    num_list.append(value)
print(num_list)

##Uma forma mais simples
num_list = list(range(1,5))
print(num_list)

##fornecendo a razao de incremento
num_list = list(range(1,5,2))
print(num_list)

##Um Exemplo mais complexo
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)