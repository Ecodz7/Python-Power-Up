import pyautogui as pa
import time

# LEGENDA
    # pyautogui.write -> escrever um texto
    # pyautogui.press -> apertar 1 tecla
    # pyautogui.click -> clicar em algum lugar da tela
    # pyautogui.hotkey -> combinação de teclas
    # pyautogui.PAUSE -> intervalo de tempo de execução entre os comandos
    # time.sleep -> intervalo de tempo para interromper o código

pa.PAUSE = 0.3

# Passo a passo do Projeto de Automatização de Tarefas (importação de dados em uma tabela e preenchimento automático)
    # Passo 1: Entrar no sistema da empresa (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
        # Abrir o navegador

pa.press ("win")
pa.write ("Chrome")
pa.press ("enter")   

        # Digitar e entrar no site

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pa.write (link)
pa.press ("enter")
time.sleep (3)

        # Preencher login e senha

pa.click (x=2939, y=506)
pa.write ("projetoautomatização@hotmail.com")
pa.press ("tab")
pa.write ("projetoautomatizacao")
pa.press ("tab")
pa.press ("enter")
time.sleep (3)

    # Passo 2: Importação de dados e preenchimento dos campos
        # Importar dados

import pandas as pd 
pd.read_csv("produtos.csv")
tabela = pd.read_csv("produtos.csv")

        # Preencher as informações de cada campo

                #codigo
for linha in tabela.index:
        codigo = str(tabela.loc[linha, "codigo"])
        pa.click (x=2995, y=365)
        pa.write (codigo)
        pa.press ("tab")

                #marca
        pa.write (str(tabela.loc[linha, "marca"]))
        pa.press ("tab")      

                #tipo
        pa.write (str(tabela.loc[linha, "tipo"]))
        pa.press ("tab")

                #categoria
        pa.write (str(tabela.loc[linha, "categoria"]))
        pa.press ("tab")       

                #preço
        pa.write (str(tabela.loc[linha, "preco_unitario"]))
        pa.press ("tab")

                #custo
        pa.write (str(tabela.loc[linha, "custo"]))
        pa.press ("tab")

                #obs
        obs = str(tabela.loc[linha, "obs"])
        if obs != "nan":
                pa.write (obs)
        pa.press ("tab")
        pa.press ("enter")
        time.sleep (2)
        pa.scroll (1000)  


           
        