import sys
from bibliotecaUtils import *



try:
    match sys.argv[1]:
        case "-login":
            try:
                login(sys.argv[2], sys.argv[3])
            except IndexError:
                print("No has ingresado una contraseña o un nombre de usuario, vuelve a intentarlo, si us plau.")
        case _:
            print("El parámetro ingresado no es correcto, vuelve a leer las instrucciones del xampú, si us plau.")
except IndexError:
    print("No has puesto ningún parámetro, vuelve a intentarlo, si us plau.")