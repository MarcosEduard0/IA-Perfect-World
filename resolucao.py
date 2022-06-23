import ctypes
import pyautogui 

arquivo = open('systemsettings.ini', 'r') 

resolucao = pyautogui.size()
print("Width =", resolucao[0])
print("Height =", resolucao[1])

Width = resolucao[0] 
Height = resolucao[1] 

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