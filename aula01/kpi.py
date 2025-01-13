print("-="*10,"CALCULADORA DE BÔNUS SALARIAL","-="*10)
nome = str(input("Digite seu nome: "))
salario = float(input("Digite o valor do seu salário bruto: "))
atingimento = float(input("Digite o percentual de atingimento do bônus:"))

KPI = 1000 + salario * atingimento

print(f"Olá {nome}, o valor do seu bônus este ano foi de R${KPI:.2f}.")
print("-="*10,"ENCERRANDO PROGRAMA","-="*10)    
