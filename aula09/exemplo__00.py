from loguru import logger

logger.add("meu_log.log", level = "CRITICAL")

def soma(x,y):
    try:
        soma = x + y
        logger.info(f"parabéns, você digitou valores corretos: {soma}")
        return soma
    except:
        logger.critical("Você deve digitar valores corretos")

print(soma(2,3))