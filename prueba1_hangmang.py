import os
import random 

def clear():
   os.system("clear") 

def write():
    
    with open ("./archivos/data.txt","r",encoding="utf-8") as f:
        # for i,p in (enumerate(f,1)):
        #     print(i,p)
        palabras  = {i:v for i,v in enumerate(f,1)}
        eleccion= (random.choice(palabras))
        print("""
Bienvenido al juego del ahorcado
Solo debes intentar encontrar la palabra escondida
Pero solo tienes 6 oportunidades
¡VAMOS A JUGAR! \n""") 
        print(eleccion)
        longitud = int(len(eleccion))
        print("_ "*(longitud-1)) 
        correcto = []
        vidas = 6
        #print("\nVidas = {} \n".format(vidas))
        #letra=str.lower(input("\nIngresa una letra:"))
        #print(letra)
        longitud = len(eleccion)
        
        lista = list(eleccion)
        lista.pop(-1)
        print("\n{}".format(lista))
        


        while vidas != 0 or (longitud-1) == len(correcto):
            print("\nVidas: {}".format(vidas))
            letra = str.lower(input("\nIngresa una letra:"))
            if len(letra) > 1:
                print("Solo se permite poner UNA sola letra por intento >:v")
            if len(letra) == 1:
                if letra in eleccion:
                    correcto.append(letra)
                    print("correcto,vas por buen camino")
                elif letra not in eleccion:
                    vidas -= 1
                    print("Esa letra no está")
                if vidas == 0:
                    print("Game Over")
                if (longitud-1) == len(correcto):
                    print("GANASTE")
                    break
            




def run():
    clear()
    write()

if __name__ == "__main__":
    run()