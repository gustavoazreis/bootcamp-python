import csv

def ler_csv(nome_do_arquivo: str) -> list[dict]:
    """
    Função que lê um arquivo csv e retorna um dicionário.
    """
    dados = []
    with open (nome_do_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            dados.append(linha)
    return dados

def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    """
    Função que filtra produtos onde entregue = True.
    """
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados

def somar_valores_dos_produtos(lista_com_produtos_filtrados: list[dict]) -> int:
    """
    Função que soma todos os produtos na lista.
    """
    valor_total = 0
    for produto in lista_com_produtos_filtrados:
        valor_total += int(produto.get("price"))
    return valor_total
