import hashlib

session = False
sessionName = None
sessionTry = 0

def login(username, password):
    global session, sessionName, sessionTry
    password=encriptar(password)
    with open("usuaris.txt") as archivo:
        for linea in archivo:
            username_bbdd, password_bbdd = linea.split("|")
            if username_bbdd.strip() == username and password_bbdd.strip() == password:
                session = True
                sessionName = username
                print("Benvingut "+username)
                bibliotecaMenu()
                break
    
    if session != True and sessionTry < 2:
        sessionTry=sessionTry+1
        print("Has fallat l'inici de sessió, torna-ho a provar.")
        newusername = str(input("Nom d'usuari: "))
        newpassword = str(input("Contrasenya: "))
        login(newusername, newpassword)
    elif session != True and sessionTry == 2:
        print("Has esgotat el numero d'intents disponibles, prova-ho més tard.")
        
    
def encriptar(password):
    return str(hashlib.md5(password.encode()).hexdigest())

def buscarLibro(titol):
    with open("llibres.txt") as archivo:
        encontrado=False
        for linea in archivo:
            titol_bbdd, autor_bbdd, any_publicacio_bbdd, genere_bbdd, isbn_bbdd = linea.split("|")
            if titol_bbdd.lower() == titol.lower():
                print("Títol:", titol_bbdd)
                print("Autor:", autor_bbdd)
                print("Año de publicacion:", any_publicacio_bbdd)
                print("Genero:", genere_bbdd)
                print("ISBN:", isbn_bbdd)
                encontrado = True
                break
        if not encontrado:
            print("LIbro no encontrado")

def agregarLibro(titol, autor, any_publicacio, genere, ISBN):
    ### Comprobamos si ya existe el libro
    with open("llibres.txt") as archivo:
        for linea in archivo:
            titol_bbdd, autor_bbdd, any_publicacio_bbdd, genere_bbdd, isbn_bbdd = linea.split("|")
            if titol_bbdd.strip() == titol and autor_bbdd.strip() == autor and any_publicacio_bbdd.strip() and genere_bbdd.strip() == genere and isbn_bbdd.strip() == ISBN:
                print("El llibre amb titol",titol,"ja existeix a la Base de Dades")
                bibliotecaMenu()
                return
    
    ### Agregamos el libro
    with open("llibres.txt", "a") as archivo:
        archivo.write(f"\n{titol}|{autor}|{any_publicacio}|{genere}|{ISBN}")
        print("Has añadido el libro correctamente")
        
def esborrarLlibre(titol):
    print("Borrando libro : ", titol)
    
def bibliotecaMenu():
    print("\n")
    print("=========================")
    print("Menu d'interració de la Biblioteca")
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
            case 3:
                llibreTitol = str(input("Insereix el titol del llibre: "))
                autorTitol = str(input("Insereix l'autor del llibre: "))
                anyPublicacio = str(input("Insereix l'any de publicació: "))
                genereLlibre = str(input("Insereix el genere del llibre: "))
                isbnLlibre = str(input("Insereix el ISBN del llibre: "))
                if llibreTitol and autorTitol and anyPublicacio and genereLlibre and isbnLlibre:
                    agregarLibro(llibreTitol, autorTitol, anyPublicacio, genereLlibre, isbnLlibre)
                else:
                    print("No has inserit correctament totes les dades del llibre, torna-ho a probar")
                    bibliotecaMenu()
            case 4:
                llibreTitol = str(input("Insereix el titol del llibre que volguis eliminar: "))
                if llibreTitol:
                    esborrarLlibre(llibreTitol)
                else:
                    print("No has inserit el nom del llibre a esborrar")
            case _:
                print("\nError : Opcio no válida : "+str(opcio))
                bibliotecaMenu()
    except ValueError:
        print("Error : Només es permés fer ús de numeros per seleccionar una opció")
        bibliotecaMenu()