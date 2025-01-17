#1 - Abrir o sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pyautogui.hotkey - duas teclas ao mesmo tempo
# pyautogui - automação

import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press("win")

pyautogui.write("egde")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

pyautogui.press("enter")
time.sleep(3)

#2 - Fazer login

pyautogui.click(x=741, y=503)
pyautogui.write("pythonimpressionador@gmail.com")

pyautogui.press("tab")
pyautogui.write("minha senha aqui")

pyautogui.press("tab")
pyautogui.press("enter")

#3 - Importar a base de dados dos produtos
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

#4 - Cadastrar 1 produto

for linha in tabela.index:
    pyautogui.click(x=849, y=349)

    #Codigo
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    #Marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    #Tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    #Categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    #Preco_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #Custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #Observacao
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    #Numero positivo = scroll para cima
    #Numero negativo = scroll para baixo

    pyautogui.scroll(10000000)

#5 - Repetir o passo 4 até acabar todos os produtos
# Resolução acima