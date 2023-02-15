from datetime import date
class Student:
    def __init__(self,id,name,dob,classification):
        self.__studentid = "id"
        self.__name = name
        self.dob = dob
        self.age = 0
        self.register = ""


# attribute
    def calc_age(self):
        today = date.today()
        x = self.dob.split("/")
        x_year = int(dob[2])
        self.age = today.year - x_year

    def calc_register(self):
        if self.classification == "senior":
            self.register = "4/2 thru 4/3"
        elif self.classification == "junior":
            self.register = "4/4 thru 4/6"
        elif self.classification == "soph":
            self.register = "4/6 thru 4/9"
        elif self.classification == "fresh":
            self.register = "4/10 thru 4/12"
        else:
            self.register = "class not found"                             #catch all

    def get_age(self):
        return self.age
    def get_register(self):
        return self.register


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




