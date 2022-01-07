# Utilização do Logging
import logging

"""
Niveis de logging
debug - Só estou informando informaçoes para desenvolvedores
info - Só quero informar algo que esta acontecendo no programa, mas não é um erro
warning - Quero alertar algo que esta acontecendo fora do esperado, porem ainda não é um erro, mas pode gerar futuramente
error - Um erro ocorreu na aplicação
critical - Um erro com consequencias graves acaba de acontecer na aplicação
"""
logging.basicConfig(
    level=logging.DEBUG,
    filename="app.log",
    filemode="a",
    format="%(levelname)s = %(message)s",
)  # Setar o nivel
logging.debug("Logging no nivel debug")
logging.info("Logging no nivel info")
logging.warning("Logging no nivel warning")
logging.error("Logging no nivel error")
logging.critical("Logging nivel critical")
