import pyautogui
import pandas
import time

## Abrir o endge
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')

## Digitar o Site
time.sleep(0.8)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

## Logar no Site    Garmin  Relogio 1   440.0   96.8    nan

time.sleep(1)
pyautogui.click(x=731, y=391)
pyautogui.write('teste@gmail.com')
pyautogui.press('tab')
pyautogui.write('testeA')
time.sleep(0.5)
pyautogui.press('enter')

#preenchendo o banco de dados 
time.sleep(0.8)
pyautogui.click(x=920, y=278)

#importar banco de dados
tabela = pandas.read_csv('produtos.csv')
print(tabela)

linha = 0

#funcao para repetir processo ate acabar o banco de dados
for linha in tabela.index:

    #codigo do produto
    codigo = tabela.loc[linha,'codigo'] 

    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    #Marca do Produto
    marca = tabela.loc[linha,'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    #Tipo do Produto
    tipo = tabela.loc[linha,'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    #Categoria do Produto
    categoria = tabela.loc[linha,'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    #Preço Unitário do Produto
    preco = tabela.loc[linha,'preco_unitario']
    pyautogui.write(str(preco))
    pyautogui.press('tab')


    #Custo do Produto
    custo = tabela.loc[linha,'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')


    #OBS
    obs = tabela.loc[linha,'obs']
    pyautogui.write(str(obs))

    #enviar o produto
    pyautogui.press('enter')

    #voltar des do começo da tela
    pyautogui.scroll(200)
    pyautogui.click(x=920, y=278)





