# #### try-except e if

# 21: Conversor de Temperatura
#try:
#    celsius = float(input("Digite a temperautra em Celsius: "))
#    fahrenheit = (celsius * 9/5) + 32
#    print(f"{celsius}ºC é igual a {fahrenheit}ºF.")
#except ValueError:
#    print("Porfavor, digite um número válido para a temperatura.")

# 22: Verificador de Palíndromo
#entrada = input ("Digite uma palavra ou frase: ")
#if isinstance(entrada, str):
#    formatado = entrada.replace(" ", "").lower()
#   if formatado == formatado[::-1]:
#        print("É um palíndromo.")
#    else:
#        print("Não é um palíndromo.")
#else:
#    print("Entrada inválida. Por favor, digite uma palavra ou frase.")

# 23: Calculadora Simples
#try:
#    num1 = float(input("Digite o primeiro número: "))
#    num2 = float(input("Digite o segundo número: "))
#    operador = input("Digite o operador (+, -, *, /): ")
#    if operador == "+":
#        resultado = num1 + num2
#    elif operador == "-":
#        resultado = num1 + num2
#    elif operador == "*":
#        resultado = num1 * num2
#    elif operador == "/" and num2 != 0:
#        resultado = num1 / num2
#    else:
#        print("Operador inválido ou divisão por zero")
#    print(f"Resultado: {resultado}")
#except ValueError:
#    print("Erro: Entrada inválida. Certifique-se de inserir números.")

# 24: Classificador de Números
#try:
#    numero = int(input("Digite um número: "))
#    if numero > 0:
#        print("Positivo")
#    elif numero < 0:
#        print("Negativo")
#    else:
#        print("Zero")
#    if numero % 2 == 0:
#        print("Par")
#    else:
#        print("Ímpar")
#except ValueError:
#    print("Por favor, digite um número inteiro válido.")

# 25: Conversão de Tipo com Validação
#entrada_lista = input("Digite uma lista de números separados por vírgula: ")
#numeros_str = entrada_lista.split(",")
#numeros_int = []
#try:
#    for num in numeros_str:
#        numeros_int.append(int(num.strip()))
#    print(f"Lista de inteiros: {numeros_int}")
#except ValueError:
#    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")
