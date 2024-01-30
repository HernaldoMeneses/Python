'''
    **** Listas
        - Conceito

    **** Hands on
        - Algumas formas de utilizar Listas
            - Acessar os elementos da listas
            - Ordenação e Posição dos elementos
            - Casos Especiais interessantes

'''

conceito = '''
    Listas em python são uma coleção de itens ordenados
    esta coleção pode conter quaisquer tipo de dado
    inclusive outra lista.

    sua represenção em python é sempre com os ([])
    com os elementos separados por (,)

'''

exemplo = '''    list_exemplo = [iten1, item2, 5, "string", var, 5.6]

    para acessar o 3 elemento dessa lista fazemos o seguinte:

    print(list_exemplo[2])
'''

ordem = '''    a ordem do item desejaso sempre será igual a sua posição - 1
    isso ocorre porque a ordenação sempre inicia com 0

    lista_ordens = [0,1,2,3,...]
    lista_posi__ = [1,2,3,4,...]
'''
    
especial = '''    Casos especiais interessantes
    print(list_exemplo[-1]) #exibe sempre o último da lista
    print(list_exemplo[-2]) #exibe sempre o penúltimo da lista
    print(list_exemplo[-3]) #exibe sempre o antepenúltimo da lista
'''

lista_ = [conceito, exemplo, ordem, especial]

#print(lista_[0])
#print(lista_[1])
#print(lista_[2])
print(lista_[3])