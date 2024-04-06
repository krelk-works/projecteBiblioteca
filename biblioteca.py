import sys
from bibliotecaUtils import *
from getpass import getpass

try:
    with open("llibres.txt", "r") as archivo:
        pass
except OSError:
    print("Arxiu de llibres no trobat, creant arxiu...")
    with open("llibres.txt", "a") as archivo:
        archivo.write("")
    print("[ok] - Arxiu creat correctament.")

try:
    with open("usuaris.txt", "r") as archivo:
        pass
except OSError:
    print("Arxiu d'usuaris no trobat, creant arxiu...")
    with open("usuaris.txt", "a") as archivo:
        archivo.write("")
    print("[ok] - Arxiu creat correctament.")

if not session:
    print("\n[BiblitecaCanCasacuberta] - v1.0")
    print("\nBenvingut a la biblioteca, si us plau, inicia sessió per poder accedir al sistema.\n")
    newusername = str(input("Nom d'usuari: "))
    newpassword = getpass("Contrasenya: ")
    login(newusername, newpassword)