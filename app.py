# Object Oriented
# +class Object
# +self
# +constructor __init__
# Encapsulation 
# dir method
# add Attribute
# delete attribute
# delete Object 
# class attribute
# +getter setter
# +Access modifiers
# Inhertance
# method overrride...
# polymo


class Student:
    # nom age email uns....  attribute 
    __nom = None # public 
    __age = None   # protected
    __email = None  # private
     # constructor __init__
    """ def __init__(self,nom,age,email="a@a.com"):
        self.nom = nom
        self.age = age
        self.email = email """
        #setter
    def set_nom(self,v):
        self.nom = v
    def get_nom(self):
        return self.nom
    def set_val(self,value)  :
        if(type(value)==int):
            self.value = value 
        else: 
            print("the value is not Integer")    
        #getter
    def get_val(self) :
        return self.value
    def talk(self):   # Method Action function
        print(" my name is ?")
        
    def write(self):
        print(" my Name is ", self._age)
    
     
#std1 = Student("Ahmed",25,"ahmed@gmail.com")


#std2 = Student("Sara",15,"sara@gmail.com")


#std3 = Student("ali",13)


##################Encapsulation######################
# std4 = Student()
# std4.nom = "Imen"

# std4._age = 25

# std4.__email = "imen@gmail.com"
# print(std4.nom)
# print(std4._age)
# print(std4.__email)

std5 = Student()
std5.set_val(25)
std5.set_nom("Sara")
print(std5.get_nom())

print(std5.get_val())



