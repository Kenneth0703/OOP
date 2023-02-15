import StudentClass as sc


studentid = 1001
name = "jphn"
dob = "10/11/2001"
classification = "jr"

student1 = sc.Student(studentid,name,dob,classification)

student1.calc_age()     #make sure you use object name
student1.calc_register()

print(f"Studnet ages is: {student1.get_age()}")
print(f"Studnet can register between: {student1.get_register()}")










# import StudentClass as sc
# def main():
#     stu = input("Enter Student ID: ")
#     name = input("Enter Student Name: ")
#     dob = input("Enter DOB : ")
#     classification = input("Enter Classication ID: ")

#     student = sc.Student(age,dob,id)
#     print(student)


# main()



