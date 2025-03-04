from loguru import logger
from sys import stderr
from functools import wraps

logger.remove()

# Config do logger para exibir logs no stderr e salvar em arquivo, com filtragem e formatação específicas
logger.add(
    sink = stderr,
    format = "{time} <r>{level}</r> <g>{message}</g> {file}",
    level = "INFO"
)

logger.add(
    "meu_arquivo_de_logs.log", # Arquivo onde os logs serão salvos
    format = "{time} {level} {message} {file}",
    level = "INFO"
)

logger.add(
    "meu_arquivo_de_logs_critical.log", # Arquivo onde os logs serão salvos
    format = "{time} {level} {message} {file}",
    level = "ERROR"
)

# Exemplo de uso
logger.info("Este é um log de informação.")
logger.error("Este é um log de erro.")