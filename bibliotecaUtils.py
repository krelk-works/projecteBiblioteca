import hashlib
from getpass import getpass


session = False
sessionName = None
sessionTry = 0

def login(username, password):
    global session, sessionName, sessionTry
    password=encriptar(password)
    with open("usuaris.txt", "r") as archivo:
        for linea in archivo:
            username_bbdd, password_bbdd = linea.split("|")
            if username_bbdd.strip() == username and password_bbdd.strip() == password:
                session = True
                sessionName = username
                print("\nBenvingut "+username+"\n")
                bibliotecaMenu()
                break
    
    if session != True and sessionTry < 2:
        sessionTry=sessionTry+1
        print("[!] - Has fallat l'inici de sessió, torna-ho a provar.\n")
        newusername = str(input("Nom d'usuari: "))
        newpassword = getpass("Contrasenya: ")
        login(newusername, newpassword)
    elif session != True and sessionTry == 2:
        print("\n[!] - Has esgotat el numero d'intents disponibles, prova-ho més tard.")
        print("=====================================================================")
        
    
def encriptar(password):
    return str(hashlib.md5(password.encode()).hexdigest())

def buscarLibro(titol):
    print("[...] - Buscant llibre {",titol,"} a la base de dades...")
    with open("llibres.txt", "r") as archivo:
        encontrado=False
        print("-------------------")
        for linea in archivo:
            titol_bbdd, autor_bbdd, any_publicacio_bbdd, genere_bbdd, isbn_bbdd = linea.split("|")
            if titol_bbdd.lower() == titol.lower():
                print("Títol:", titol_bbdd)
                print("Autor:", autor_bbdd)
                print("Año de publicacion:", any_publicacio_bbdd)
                print("Genero:", genere_bbdd)
                print("ISBN:", isbn_bbdd)
                print("-------------------")
                encontrado = True
                break
        if not encontrado:
            print("[!] - Llibre no trobat, tornant al menu principal.")
    bibliotecaMenu()

def veureTotsElsLlibres():
    with open("llibres.txt", "r") as archivo:
        print("-------------------")
        print("Llistat de llibres:")
        print("-------------------")
        for linia in archivo:
            titol_bbdd, autor_bbdd, any_publicacio_bbdd, genere_bbdd, isbn_bbdd = linia.strip().split("|")
            print("Titol:", titol_bbdd)
            print("Autor:", autor_bbdd)
            print("Any de publicacio:", any_publicacio_bbdd)
            print("Genere:", genere_bbdd)
            print("ISBN:", isbn_bbdd)
            print("-------------------")
    bibliotecaMenu()

def afegirLlibre(titol, autor, any_publicacio, genere, ISBN, bypass = False):
    liniesTotals = 0
    with open("llibres.txt", "r") as archivo:
        for linea in archivo:
            titol_bbdd = linea.split("|")[0]
            if titol_bbdd == titol:
                print("[!] - El llibre amb titol",titol,"ja existeix a la base de dades. Tornant al menu principal.")
                bibliotecaMenu()
                return
            liniesTotals += 1
    
    with open("llibres.txt", "a") as archivo:
        if liniesTotals > 0:
            archivo.write(f"\n{titol}|{autor}|{any_publicacio}|{genere}|{ISBN}")
        else:
            archivo.write(f"{titol}|{autor}|{any_publicacio}|{genere}|{ISBN}")
        
        if not bypass:
            print("[ok] - Has afegit el llibre",titol,"correctament")
    
    if not bypass:
        bibliotecaMenu()
        
def esborrarLlibre(titol, confirm = True):
    confirmacio = None
    if confirm:
        confirmacio = str(input("[!] - Realemnt vols esborrar el llibre de la base de dades? [S/N]: "))
    if confirm and confirmacio.capitalize() == "S" or not confirm:
        with open("llibres.txt", "r") as archivo:
            encontrado=False
            for linea in archivo:
                titol_bbdd = linea.split("|")[0]
                if titol_bbdd.lower() == titol.lower():
                    encontrado = True
            if not encontrado:
                print("[!] - Llibre per esborrar no trobat.")
                if confirm:
                    print("[!] - Tornant al menu principal.")
                    bibliotecaMenu()
        
        # Desem les línies del fitxer a una llista
        linies = []
        with open("llibres.txt", "r") as arxiu:
            for linia in arxiu.readlines():
                linies.append(linia)
        
        with open("llibres.txt", "w") as arxiu:
            # Esborrem el contingut del fitxer
            arxiu.write("")

            # Escriurem novament el document sense el salt de linia final
            maxLinies = len(linies) - 2
            liniaActual = 0
            for linia in linies:
                if linia.split("|")[0] != titol:
                    if liniaActual == maxLinies:
                        arxiu.write(linia.replace('\n', ''))
                    else:
                        arxiu.write(linia)
                    liniaActual += 1
    else:
        print("[!] - Esborrament de llibre cancelat, tornant al menu principal")

    if confirm:
        bibliotecaMenu()

def editarLlibre(titol):
    llibreTrobat = False
    
    # Dades de la base de dades
    titol_bbdd, autor_bbdd, any_publicacio_bbdd, genere_bbdd, isbn_bbdd = None, None, None, None, None
    
    with open("llibres.txt", "r") as archivo:
        for linea in archivo:
                titol_bbdd, autor_bbdd, any_publicacio_bbdd, genere_bbdd, isbn_bbdd = linea.split("|")
                if titol_bbdd.lower() == titol.lower():
                    llibreTrobat = True
                    break
        
    if llibreTrobat:
        print("A continuació modifica les dades del llibre (si ho deixes en blanc no es canviara)")
        print("==================================================================================")
        print("Llibre actual :",titol)
        llibreTitol = str(input("Insereix el nou titol del llibre: "))
        autorTitol = str(input("Insereix nou autor del llibre: "))
        anyPublicacio = str(input("Insereix nou any de publicació: "))
        genereLlibre = str(input("Insereix nou genere del llibre: "))
        isbnLlibre = str(input("Insereix el nou ISBN del llibre: "))
        
        nouTitol = llibreTitol or titol_bbdd
        nouAutor = autorTitol or autor_bbdd
        nouAny = anyPublicacio or any_publicacio_bbdd
        nouGenere = genereLlibre or genere_bbdd
        nouISBN = isbnLlibre or isbn_bbdd
        esborrarLlibre(titol, False)
        afegirLlibre(nouTitol, nouAutor, nouAny, nouGenere, nouISBN, True)
        print("-------------------")
        print("Llibre actualitzat :",titol)
        print("-------------------")
        print("Titol:", nouTitol)
        print("Autor:", nouAutor)
        print("Any de publicacio:", nouAny)
        print("Genere:", nouGenere)
        print("ISBN:", nouISBN)
        print("-------------------")
        bibliotecaMenu()
    else:
        print("[!] - No s'ha trobat el llibre que vols editar. Tornant al menu principal.")
        bibliotecaMenu()

def bibliotecaMenu():
    print("=========================")
    print("Menu interactiu de la Biblioteca Can Casacuberta")
    print("[1] Veure un llibre")
    print("[2] Veure tots els llibres")
    print("[3] Afegir un llibre")
    print("[4] Eliminar un llibre")
    print("[5] Editar un llibre")
    print("[6] Sortir")
    print("==========================")
    try:
        opcio=int(input("Seleccionar opció: "))
        match opcio:
            case 1:
                titol = input("Introdueix el nom del llibre que vols veure: ")
                buscarLibro(titol)
            case 2:
                veureTotsElsLlibres()
            case 3:
                llibreTitol = str(input("Insereix el titol del llibre: "))
                autorTitol = str(input("Insereix l'autor del llibre: "))
                anyPublicacio = str(input("Insereix l'any de publicació: "))
                genereLlibre = str(input("Insereix el genere del llibre: "))
                isbnLlibre = str(input("Insereix el ISBN del llibre: "))
                if llibreTitol and autorTitol and anyPublicacio and genereLlibre and isbnLlibre:
                    afegirLlibre(llibreTitol, autorTitol, anyPublicacio, genereLlibre, isbnLlibre)
                else:
                    print("No has inserit correctament totes les dades del llibre, torna-ho a probar")
                    bibliotecaMenu()
            case 4:
                llibreTitol = str(input("Insereix el titol del llibre que volguis eliminar: "))
                if llibreTitol:
                    esborrarLlibre(llibreTitol)
                else:
                    print("No has inserit el nom del llibre a esborrar")
                    bibliotecaMenu()
            case 5:
                llibreTitol = str(input("Insereix el titol del llibre que volguis editar: "))
                if llibreTitol:
                    editarLlibre(llibreTitol)
                else:
                    print("No has inserit el nom del llibre a editar")
                    bibliotecaMenu()
            case 6:
                print("Sistema de biblioteca tancat. Fins la propera!")
                exit()
            case _:
                print("\n[!] - Opcio no válida : "+str(opcio))
                bibliotecaMenu()
    except ValueError:
        print("[!] - Només es permés fer ús de numeros per seleccionar una opció")
        bibliotecaMenu()