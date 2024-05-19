import time
import pyautogui
import pandas as pd

tabela = pd.read_csv(r"D:\codes\automacao\lista_de_produtos.csv")
pyautogui.PAUSE = 2

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.click(x=513, y=464)

time.sleep(2)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=671, y=386)
pyautogui.write("TestOne@gmail.com")
pyautogui.press("tab")
pyautogui.write("keyTest")
pyautogui.press("tab")
pyautogui.press("enter")

for linha in tabela.index:

    pyautogui.click(x=556, y=274)
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

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
   
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    else:
        pyautogui.write("NULL")
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    pyautogui.scroll(5000)

