# Object Oriented
# class Object
# self
# constructor __init__
# Encapsulation 
# dir method
# add Attribute
# delete attribute
# delete Object 
# class attribute
# getter setter
# Access modifiers
# Inhertance
# method overrride...
# polymo


class Student:
    # nom age email uns....  attribute 
    nom = None
    age = None
    email = None
     # constructor __init__
    def __init__(self,nom,age,email="a@a.com"):
        self.nom = nom
        self.age = age
        self.email = email
        
    def talk(self):   # Method Action function
        print(" my name is ?")
        
    def write(self,name):
        print(" my Name is ", name)
    
     
std1 = Student("Ahmed",25,"ahmed@gmail.com")


std2 = Student("Sara",15,"sara@gmail.com")


std3 = Student("ali",13)
std3.email = "Ali@gmail.com"

std1.write(std1.nom)
std1.write(std2.nom)
std3.write(std3.email)

##################Encapsulation######################


