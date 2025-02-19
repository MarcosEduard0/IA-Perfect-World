import re
import time
import ctypes  # Para criar janelas de aviso
import pyautogui
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import pytesseract as ocr
import sys
import keyboard

sys.path.append("../../")

import utils.function as f

# Configuração do caminho do executável Tesseract
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
ocr.pytesseract.tesseract_cmd = TESSERACT_PATH


def capturar_adds(bounding_box):
    """
    Captura a área de tela definida por bounding_box (x1, y1, x2, y2),
    retorna a imagem recortada.
    """
    screenshot = pyautogui.screenshot()
    cropped_img = screenshot.crop(bounding_box)
    return cropped_img


def ler_texto_ocr(imagem, lang="por"):
    """
    Lê o texto de uma imagem usando Tesseract OCR, com alguns pré-processamentos.
    """
    # 1. Converter para tons de cinza
    img_gray = imagem.convert("L")

    # 2. Ajustar brilho/contraste (opcional, teste para ver se melhora)
    enhancer = ImageEnhance.Contrast(img_gray)
    img_contrasted = enhancer.enhance(2.0)  # Ajuste o valor se desejar

    # 3. Aplicar um filtro de nitidez (opcional)
    img_sharp = img_contrasted.filter(ImageFilter.SHARPEN)

    # 4. Inverter (negativo) se for necessário mesmo
    #    Isso pode ou não ajudar, dependendo da cor de fundo e do texto
    img_invertida = ImageOps.invert(img_sharp)

    # 5. Tentar extrair o texto
    texto_extraido = ocr.image_to_string(img_invertida, lang=lang)

    return texto_extraido


def obter_quantidade_tempo_adds(imagem):
    """
    Extrai o texto da imagem e conta ocorrências de atributos esperados.
    """
    adds = {
        "Defesa_1": 0,
        "Defesa_2": 0,
        "Ataque_1": 0,
        "Ataque_2": 0,
        "AtqM": 0,
        "Constituição": 0,
        "Inteligência": 0,
    }

    texto_adds = ler_texto_ocr(imagem, lang="por").strip()
    print(texto_adds)  # Para depuração

    # Lista de atributos a serem contados no OCR
    padroes = {
        "Defesa_1": ["Defesa +1"],
        "Defesa_2": ["Defesa +2"],
        "Ataque_1": ["Ataque +1", "Afaque +1"],
        "Ataque_2": ["Ataque +2", "Afaque +2"],
        "AtqM": ["AtqM", "AtqU", "AtM", "AtgM"],
        "Constituição": ["Constituição", "Constitução"],
        "Inteligência": ["Intelgência", "Inteligência", "Inteigência"],
        "Forca": ["Força", "Forca"],
        "Destreza": ["Destreza", "Destreza"],
    }

    # Conta as ocorrências de cada atributo na imagem processada
    for chave, palavras in padroes.items():
        adds[chave] = sum(texto_adds.count(palavra) for palavra in palavras)

    return adds


f.ShowWindow("Perfect World - Rate Media: Jornada ao Oeste")
pyautogui.sleep(1)

# Lista de possíveis caminhos para o botão
botao_paths = [
    r"..\..\includes\1920x1080\botaoGravar.png",
    r"..\..\includes\1920x1080\botaoGravar1.png",
]

BotaoGravar = None

for path in botao_paths:
    try:
        BotaoGravar = f.LocateButton(path)
        if BotaoGravar:  # Se encontrou, interrompe o loop
            break
    except Exception as e:
        print(f"Erro ao tentar localizar {path}: {e}")  # Debug opcional


while True:
    LocateAnel = pyautogui.locateCenterOnScreen(
        r"..\..\includes\1920x1080\anel2.png", confidence=0.8
    )

    pyautogui.rightClick(LocateAnel[0], LocateAnel[1])
    pyautogui.leftClick(BotaoGravar[0], BotaoGravar[1])
    pyautogui.moveTo(LocateAnel[0], LocateAnel[1])
    pyautogui.sleep(1.5)
    msg_moeda_prata = pyautogui.locateOnScreen(
        r"..\..\includes\1920x1080\moeda_prata.png", confidence=0.8
    )

    # Ajusta área a ser capturada
    area_adds = (
        msg_moeda_prata[0] - 63,
        msg_moeda_prata[1] + 18,
        msg_moeda_prata[0] + 48,
        msg_moeda_prata[1] + 86,
    )
    img_cortada = capturar_adds(area_adds)
    # img_cortada.show()
    pyautogui.moveTo(BotaoGravar[0], BotaoGravar[1])

    # Extrai a contagem de "Tempo" (ou seja lá o que vc estiver procurando)
    atributos = obter_quantidade_tempo_adds(img_cortada)
    print(atributos)

    if atributos["Defesa_2"] >= 2:
        exit()
