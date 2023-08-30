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
# class Product:
#    def __init__(self,Name='defult',expire="9/9/2023",originprice=0.23,sellpersanteg=123):
#     self.Name= Name
#     self.expire=expire
#     self.__originprice=originprice
#     self.sellpersanteg=sellpersanteg
#     # self.sellprice=originprice*sellprice
#    def __str__(self):
#        return f'name is{self.name} and expire {self.expire} and sellprice{self.sellprice}'
#    def getsellprice(self):
#       sellprice=self.__originprice*self.sellpersanteg
#       return sellprice
# Product1=Product('chips','8/9/2023',0.50,0.25)
# print(Product1.Name)
# print(Product1.getsellprice())

# class techaer:
#     def __init__(self,Name,course):
#         self.Name=name
#         self.course=course
        
    
# class student(techaer):
#     def __init__(self,name,course):
#         self.Name=name
#         self.course=course
            
#     super().techaer(Name,cou
   


# class Animal:
#     def __init__(self,name,eat):
#         self.Animalname=name
#         self.Animaleat=eat
#     def __str__(self):
#          return f'name is{self.Animalname} and {self.Animaleat}'
# class Dog(Animal):

#     def __init__(self, name, eat):
#         super().__init__(name, eat)
#         self.name=name
#         self.eat=eat
#     def __str__(self):
#         return f'name is {self.name} and eat is {self.eat}, animal name is{self.Animalname} and animal eat{self.Animaleat}'

# obj1=Dog('Husky','meat')
# print(obj1.name)
# print(obj1.eat)

# class squer:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def area(self):
#         return self.x*self.y

# class rectangle(squer):
#     def __init__(self,y,x):
#         self.y=y
#         # self.x=x
#         super().__init__(x,y)
    
#     # def area(self):
#     #     return super().area()
#     def arearectangle(self):
#         return self.x*self.y
# obj1=squer(10,4)
# print(obj1.area())
# obj2=rectangle(10,5)
# print(obj2.arearectangle())


<<<<<<< HEAD
# class Animals:
#     def __init__(self,name,type):
#         self.name=name
#         self.type=type
#     def __str__(self):
#         return f'name is {self.name} and type is {self.type}'
#     def __eq__(self,other):
#         return self.name==other.name and self.type==other.type
# Animal1=Animals('cat','mamal') 
# print('animal 1',Animal1)
# Animal2=Animals('cat','mamal')
# print('animal 2',Animal2)
# print('check if equal or not', Animal1==Animal2)
# print('check obj 1 type',type(Animal1))
# print('check obj 2 type',type(Animal2))    

# print('check obj 1 memory location ',id(Animal1))       
# print('check obj 2 memory location ',id(Animal2))    

# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# # def name():
# #     print('hi from tkinter')
# ttk.Label(frm, text="Hello World!").grid(column=1, row=1)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

from tkinter import *
Window=Tk()
Window.title('welcome to likeGeeks app')
Window.geometry('350x200')
lbl=Label(Window, text='Hello')
lbl.grid(column=0,row=0)
count1=0
def clicked():
    global count1
    count1 +=1
    print(count1)
    lbl.configure (text=f"count{count1}")
input = Entry(Window,width=10)
inputtext= Text(Window,height=5,width=20)
inputtext.pack()
btn=Button(Window, text="click Me" , command=clicked)
btn.grid(column=1, row=0)
Window.mainloop()
=======
class father:
    def __init__(self,name,age,haircolor):
        self.fathername=name
        self.fatherage=age
        self.haircolor=haircolor
    def __str__(self):
        return f'father is name{self.fathername} and fatherage{self.fatherage}and haircolor{self.haircolor}'
class mother:
    def __init__(self,name,age,eyecolor):
        self.mothername=name
        self.motherage=age
        self.eyecolor=eyecolor    
    def __str__(self):
        return f'mother name is{self.mothername} and age{self.motherage} and eyecolor{self.eyecolor}'
class partty:
    def __init__(self,location):
        self.location=location
    def __str__(self):
        return self.location

class son(father,mother,partty):
    def __init__(self,name,age,fathername,fatherage,haircolor,mothername,motherage,eyecolor,location):
        father.__init__(self,fathername,fatherage,haircolor)
        mother.__init__(self.mothername,motherage,eyecolor)
        partty.__init__(self,location)
        self.name=name
        self.age=age
    def __str__(self):
        return f'name is {self.name} and age{self.age}'
    
    


son1=son('basel',20,'ali',50,'black','nina',40,'blue','jordan')
print(son1)
>>>>>>> 0c53136af91a64fd1f1705790895a8e6c1cc6420
