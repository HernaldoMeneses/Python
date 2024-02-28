'''
    **** Strings
        - Tipo de dado primitivo.
        - Várias Funcionalidades.
        - Em Python são caracterizadas por "" ou '' ou 3 '.

    **** Hands on
        - Algumas formas de utilizar strings
            - 1 Alterando a Exibição da String com métodos 
            - 2 Concatenando Strings
            - 3 Espaços em branco e quebras de linha
            - 4 Strings com apóstofres

'''

# Tópico 1 - Alterando a Exibição da String com métodos 

name = "hernaldo meneses" # Seja name igual à string 
print(name) # Exiba a o valor contido na variável name
print(name.title()) # Exiba a o valor contido na variável name com a primeira leta maiuscula
print(name.lower()) # Exiba toda string contida na variável name com letras minusculas
print(name.upper()) # Todas as letras maiúsculas
print(name)

# Tópico 2 - Concatenando Strings 

base = " - Nome: "
print(base + name) # Exiba a o valor contido na variável name
print((base + name).title()) # Exiba a o valor contido na variável name com a primeira leta maiuscula
print((base + name).lower()) # Exiba toda string contida na variável name com letras minusculas
print((base + name).upper()) # Todas as letras maiúsculas
print((base + name))

stg_concat = " - Nome: " + name
print(stg_concat)

stg_concat = " - Nome: " + name.title()
print(stg_concat)

stg_concat2 = " - Nome: " + "hernaldo meneses"
print(stg_concat2)

# Tópico 3 - Espaços em branco e quebras de linha
info_sms = '''
    Caracteres Sepeciais que marcam tabulações e quebras de linha
        - \\t - Tabulação
        - \\n - Quebra de linha

'''
print(info_sms)
print(name.title())
print("\t" + name.title())
print("\t" + stg_concat.title())
print("\t" + name.title() + "\n")
print("\t" + stg_concat.title())

_stg_space = '                     space left'
stg_space_ = 'space rigth                    '
_stg_space_ = '       space rigth            '

print(_stg_space)
print(_stg_space.lstrip())
print(_stg_space_.rstrip())
print(_stg_space_.rstrip().lstrip())
print(_stg_space_.strip())


# Tópico 4 - strings com apóstofre
stg_apostofre = "It's my string"
print(stg_apostofre)