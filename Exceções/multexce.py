class NumeroNegativoError(Exception):
    pass

while True:
    try:
        s= input()
        z = int(s)
        if z <0:
            raise NumeroNegativoError("O valor não pode ser negativo")
        x = 5/z
        print(x)
        print("Programa finalizado")
        break
    except ZeroDivisionError as zde:
        print("Não é possivel dividir por zero")
    except ValueError as ve:
        print("Entrada Incorreta")
    except EOFError:
        print("Programa interrompido")
        break


