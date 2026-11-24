import sys
while True:
    try:
        x = int(input())
        print(x)
        print("Programa finalizado com sucesso!")
        break
    except ValueError as vae:
        print("Entrada Incorreta")
        # print(vae.__traceback__)
        # print(f"Erro: {sys.exc_info()[1]}")