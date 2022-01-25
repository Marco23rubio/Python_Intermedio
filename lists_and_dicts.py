def run():
    my_list = [1,"hello",True,4.5]
    my_dict = {"firstname":"Facundo","lastname":"García"}

    super_list = [
        {"firstname":"Facundo","lastname":"García"},
        {"firstname":"Miguel","lastname":"Torres"},
        {"firstname":"Pepe","lastname":"Rodelo"}
    ]

    super_dict = {
        "Natural_nums":[1,2,3,4,5],
        "Integer_nums":[-1,0,2,4,8],
        "Floating_nums":[1.1,4.8,6.85]
    }

    for key,value in super_dict.items():
        print(key,":",value)
    
    print("-"*50)

    for value in super_list:
        print("Firstname:",value["firstname"],"-","Lastname:",value["lastname"])
        # for key,value in value.items():
        #     print(f"{key}-{value}")

if __name__ == "__main__":
    run()