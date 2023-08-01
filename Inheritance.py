class Car:
    def __init__(self,company,owner,color,speed) :
        self.company = company
        self.owner = owner
        self.color = color
        self.speed = speed
        
    def move(self):
        print("the Car has moved")
    
    def stop(self):
        print("the Car has Stoped")
    

class Truck(Car):
    pass
    
        
    
    
class Vehicle(Car):
    pass

class OS:  # Sup class Parent Class
    
    def __init__(self,company,version,annee) :
        self.company = company
        self.version = version
        self.annee= annee
        
    def start(self):
        pass
    
    def stop(self):
        pass
    
    def display(self):
        print("This is OS System")

    
    
class Windows(OS):  # Sub Class Child class 
    # def display(self):
    #     print("This is Windows System")
    pass

class MacOS(OS):
    def display(self):
        print("This is Mac System")


class Linux(OS):
    def display(self):
        print("This is Linux System")


class Ubuntu(Linux) :
    def display(self):
        print("This is Ubuntu System")

       
w = Windows("MicoSoft",11,2019)
m = MacOS("Appel",15.2,2021)
l = Linux("Redhat",9,2009)
u = Ubuntu("Ubuntu",23.04,2023)


w.display()
m.display()
l.display()
u.display()
        
        
# c = Car("Jeeb","sara","Black",150)

# print(c.company)

# t = Truck("Jeeb-Truck","ahmed","Blue",80)
# print(t.company)
    