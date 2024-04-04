import sys
from bibliotecaUtils import *

session = False
sessionName = None
sessionTry = 0

try:
    match sys.argv[1]:
        case "-login":
            try:
                login(sys.argv[2], sys.argv[3])
            except IndexError:
                print("No has ingresado una contraseña o un nombre de usuario, vuelve a intentarlo, si us plau.")
        case "-agregar":
            try:
                if session:
                    agregar_libro(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
                else:
                    print("Abans de fer cualsevol acció hauras d'iniciar sesió")
            except IndexError:
                print("Faltan datos del libro")
        case _:
            print("El parámetro ingresado no es correcto, vuelve a leer las instrucciones del xampú, si us plau.")
except IndexError:
    print("No has puesto ningún parámetro, vuelve a intentarlo, si us plau.")
   
        
        
