import webbrowser
import pyautogui
from time import sleep

# Opção 1 (descomentar a opção desejada)
# telefones = [5548995853584, 554799558685, 5547558896584]


telefones = []
with open('fones.txt', 'r') as arquivo:
    for linha in arquivo:
        # Remove espaços em branco, colchetes e apóstrofos
        telefone = linha.strip().replace('[', '').replace(']', '').replace("'", "")
        telefones.append(telefone)

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click(941,332,duration=1)
    sleep(5)
    pyautogui.click(956,397,duration=1)
    sleep(10)
    pyautogui.typewrite('Teste bot')
    sleep(5)
    pyautogui.press('enter')