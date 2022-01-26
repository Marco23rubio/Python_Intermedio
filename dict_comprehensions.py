import math 

def run():
    # diccionario = {}

    # for i in range(1,101):
    #     diccionario[i] = i **3
    
    # print(diccionario)
    # diccionario = {i:i**3 for i in range(1,101) if i %3 !=0}

    # print(diccionario)

    # diccionario = {i:math.sqrt(i) for i in range(1,101)}
    # print(diccionario)

    palindrome = lambda string: string == string [::-1]
    print(palindrome("fernanda"))

if __name__ == '__main__':
    run() 