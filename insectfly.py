import insectclass as ins

def main():
    my_bug = ins.Bug()
    print("my bug flew")

    for count in range(10):    
        print("my bug flew this far:",my_bug.get_flight())
        my_bug.fly()
main()