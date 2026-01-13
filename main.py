import pyautogui
import pandas as pd
import time

#importar a base de produtos
tabela = pd.read_csv("produtos.csv")
# print(tabela)

# URL da página de login que será acessada pelo código
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# 3 comandos usados da biblioteca pyautogui:    
# Pyautogui.press - Serve para pressionar uma tecla do seu teclado
# Pyautogui.write - Serve para escrever com o teclado (como se fosse você digitando)
# Pyautogui.click - Serve para clicar com o mouse

# define o tempo de espera entre os comandos do Pyautogui
pyautogui.PAUSE = 1

# abrir sistema (no nosso caso o chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

# espera carregar
time.sleep(3)

# fazer login (aqui pode preencher com qualquer dado de login)
pyautogui.click(x=649, y=468)
pyautogui.write("dalessandro@gmail.com")
pyautogui.press("tab")
pyautogui.write("InterMelhorDoSul")
pyautogui.press("tab")
pyautogui.press("enter")

# aqui precisamos percorrer as linhas da tabela
# para cada linha vamos cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=651, y=322) # clica no 1° campo
    pyautogui.write(str(tabela.loc[linha, "codigo"])) # pega o código da tabela e escreve no campo
    pyautogui.press("tab") # passa pro proximo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab") 
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]): # verifica se existe informação em obs, caso contrario não preenche
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000) 
 
