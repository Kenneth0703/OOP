from datetime import date

class Student:
    def __init__(self,studentid,name,dob,classification):
        self.__studentid = studentid
        self.__name = name
        self.__dob = dob
        self.__classification = "Class"
        
        self.__age = 0
        self.__register = ""

# attribute
    def calc_age(self):
        today = date.today()

        dob = self.__dob.split("/")
        dob_year = int(dob[2])
        self.__age = today.year - dob_year

    def calc_register(self):
        if self.__classification == "senior":
            self.register = "4/2 thru 4/3"
        elif self.__classification == "junior":
            self.register = "4/4 thru 4/6"
        elif self.__classification == "soph":
            self.register = "4/6 thru 4/9"
        elif self.__classification == "fresh":
            self.register = "4/10 thru 4/12"
        else:
            self.register = "class not found"                             #catch all

    def get_age(self):
        return self.__age
    def get_register(self):
        return self.__register


        # all my code
    # def calc_age(self):
    #     today = date.today()
    #     year = today.year()
    #     # dob = "10/11/2001"
    #     dob = dob.split("/")
    #     dob_year = int(dob[2])
    #     self.age = dob_year - year

    # def age1(self):
    #     if self.age == 22:
    #         return "Senior"
    #     else: 
    #         return "ooo"
    #     # return "This student is " + format (self.age)




