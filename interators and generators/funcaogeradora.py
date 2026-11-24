def imprime():
    print('Linha 1')
    yield 1
    print('Linha 2')
    yield 2
    print('Linha 3')
    yield 3

print(next(imprime()))

print('-'*100)

def funcgeradora():
    for i in range(10):
        yield i
numeros = funcgeradora()
while True:
    try:
        print(next(numeros))
    except :
        break