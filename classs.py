# class Studint:
#     def __init__(self,Name='defult',Age=18,Grade=1,City='irbid',Speacialise='computer',passowrd='123456'):
#         self.name=Name
#         self.age=Age
#         self.grade=Grade
#         self.city=City
#         self.speacialise=Speacialise
#         self.password=passowrd
#     def __str__(self):
#        return f'name is{self.name} and age {self.age} and grade{self.grade}and city{self.city}and speacialise{self.speacialise}'
#     def talk(self):
#         return f'hello my name is {self.name}'
#     def addCourse(self, newCoures):
#        return f'hello{self.name} you have added{newCoures}to youer coures'

# students=[]
# while True:

#     print('welcome to programe')
#     print('1-login')
#     print('2-register')
#     print('3-exit')
#     userchoice=int(input('emter the choice'))
#     if userchoice ==1:
#         print('welcome to our longin page')
#         while True:

#          username=input('enter th name  ')
#          password=input('enter the password  ')
#         #  for i in range(len(students)):
#         #     if students[i].name==username and students[i].password==password:
#         #         print('your are logged in succesfully')
#         #         print(students[i])
#         #         break
            
#         #     else:
#         #         print('wrong username or password')
#                 #  OR
#         for student in students:
#              if student.name==username and student.password==password:
#                 print('your are logged in succesfully')
#                 print(student)
#                 print('1-add course')
#                 print('2-take quiz')
#                 # studentChoice=int(input('enter the choice'))
#                 # if studentChoic== 1:
#                 #     studint1.addCourse(input('enter the course name:'))
#              else:
#                   print('wrong username or password')


    
#     elif userchoice==2:
#         print('hello my programe')
#         name=input('enter the name  ')
#         age=int(input('enter the age  '))
#         grade=int(input('enter the grade  '))
#         city=input('enter the city  ')
#         speacialise=input('enter the speacialise  ')
#         password=input('enter the password  ')
#         studint1=Studint(name,age,grade,city,speacialise)
#         print("information added succes")
#         print("added new croues")
#         coures=input('enter the coures  ')
#         print(studint1. addCorse(coures))
#         print(studint1)
#         students.append(studint1)
#         print(students)
#     elif userchoice==3:
#         break
#  
# #creat the class for product in market
class Product:
   def __init__(self,Name='defult',expire="9/9/2023",originprice=0.23,sellpersanteg=123):
    self.Name= Name
    self.expire=expire
    self.__originprice=originprice
    self.sellpersanteg=sellpersanteg
    # self.sellprice=originprice*sellprice
   def __str__(self):
       return f'name is{self.name} and expire {self.expire} and sellprice{self.sellprice}'
   def getsellprice(self):
      sellprice=self.__originprice*self.sellpersanteg
      return sellprice
Product1=Product('chips','8/9/2023',0.50,0.25)
print(Product1.Name)
print(Product1.getsellprice())

      

   