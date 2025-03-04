import pandas as pd
import os
import glob

# Função de Extract que lê e consolida os jsons

def extrair_dados_e_consolidar(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path,'*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index = True)
    return df_total

# Função que transforma

def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

# Função que da load em csv ou parquet


def carregar_dados(df: pd.DataFrame, format_saida: list):
    """
    Parametro que vai ser ou "csv" ou "parquet" ou "os dois"
    """

    for formato in format_saida:
        if formato == "csv":
            df.to_csv("dados.csv")
        if formato == "parquet":
            df.to_parquet("dados.parquet")

# Função consolidada para chamar a pipeline

def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados_e_consolidar(pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida)

# Teste

if __name__ == "__main__":
    pasta: str = 'data'
    data_frame = extrair_dados_e_consolidar(pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    formato_saida: list = ["csv","parquet"]
    carregar_dados(data_frame_calculado, formato_saida)