#   Alterando, acrescentando ou removendo elementos

#   Empty
L_Empty = []

#   Acrescentando Elementos
#   ##  Ao Final - Método append()
L_Empty.append('i0e1')
L_Empty.append('i1e2')
L_Empty.append('i2e3')
L_Full = L_Empty
print(L_Full)

#   Acrescentando Elementos
#   ##  Posicionando - Método insert(indice, element) (argumentos)
L_Full.insert(3,"bring")
print(L_Full)

#   Removendo Elementos
#   ##  del var_var[indice_Elemento]
del L_Full[3]
print(L_Full)

#   ## pop() - remove o último item de uma lista, mas permite que você trabalhe com o valor do item após remoção
last = L_Full.pop()
print(L_Full)
print(last)

#Reinsert
L_Full.insert(2,last)
print(L_Full)

#   ## pop(indice_position)
last = L_Full.pop(0)
print(L_Full)

#   ## remove(value) - remove o item de acordo com seu valor
L_Full = L_Full.remove('i1e2')
print(L_Full)


print("LineBy_")