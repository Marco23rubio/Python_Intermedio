from functools import reduce

def run():
    my_list = [1,4,5,6,9,13,19,21]

    odd = list(filter(lambda x: x%2 !=0,my_list))

    print(odd)

    list2 = [1,2,3,4,5,6]

    squares = list(map(lambda x: x**2,list2))

    print(squares)

    list3 = [2,2,2,2,2]

    all_multiplied = reduce(lambda x,y:x*y,list3)

    print(all_multiplied)


if __name__ == "__main__":
    run()