#!/usr/bin/python3

# Author: Kaio Amaral or kira
# Script that contains the banners.

# Commands that can be used.
commands = {
  "Call Log": "Historico de Chamadas.",
  "Camera Photo": "Tirar Foto.",
  "Volume": "Mudar Volume.",
  "Contact List": "Lista de Contatos.",
  "Media Player": "Tocar uma Música.",
  "tts Speak": "Falar algo.",
  "Location": "Localização.",
  "Sms List": "Lista de Mensagens.",
  "Sms Send": "Enviar uma Mensagem.",
  "Torch": "Ligar Lanterna.",
  "Wallpaper": "Mudar Wallpaper."
  }


# All banners.
def banner():
    text = """1 - Ver Todos Comandos\n2 - Ver Informações do Criador\n3 - Sair\n4 - Comando Aparte"""
    bn1 =  f"""
      _
  ___| |___
 |___   ___|
     | |      don't leave me here
     | |
     | |
     '-'

kira's justice

{text}
"""

    bn2 = f"""
      ▄▄▄▄▄███████████████████▄▄▄▄▄
    ▄██████████▀▀▀▀▀▀▀▀▀▀██████▀████▄
  ▄██▀████████▄─────────────▀▀████─▀██▄
 ▀██▄▄██████████████████▄▄▄─────────▄██▀
   ▀█████████████████████████▄────▄██▀
     ▀████▀▀▀▀▀▀▀▀▀▀▀▀█████████▄▄██▀
       ▀███▄──────────────▀██████▀
         ▀██████▄─────────▄████▀
            ▀█████▄▄▄▄▄▄▄███▀
              ▀████▀▀▀████▀
                ▀███▄███▀
                   ▀█▀


{text}
"""

    bn3 = f"""
 ___
|_ _|    ▄█▀█▄  ▄███▄
 | |    ▐█░██████████▌
 | |     ██▒█████████
 | |      ▀████████▀
|___|        ▀██▀
 _                _    _
| |__   __ _  ___| | _(_)_ __   __ _
| '_ \ / _` |/ __| |/ / | '_ \ / _` |
| | | | (_| | (__|   <| | | | | (_| |
|_| |_|\__,_|\___|_|\_\_|_| |_|\__, |
                               |___/

{text}
"""


    bn4 = f"""

███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████


{text}
"""
    return [bn1, bn2, bn3, bn4]










def usage():
    texto = "\033[31m"+"[-] Erro na Passagem de Argumentos!"+"\033[1;32m"+"\n[+] Use: "+"\033[1;32m"+"python3 dedsec.py"+"\033[1;34m"+" [host] "+"\033[1;33m"+"[porta]"+"\033[0;0m"
    return texto
