def divisor(num):
    
    try:
        lista =[i for i in range(1,num+1)if num %i ==0]
        if num <=0:
            raise ValueError("No se pueden ingresar numeros negativos o el 0")        
        return lista              
    except ValueError as ve:
        print(ve)
        return str(num) + ":No es un numero positivo"
        
def run():
    try:
        num = int(input("Ingresa un número: "))    
        print(divisor(num))
    except ValueError:
        print("Solo se pueden ingresar números enteros")


if __name__ == "__main__":
    run()