#Pecorrendo todos itens de uma lista com laço for
#For iten in list:
#Identeition matters

magicians = [
    'alice',
    'david',
    'carolina'
    ]

print(magicians)

for i_list in magicians:
    print(i_list)

print("\n")
for i_list in magicians:
    print("\t" + i_list.title())

print("\n")
for i_list in magicians:
    print("\t\tHello, " + i_list.title() + "!")
    print("\t\t\tI can't wait to see your next trick," + i_list.title() +"!")

#continue.. 90/592

#after for loop (recue identation )
print("\t Thanks you, everyone. that was a great magic show! \n") #Wout of For loop

'''
    A importância da  identação e porque ela é forçada na linguagem python
        a identação conecta a linha atual ao codigo da linha anterior (forçando-a)
        facilita a leitura do código
        força a organização lógica

        a identação na linguagem deve ser observada com cuidado
            pode bugar o código
            ou gerar saídas com erros lógicos.

        Python avisará:
            IndentationError: expected an indented block
            IndentationError: unexpected indent
        
        mas em caso de erros lógicos, esse cuidado fica a cargo do programador.

'''

