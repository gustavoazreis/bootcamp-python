# Dúvida isinstance

is_nome_aluno: bool = False

while is_nome_aluno is not True:
    idade_do_aluno = int(input('Digite uma classe: '))
    if isinstance(nome_aluno, str):
        nome_aluno_maiusculo = nome_aluno.upper()
        print(nome_aluno_maiusculo)
        is_nome_aluno = True
    else:
        print("Você digitou uma classe errada, precisa ser str")