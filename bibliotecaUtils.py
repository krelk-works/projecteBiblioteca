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
            username_bbdd = username_bbdd.strip() ### Evitar errores por espacios en blanco en el nombre
            password_bbdd = password_bbdd.strip() ### Evitar errores por espacios en blanco en la contraseña
            if username_bbdd == username and password_bbdd == password:
                session = True
                sessionName = username
                print("Benvingut "+username)
                bibliotecaMenu()
                break
    
    if session != True and sessionTry < 3:
        sessionTry=sessionTry+1
        print("Has fallat l'inici de sessió, torna-ho a provar.")
        newusername = str(input("Nom d'usuari: "))
        newpassword = str(input("Contrasenya: "))
        login(newusername, newpassword)
    elif session != True and sessionTry == 3:
        print("Has esgotat el numero d'intents disponibles, prova-ho més tard.")
        
    
def encriptar(password):
    return str(hashlib.md5(password.encode()).hexdigest())

def agregar_libro(titol, autor, any_publicacio, genere, ISBN):
    with open("llibres.txt", "a") as archivo:
        archivo.write(f"{titol}|{autor}|{any_publicacio}|{genere}|{ISBN}\n")
    print("Has añadido el libro correctamente, HIJO DE PUTA")
    
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
                ###agregar_libro()
                print("Agregar libro...")
            case _:
                print("\nError : Opcio no válida : "+str(opcio))
                bibliotecaMenu()
    except ValueError:
        print("Error : Només es permés fer ús de numeros per seleccionar una opció")
        bibliotecaMenu()