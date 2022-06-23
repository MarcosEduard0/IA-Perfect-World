import ctypes
import pyautogui #Biblioteca automação

arquivo = open('systemsettings.ini', 'r') #Abrindo o arquivo para leitura

resolucao = pyautogui.size()
print("Width =", resolucao[0])
print("Height =", resolucao[1])

Width = resolucao[0] #pegando a o tamanho da largura da tela
Height = resolucao[1] #pegando a o tamanho da altura da tela

linha = [] #Lista para ler o arquivo

for i in range(58): #Total de linhas no arquivo

    if i == 23: #Quando chegar na linha da resolução, ira apagar e adicionar a nova resolução
        aux = arquivo.readline() #apagando linha antiga
        aux = arquivo.readline() 
        linha.append('RenderWid = ' + str(Width) + '\n') #adicionando linha nova
        linha.append('RenderHei = ' + str(Height) + '\n') 
    
    else:
        linha.append(arquivo.readline()) #conitnuando a ler o arquivo
    

arquivo = open('systemsettings.ini', 'w') #Abrindo o arquivo para escrita
arquivo.writelines(linha) #Escrevendo no arquivo

arquivo.close() #Fechando o arquivo
arquivo.close()


'''RenderWid = 1916
RenderHei = 1008
58'''