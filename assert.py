def divisor(num):
        
    lista =[i for i in range(1,num+1)if num %i ==0]
    return lista              
        
def run():
   
    num = input("Ingresa un número: ")
    assert num.isnumeric(), "Debes ingresar un número entero"    
    print(divisor(int(num)))
   
if __name__ == "__main__":
    run()