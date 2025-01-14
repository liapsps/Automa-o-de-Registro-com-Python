# pseudocódigo
    # passo 1: abrir o sistema da empresa (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
    # passo 2: fazer login
    # passo 3: pegar base de dados dos produtos
    # passo 4: cadastrar 1 produto
    # passo 5: repetir o passo 4 até acabar os produtos

# em python
    # pip install pyautogui

import pyautogui # serve pra automatizar qualquer tarefa que envolva interações com a UI
import time

pyautogui.PAUSE = 1 # a cada comando, ele espera xseg

# pyautogui.click -> clicar 

# pyautogui.press -> pressionar uma tecla
# pyautogui.write -> escrever
# pyautogui.hotkey -> atalho de teclado (ex: ctrl C)

# passo 1: abrir o sistema da empresa

# abrir o google chrome
pyautogui.press("win")  # aperta a tecla win "Windows"

# digitar o texto chrome
pyautogui.write("chrome")

# apertar enter
pyautogui.press("enter")

# clicar no meu perfil do chrome
pyautogui.click(x=346, y=633)

# entrar no link do sistema da empresa
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# pedir pro computador esperar 3 segundos
time.sleep(3)

# passo 2: fazer login
pyautogui.click(x=490, y=376)
pyautogui.write("emailficticio@gmail.com")

pyautogui.click(x=424, y=476) # passa para o campo da senha
pyautogui.write("senhaficticia123")

pyautogui.press("tab") # passa para o botão "logar"
pyautogui.press("enter")

# passo 3: pegar base de dados dos produtos
    # pip install pandas openpyxl

import pandas # fornece ferramentas para anális e manipulação de dados

tabela = pandas.read_csv("produtos.csv")

print(tabela)

time.sleep(2)

# passo 4: cadastrar 1 produto
for linha in tabela.index:
    pyautogui.click(x=523, y=257) # clica no 1° campo
    pyautogui.hotkey('ctrl', 'a') # seleciona o texto para substituir, quando houver um no lugar

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab") # passa para o próximo campo

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab") # passa para o próximo campo

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab") # passa para o próximo campo

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab") # passa para o próximo campo

    # preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab") # passa para o próximo campo

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab") # passa para o próximo campo

    # obs
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
            pyautogui.write(str(obs))

    pyautogui.press("tab") # passa para o próximo campo
    pyautogui.press("enter") # aperta o botão de enviar
    pyautogui.scroll(10000)

# passo 5: repetir o passo 4 até acabar os produtos
 