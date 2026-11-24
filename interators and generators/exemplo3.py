numeros = [1,2,3,4,5,6,7,8,9,10]
#Função geradora quadrados
quadrados = (i**i for i in numeros)
print(quadrados)
x = zip(numeros,quadrados)
for i in x:
    print(i)