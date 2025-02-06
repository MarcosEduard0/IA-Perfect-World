import re
import time
import ctypes  # Para criar janelas de aviso
import pyautogui
from PIL import ImageOps, ImageEnhance, ImageFilter
import pytesseract as ocr
import sys

sys.path.append("../../")

import utils.function as f


# Configuração do caminho do executável Tesseract
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
ocr.pytesseract.tesseract_cmd = TESSERACT_PATH


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


def capturar_adds(bounding_box):
    """
    Captura a área de tela definida por bounding_box (x1, y1, x2, y2),
    retorna a imagem recortada.
    """
    screenshot = pyautogui.screenshot()
    cropped_img = screenshot.crop(bounding_box)
    return cropped_img


def obter_quantidade_adds(imagem):
    """
    Extrai o texto da imagem (usando a função de OCR),
    faz o split para identificar quantos 'Tempo' aparecem
    e retorna a contagem.
    """
    texto_adds = ler_texto_ocr(imagem, lang="por")
    palavras = re.split(
        r"[^0-9A-Za-zÁ-ú]+", texto_adds
    )  # incluí Acentos de modo simplificado
    print(palavras)
    total_atqm = palavras.count("AtaM") + palavras.count("AtqM") + palavras.count("AtM")
    total_espirito = palavras.count("Espírito") + palavras.count("Espíritu") + palavras.count("Espirito") + palavras.count("Espiritu")
    total_penetracao = palavras.count("Mágica") + palavras.count("Magica")

    return total_atqm, total_espirito, total_penetracao


def main():
    # Tenta trazer a janela do Perfect World para o primeiro plano
    f.ShowWindow("Perfect World - Rate Media: Jornada ao Oeste")

    # Localiza o botão Reproduzir
    botao_reproduzir = f.LocateButton(
        r"..\..\includes\1920x1080\botaoIniciarAstrolabioAtivo.png",
        r"..\..\includes\1920x1080\botaoIniciarAstrolabioDesativado.png",
    )
    if not botao_reproduzir:
        ctypes.windll.user32.MessageBoxW(
            0, "Não foi possível localizar o botão 'Iniciar Hoposcopo'.", "Erro", 0
        )
        return

    # Ajusta área a ser capturada
    area_adds = (
        botao_reproduzir[0] + 170,
        botao_reproduzir[1] - 410,
        botao_reproduzir[0] + 325,
        botao_reproduzir[1] - 60,
    )

    # Clica em reproduzir
    pyautogui.click(botao_reproduzir[0], botao_reproduzir[1])
    time.sleep(0.5)  # Espera forjar o item (ajuste se precisar mais/menos)

    while True:
        # Captura a área de tela
        img_cortada = capturar_adds(area_adds)

        # Extrai a contagem de "Tempo" (ou seja lá o que vc estiver procurando)
        total_atqm, total_espirito, total_penetracao = obter_quantidade_adds(
            img_cortada
        )
        print(
            f"Ataque Magico: {total_atqm} Espirito: {total_espirito} Penetracao Magica: {total_penetracao}"
        )

        if sum([total_atqm, total_espirito, total_penetracao]) >= 6:
            # Se já atendeu a condição, segura o novo add
            pyautogui.click(botao_reproduzir[0] + 155, botao_reproduzir[1] - 15)
            pyautogui.alert(
                text=(
                    f"Parabéns, conseguimos uma astrolábio com {total_atqm}-{total_espirito}-{total_penetracao}"
                    f"Ataque Magico: {total_atqm} Espirito: {total_espirito} Penetracao Magica: {total_penetracao}"
                ),
                title="I.A do John",
                button="Obrigado",
            )
        else:
            print("clique")
            pyautogui.click(botao_reproduzir)
            time.sleep(0.5)


if __name__ == "__main__":
    main()
