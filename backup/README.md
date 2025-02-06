# Installation

Python >= 2.7
[tesseract ocr](https://digi.bib.uni-mannheim.de/tesseract/)
ou
[tesseract ocr](https://github.com/tesseract-ocr/tesseract/releases)

```
py -m pip install pytesseract
py -m pip install pyautogui
py -m pip install win32gui
py -m pip install pywin32
py -m pip install pyinstaller
```

# Executavel

```
pyinstaller nome.py
pyinstaller --onefile --noconsole nome.py
```

Com icone

```
pyinstaller --onefile --noconsole nome.py -i nome.ico
```
