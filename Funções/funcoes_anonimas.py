soma_anonima = lambda *args: sum(args)
print(soma_anonima(1,2,3,4,5))

print('-'*100)

soma_dicionario = lambda **kwargs: sum(kwargs.values())
print(soma_dicionario(x=1,y=2,z=3))

print('-'*100)
condicao_anonima =  lambda x,y:x+y if y%2==0 else x*y
print(condicao_anonima(3,5))

print('-'*100)
nomes = ["Ana","Gabriel","Christian"]
string_anonima = lambda nomes: [''.join(['*' if j in "aeiouAEIOU" else j for j in n])for n in nomes]
print(string_anonima(nomes))