import sys
while True:
    try:
        x = int(input())
        print(x)
        break
    except:
        print(f"Erro: {sys.exc_info()[1]}")