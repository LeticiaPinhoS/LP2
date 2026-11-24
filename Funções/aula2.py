import random
def misturar_caracteres(s):
    #Processar
    lista = list(s)
    random.shuffle(lista) #Misturando os caracteres
    return ''.join(lista)  #Retornando em formato de string

entrada = input()
resultado = misturar_caracteres(entrada)  #Chamada da função
print(resultado)