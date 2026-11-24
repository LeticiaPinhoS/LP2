lista = ['Ana','Gabriel','Carlos']

lista_iterador = enumerate(lista)  #retorna um iterador

print(lista_iterador)
print(next(lista_iterador))

for indice,conteudo in lista_iterador:
    print(indice, conteudo)
