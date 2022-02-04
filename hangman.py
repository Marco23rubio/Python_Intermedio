import os
import random

def clear():
    os.system("clear")

def lista():
    with open ("./archivos/data.txt","r",encoding="utf-8") as f:
        lista_palabras = [i.strip() for i in f]
        return lista_palabras
        #print(lista_palabras)
        # palabra_secreta= random.choice(lista_palabras)
        # return palabra_secreta

def palabra_secreta():
    lista_palabras = lista()
    seleccion = random.choice(lista_palabras)
    return seleccion 

def acentos():
    pass 

def interfaz():
    seleccion = palabra_secreta()
    vidas = 6
    print("""
Hola, Bienvenido al juego del ahorcado
En la pantalla apreciarás la palabra que deberas adivinar
Solo contarás con 6 vidas asi que se cuidadoso a la hora de elegir
Listo? Comencemos.

La palabra secreta es:{}
""".format(seleccion))
    
 

def run():
    # lista_palabras = archivo()
    # print(lista_palabras)
    clear()
    lista()
    interfaz()
   
if __name__ == "__main__":
    run()