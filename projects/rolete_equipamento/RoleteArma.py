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


def obter_quantidade_tempo_adds(imagem):
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
    adds = {}
    adds["Tempo"] = palavras.count("Tempo")
    adds["Defesa"] = palavras.count("Defesa")

    return adds


def main():
    # Entrada de dados
    while True:
        try:
            qtd_adds = int(
                input("Quantos adds de Redução Defesa Fisica você quer (1 a 4)?\n> ")
            )
            if 1 <= qtd_adds <= 4:
                break
            else:
                print("Valor inválido. Digite um número de 1 a 4.\n")
        except ValueError:
            print("Valor inválido. Por favor, insira um número inteiro.\n")

    while True:
        try:
            qtd_esculturas = int(
                input("Quantas 'Escultura da Reforja' você possui?\n> ")
            )
            break
        except ValueError:
            print("Valor inválido. Por favor, insira um número inteiro.\n")

    # Número máximo de tentativas (rolete)
    rolete = qtd_esculturas // 2  # Dividir por 2, como no seu código original
    tentativas_feitas = 0

    # Tenta trazer a janela do Perfect World para o primeiro plano
    f.ShowWindow("Perfect World - Rate Media: Jornada ao Oeste")

    # Localiza o botão Reproduzir
    botao_reproduzir = f.LocateButton(r"..\..\includes\1920x1080\botaoReproduzirOn.png")
    if not botao_reproduzir:
        ctypes.windll.user32.MessageBoxW(
            0, "Não foi possível localizar o botão 'Reproduzir'.", "Erro", 0
        )
        return

    # Ajusta área a ser capturada
    area_adds = (
        botao_reproduzir[0] + 65,
        botao_reproduzir[1] - 170,
        botao_reproduzir[0] + 215,
        botao_reproduzir[1] - 55,
    )
    while tentativas_feitas <= rolete:

        if keyboard.is_pressed("ctrl+c"):
            print("\nLoop interrompido pelo usuário.")
            break

        # Clica em reproduzir
        pyautogui.click(botao_reproduzir[0], botao_reproduzir[1])
        time.sleep(1.5)  # Espera forjar o item (ajuste se precisar mais/menos)

        # Captura a área de tela
        img_cortada = capturar_adds(area_adds)

        # Extrai a contagem de "Tempo" (ou seja lá o que vc estiver procurando)
        atributos = obter_quantidade_tempo_adds(img_cortada)

        # print(
        #     f"Tentativa {tentativas_feitas+1}: {atributos["Red_Fisico"]} add(s) de Redução de Dano Físico",
        # )

        if atributos["Defesa"] >= qtd_adds:
            # Se já atendeu a condição, segura o novo add
            pyautogui.click(botao_reproduzir[0] + 155, botao_reproduzir[1] - 15)
            pyautogui.alert(
                text=(
                    f"Parabéns, conseguimos uma parte do set com "
                    f"{atributos["Defesa"]} add(s) de Nível Defesa!"
                ),
                title="I.A do John",
                button="Obrigado",
            )
            break

        elif atributos["Tempo"] >= qtd_adds:
            # Se já atendeu a condição, segura o novo add
            pyautogui.click(botao_reproduzir[0] + 155, botao_reproduzir[1] - 15)
            pyautogui.alert(
                text=(
                    f"Parabéns, conseguimos uma parte do set com "
                    f"{atributos["Tempo"]} add(s) de Invocação!"
                ),
                title="I.A do John",
                button="Obrigado",
            )
            break
        else:
            # Mantém o antigo add
            pyautogui.click(botao_reproduzir[0] - 170, botao_reproduzir[1] - 15)
            time.sleep(1.5)

        tentativas_feitas += 1

    # Se terminou o while sem encontrar, exibe mensagem
    if tentativas_feitas > rolete:
        pyautogui.alert(
            text="As tentativas acabaram e não foi possível obter a quantidade de adds desejada.",
            title="I.A do John",
            button="Ok",
        )


if __name__ == "__main__":
    main()
