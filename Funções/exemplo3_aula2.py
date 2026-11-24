import random

def ordem_crescente(inicio,fim):
    conjunto = set()
    while len(conjunto) < 15:
        aleatorio = random.randint(inicio,fim)
        conjunto.add(aleatorio)
    lista =list(conjunto)

    lista.sort()
    return lista

inicio,fim = map(int, input().split())

print(ordem_crescente(inicio,fim))