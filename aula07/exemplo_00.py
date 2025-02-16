def soma(valor_1_para_somar: float, valor_2_para_somar: float) -> float:
    """
    Uma função simples de soma de valores do tipo float que retorna float.
    """
    resultado_da_soma = valor_1_para_somar + valor_2_para_somar
    return resultado_da_soma

valor_1 = int(input("Digite um valor: "))
valor_2 = int(input("Digite outro valor para ser somado: "))

valor_3 = soma(valor_1, valor_2)

print(valor_3)