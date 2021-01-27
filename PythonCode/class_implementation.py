# class Student:
#     def __init__(self, name, surname, yob, section):
#         self.name = name
#         self.surname = surname
#         self.yob = yob
#         self.section = section
#
# class School(Student):
#     def __init__(self, school):
#         self.school = school
#
#     def __str__(self):
#         return self.name + self.surname + self.yob + self.section + self.school
#
# print("Enter the number of students you want to enter the details")
# a = int(input())
# for i in range(a):
#     sch = input("Enter the school name\n")
#     i = School(sch)
#     print("Enter the name, surname, year of birth, section in the same order\n")
#     i.name = input()
#     i.surname = input()
#     i.yob = input()
#     i.section = input()
#     i.school = input()
#
# print("Entered details\n")
# for i in range(a):
#     print("name | surname | year of birth | section | school" )
#     print(i.name, i.surname, i.yob, i.section, i.school)

import pandas as pd
class student:
    def __init__(self):
        self.name = input("Enter student name :\n")
        self.surname = input("Enter surname :\n")
        self.yob= input("Enter year of birth :\n")
        self.std= input("Enter class of the student :\n")

class school(student):
    def __init__(self,*args):
        super().__init__(*args)
        self.school = input("Enter Schoolname : \n")
        def __str__(self):
            return "Name :" + self.name + " Surname :" + self.surname + " Year of Birth :" + self.yob + " Class " + self.std + " School Name : " +self.school
key = 'y'
while(key.lower() == 'y'):
    no_of_student=int(input("Enter no of students\n"))
    x=[]
    for i in range (no_of_student):
        school_obj = school()
        x.append(school_obj)
        pd.DataFrame.from_records([s.__dict__ for s in x])
    key = input("Do you want to continue. Press y or n\n")
