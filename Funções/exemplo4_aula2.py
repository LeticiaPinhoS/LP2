def soma(*args):
    resultado = 0
    for i in args:
        resultado += i
    return resultado

entrada= list(map(int,input().split()))
print(soma(*entrada))