import insectclass as ins


mosquito = ins.Bug("mosquito",2,4)
housefly = ins.Bug("housefly",2,4)

mosquito.fly()
housefly.fly()

print(f"the {mosquito.get_name} can fly up to{mosquito.get_flight}")

print(f"the {housefly.get_name} can fly up to{housefly.get_flight}")



    # for count in range(1,11):    
    #     print("my bug flew this far:",mosquito.get_flight())
    #     mosquito.fly()
