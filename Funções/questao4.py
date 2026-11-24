for i in range(6):
    numeros = list(map(int,input().split()))
# numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(6)]

filtrados = filter(lambda x: len(str(abs(x)))>2, numeros)
print(filtrados)