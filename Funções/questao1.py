from functools import reduce


def multiplicacao(*args):
    r = 1
    for i in args:
        r *= i
    return r

print(multiplicacao(1,2,3,4,5))

print("-"*100)
print("------------ Usando reduce() ---------------")

multi_anonima = lambda *args: reduce(lambda x, y: x * y, args)
print(multi_anonima(1,2,3,4,5))
    