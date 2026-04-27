from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import pandas as pd

navegador = opcoesSelenium.Chrome()
navegador.get("https://www.mercadolivre.com.br/")
pyautogui.sleep(3)
navegador.find_element(By.CLASS_NAME,"nav-search-input").send_keys("notebook" + Keys.ENTER)
pyautogui.sleep(3)

dataFrame = []

listaProdutos = navegador.find_elements(By.CLASS_NAME, "poly-card__content")

for item in listaProdutos:

    nomeProduto = ""
    precoProduto = ""
    urlProduto = ""

    if nomeProduto == "":
        try:
            nomeProduto = item.find_element(By.CLASS_NAME, "poly-component__title").text
        except Exception:
            pass

    if precoProduto == "":
        try:
            precoProduto = item.find_element(By.CLASS_NAME, "poly-component__price").text
        except Exception:
            pass

    if urlProduto == "":
        try:
            urlProduto = item.find_element(By.TAG_NAME, "a").get_attribute("href")
        except Exception:
            pass

    dataFrame.append({"Nome": nomeProduto,"Preco": precoProduto,"url": urlProduto})

df = pd.DataFrame(dataFrame)
df.to_excel("notebooks.xlsx", index=False)

print("Pronto!")
