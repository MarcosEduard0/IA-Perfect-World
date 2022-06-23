import pyautogui #Biblioteca automação
import function as f
import PIL
import pytesseract as ocr
import re
import time
import datetime
import os

arquivo = r'log.txt'

if os.path.exists(arquivo) == False:
    arquivo = open('log.txt', 'w') # Abra o arquivo (leitura)
    arquivo.close()

arquivo = open('log.txt', 'r')

conteudo = arquivo.readlines()

ini = time.time()
time.sleep(2)
fim = time.time()
total = fim - ini

f.HorarioAtual()
f.TempoGasto(total)

conteudo.append('Item: Peito def'+
                '\nTempo gasto: '+str(f.TempoGasto(total))+
                '\nPego as: '+ str(f.HorarioAtual()) +                
                '\nQuant. reforjas: 5161'+
                '\nQuant. reliquia usada: 548153\n\n')

arquivo = open('log.txt', 'w') # Abre novamente o arquivo (escrita)
arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.

arquivo.close()