import pyautogui
import utils.function as f


def locate_images(image_paths, confidence=0.9):
    for image_path in image_paths:
        try:
            found_images = list(
                pyautogui.locateAllOnScreen(image_path, confidence=confidence)
            )

            if found_images:
                return found_images
        except:
            continue

    return []


def main():
    f.ShowWindow("Perfect World")  # Abre a Janela do pw

    while True:
        botao = locate_images([r"image\1920x1080\iniciar_horoscopo.png"])[0]
        pyautogui.click(botao)
        # pyautogui.sleep(0.2)

        penetracao_images = [
            r"image\1920x1080\PenetMagica.png",
            r"image\1920x1080\PenetMagica2.png",
        ]
        penetracao = locate_images(penetracao_images)
        atqM = locate_images([r"image\1920x1080\atqM.png"])
        espirito = locate_images([r"image\1920x1080\espirito.png"])
        defesa = locate_images([r"image\1920x1080\def.png"])
        hp = locate_images([r"image\1920x1080\hp.png"])

        print(
            f"Espirito: {len(espirito)} Penetracao: {len(penetracao)} AtaM: {len(atqM)}"
        )
        print(f"Espirito: {len(espirito)} Defesa: {len(defesa)} Hp: {len(hp)}")

        print(20 * "-")

        # if len(penetracao) == len(espirito) == len(atqM) == 2:
        #     pyautogui.alert(
        #         "Conseguimos um Astro (2 2 2) de Ataque.\n", "I.A do John", "OK"
        #     )
        #     break

        if len(hp) == len(espirito) == len(defesa) == 2:
            pyautogui.alert(
                "Conseguimos um Astro (2 2 2) de Defesa.\n", "I.A do John", "OK"
            )
            break


if __name__ == "__main__":
    main()
