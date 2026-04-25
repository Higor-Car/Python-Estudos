from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui

# Abre uma janela do Chrome controlada pelo Selenium
navegador = opcoesSelenium.Chrome()

# Acessa o site de livros
navegador.get("https://books.toscrape.com/")

# Aguarda 2 segundos para a página carregar completamente
pyautogui.sleep(2)

# Busca todos os elementos com a classe "product_pod" na página
# Cada elemento representa um livro — retorna uma lista com os 20 livros da página
listaProdutos = navegador.find_elements(By.CLASS_NAME, "product_pod")

# Percorre a lista, processando um livro por vez
for item in listaProdutos:

    # Reseta as variáveis a cada iteração para evitar que
    # dados do livro anterior vazem para o próximo
    nomeProduto = ""
    precoProduto = ""

    if nomeProduto == "":
        try:
            # Busca o título dentro do <h3><a> e pega o atributo "title"
            nomeProduto = item.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
        except Exception:
            # Se o elemento não for encontrado, ignora e continua
            pass

    if precoProduto == "":
        try:
            # Busca o elemento com a classe "price_color" e pega o texto visível
            precoProduto = item.find_element(By.CLASS_NAME, "price_color").text
        except Exception:
            # Se o elemento não for encontrado, ignora e continua
            pass

    # Exibe os dados do livro atual
    print(nomeProduto)
    print(precoProduto)
    print("-------")
