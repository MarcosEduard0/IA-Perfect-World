import re
import time
import ctypes  # Para criar janelas de aviso
import pyautogui
from PIL import ImageOps, ImageEnhance, ImageFilter
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


def log_palavras(palavras, arquivo_log="ocr_log.txt"):
    """Salva as palavras extraídas pelo OCR em um arquivo de log."""
    with open(arquivo_log, "a", encoding="utf-8") as f:
        for palavra in palavras:
            f.write(palavra + "\n")


def obter_quantidade_adds(imagem):
    """
    Extrai o texto da imagem (usando a função de OCR),
    faz o split para identificar quantos 'Tempo' aparecem
    e retorna a contagem.
    """
    texto_adds = ler_texto_ocr(imagem, lang="por")
    texto_adds = texto_adds.replace("Guia", "").replace("Destino", "")
    palavras = re.split(
        r"[^0-9A-Za-zÁ-ú]+", texto_adds
    )  # incluí Acentos de modo simplificado

    # print(palavras)

    # Log das palavras no arquivo de log
    log_palavras(palavras)

    # Contagem específica das palavras relacionadas a ataque
    total_atqm = (
        palavras.count("AtaM")
        + palavras.count("AtqM")
        + palavras.count("AtgM")
        + palavras.count("AtpM")
        + palavras.count("AtM")
    )
    total_penetracao_magica = palavras.count("Mágica") + palavras.count("Magica")

    total_atqf = palavras.count("físico") + palavras.count("fisico")
    total_penetracao_fisica = palavras.count("Física") + palavras.count("Fisica")

    total_espirito = (
        palavras.count("Espírito")
        + palavras.count("Espíritu")
        + palavras.count("Espirito")
        + palavras.count("Espiritu")
    )
    total_def = palavras.count("Def")
    total_defM = palavras.count("DefM")
    total_hp = palavras.count("HP")
    total_elemetos = (
        palavras.count("Madeira")
        + palavras.count("Metal")
        + palavras.count("Fogo")
        + palavras.count("Água")
        + palavras.count("Terra")
    )

    adds = {
        "Ataque Magico": total_atqm,
        "Penetracao Magica": total_penetracao_magica,
        "Ataque Fisico": total_atqf,
        "Penetracao Fisica": total_penetracao_fisica,
        "Espirito": total_espirito,
        "Defesa": total_def - total_elemetos,
        "Defesa Magica": total_defM,
        "HP": total_hp,
    }

    return adds


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
        botao_reproduzir[0] + 327,
        botao_reproduzir[1] - 60,
    )

    # Clica em reproduzir
    pyautogui.click(botao_reproduzir[0], botao_reproduzir[1])
    time.sleep(0.5)  # Espera forjar o item (ajuste se precisar mais/menos)

    while True:
        # Captura a área de tela
        img_cortada = capturar_adds(area_adds)

        # Extrai a contagem de "Tempo" (ou seja lá o que vc estiver procurando)
        atributos = obter_quantidade_adds(img_cortada)
        # print(
        #     f"\nAtaque Magico: {atributos['Ataque Magico']} Espirito: {atributos['Espirito']} Penetracao Magica: {atributos['Penetracao Magica']} Defesa: {atributos['Defesa']}"
        # )
        print(
            f"\nAtaque Magico: {atributos['Ataque Fisico']} Espirito: {atributos['Espirito']} Penetracao Magica: {atributos['Penetracao Fisica']}"
        )

        if keyboard.is_pressed("ctrl+c"):
            print("\nLoop interrompido pelo usuário.")
            break

        # if (
        #     atributos["Ataque Magico"] >= 2
        #     and atributos["Espirito"] >= 2
        #     and atributos["Penetracao Magica"] >= 1
        # ):
        #     # Se já atendeu a condição, segura o novo add
        #     pyautogui.click(botao_reproduzir[0] + 155, botao_reproduzir[1] - 15)
        #     pyautogui.alert(
        #         text=(
        #             f"Parabéns, conseguimos uma astrolábio de ATAQUE com {atributos['Ataque Magico']}-{atributos['Espirito']}-{atributos['Penetracao Magica']}"
        #         ),
        #         title="I.A do John",
        #         button="Obrigado",
        #     )
        #     exit()

        if (
            atributos["Ataque Fisico"] >= 2
            and atributos["Espirito"] >= 2
            and atributos["Penetracao Fisica"] >= 2
        ):
            # Se já atendeu a condição, segura o novo add
            pyautogui.click(botao_reproduzir[0] + 155, botao_reproduzir[1] - 15)
            pyautogui.alert(
                text=(
                    f"Parabéns, conseguimos uma astrolábio de ATAQUE com {atributos['Ataque Magico']}-{atributos['Espirito']}-{atributos['Penetracao Magica']}"
                ),
                title="I.A do John",
                button="Obrigado",
            )
            exit()

        # elif (
        #     atributos["Defesa"] >= 2
        #     and atributos["Espirito"] >= 2
        #     and atributos["HP"] >= 1
        # ):
        #     # Se já atendeu a condição, segura o novo add
        #     pyautogui.click(botao_reproduzir[0] + 155, botao_reproduzir[1] - 15)
        #     pyautogui.alert(
        #         text=(
        #             f"Parabéns, conseguimos uma astrolábio de DEFESA com {atributos['Defesa']}-{atributos['Espirito']}-{atributos['HP']}"
        #         ),
        #         title="I.A do John",
        #         button="Obrigado",
        #     )
        #     exit()
        else:
            pyautogui.click(botao_reproduzir)
            time.sleep(0.5)


if __name__ == "__main__":
    main()
