import hashlib

def login(username, password):
    global session, sessionName, sessionTry
    with open("usuaris.txt") as archivo:
        for linea in archivo:
            username_bbdd, password_bbdd = linea.split("|")
            if username_bbdd == username and password_bbdd == password:
                session = True
                sessionName = username
                print("Benvingut "+username)
                break
    
    if session != True and sessionTry < 3:
        sessionTry=sessionTry+1
        print("Has fallat l'inici de sessió, torna-ho a provar.")
        newusername = str(input("Nom d'usuari: "))
        newpassword = str(input("Contrasenya: "))
        login(newusername, newpassword)
    else:
        print("Has esgotat el numero d'intents disponibles, prova-ho més tard.")
        
    
def encriptar(password):
    return hashlib.md5(password.encode()).hexdigest()

def agregar_libro(titol, autor, any_publicacio, genere, ISBN):
    with open("llibres.txt", "a") as archivo:
        archivo.write(f"{titol}|{autor}|{any_publicacio}|{genere}|{ISBN}\n")
    print("Has añadido el libro correctamente, HIJO DE PUTA")