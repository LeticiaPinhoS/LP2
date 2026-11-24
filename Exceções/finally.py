
while True:
    try:
        s = input()
        x = int(s)

        print("Programa finalizado com sucesso!")
        break
    except ValueError as vae:
        print("Entrada Incorreta")
        # print(vae.__traceback__)
        # print(f"Erro: {sys.exc_info()[1]}")
    finally:
        print(f"O valor digitado foi {x}")