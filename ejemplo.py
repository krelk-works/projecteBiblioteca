import sys
import hashlib

sesion = False
    
def login(username, password):
    ###llistaUsuaris = open("usuaris.txt", "r")
    ##print(llistaUsuaris.read())
    ###print("Inicio de sesión de : ",username, password)
    ###print("Contraseña encriptada : ",encriptar(password))
    
    with open("usuaris.txt") as archivo:
        for linea in archivo:
            nombre, contraseña = linea.split("|")
            print("Nombre usuario: ", nombre)
            print("Contraseña : ", contraseña)
            
    
    
def encriptar(password):
    return hashlib.md5(password.encode()).hexdigest()

def agregar_libro(titol, autor, any_publicacio, genere, ISBN):
    with open("llibres.txt", "a") as archivo:
        archivo.write(f"{titol}|{autor}|{any_publicacio}|{genere}|{ISBN}\n")
    print("Has añadido el libro correctamente, HIJO DE PUTA")

try:
    match sys.argv[1]:
        case "-login":
            try:
                login(sys.argv[2], sys.argv[3])
            except IndexError:
                print("No has ingresado una contraseña o un nombre de usuario, vuelve a intentarlo, si us plau.")
        case "agregar_libro":
            try:
                if sesion:
                    agregar_libro(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
                else:
                    print("Primero inicia sesion puta")
            except IndexError:
                print("Faltan datos del libro")
        case _:
            print("El parámetro ingresado no es correcto, vuelve a leer las instrucciones del xampú, si us plau.")
except IndexError:
    print("No has puesto ningún parámetro, vuelve a intentarlo, si us plau.")
   
        
        
