# global x
x = 5
def muda_e_imprime():
    # global x
    x = 7
    print(f"Valor de x dentro da função {x}")

print(f'O valor antes da função:  {x}')
muda_e_imprime()  #Executando a função
print(f'O valor de x depois da função: {x}')