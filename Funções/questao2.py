def dadosPessoais(**kwargs):
    if "Nome" in kwargs:
        print("Nome: ", kwargs["Nome"])
    if "Idade" in kwargs:
        print("Idade: ", kwargs["Idade"])

    if "Nome" in kwargs or "Idade" in kwargs:
        print()

dadosPessoais(
    Nome='Júnior',
    Sobrenome='Limeira',
    Idade=29,
    Profissao='Professor'
)