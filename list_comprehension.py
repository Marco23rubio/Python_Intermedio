def run():

    # lista = []
    # cantidad = 100

    # for x in range(1,cantidad+1):
    #     if x**2 % 3 !=0:
    #         lista.append(x**2)
    
    #lista = [i for i in range(1,100000)if i % 36 == 0]

    number =[x for x in range(1,100000)if x % 4 == 0 and x % 6 == 0 and x % 9 == 0]

    print(number)

    #print(lista)

if __name__ == "__main__":
    run()