print("-="*10,"CALCULADORA DE BÔNUS SALARIAL","-="*10)

# Solicitação ao usuário para input do nome
try:
    nome = str(input("Digite seu nome: "))
    # Check se o nome está vazio
    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio.")
    # Check se tem números no nome
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")
    else:
        print(f"Nome válido: {nome}")
except ValueError as e:
    print(e)

# Solicitação ao usuário para input do salário
try:
    salario = float(input("Digite o valor do seu salário bruto: "))
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")

# Solicita ao usuário que digite o valor do bônus recebido
try:
    bonus_recebido = float(input("Digite o valor do bônus recebido: "))
    if bonus_recebido < 0:
        print("Por favor, digite um valor positivo para o bônus.")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número")  

atingimento = float(input("Digite o percentual de atingimento do bônus:"))

#lógica de cálculo
bonus_final = bonus_recebido * 1.2
KPI = (salario + bonus_final)/1000

print(f"Olá {nome}, o valor do seu bônus este ano foi de R${KPI:.2f}.")
print("-="*10,"ENCERRANDO PROGRAMA","-="*10)    
