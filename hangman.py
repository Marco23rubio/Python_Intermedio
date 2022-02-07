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


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def interfaz():
    print("""
Hola, Bienvenido al juego del ahorcado
En la pantalla apreciarás la palabra que deberas adivinar
Solo contarás con 6 vidas asi que se cuidadoso a la hora de elegir
Listo? Comencemos.

La palabra secreta es:
""")
    
def juego():
    lista_adivinanza= []
    lista_total = []
    seleccion = normalize(palabra_secreta())
    print(seleccion)
    actual = []
    vidas = 6
    for i in range(len(seleccion)):
            actual.append("_")
    while vidas != 0:
        print("vidas:",vidas)
        print(actual)
        print(lista_adivinanza)
        adivinanza = (str(input("\nIngresa una letra:")))
        adivinanza = adivinanza.lower()
        for i in range(len(seleccion)):
            if seleccion[i] == adivinanza:
                actual[i] = adivinanza
        clear()
        if len(adivinanza) > 1:
            print("Solo se puede poner una letra por intento >:v")
        if len(adivinanza) == 1:
            if adivinanza in lista_total:
                print("Ya usaste esa letra, intenta con otra")
            else:
                if adivinanza in seleccion:
                    print("Es correcto sigue asi",adivinanza)
                    lista_adivinanza.append(adivinanza)
                    lista_total.append(adivinanza)
                elif adivinanza not in seleccion:
                    print("Es incorrecto",adivinanza)
                    vidas -= 1
                    lista_total.append(adivinanza)
                if len(lista_adivinanza) == len(actual):
                    clear()
                    print("FELICIDADES HAS GANADO TU PALABRA ERA:",seleccion)
                    break
                if vidas == 0:
                    clear()
                    print("Lo siento, has perdido, tu palabra era:",seleccion)       

def run():
    clear()
    lista()
    interfaz()
    juego()
    
if __name__ == "__main__":
    run()