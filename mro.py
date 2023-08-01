class A:
    def do_this(self):
        print("Doing this in Class A")
        
class B(A):
    pass

class C:
    def do_this(self):
        print("Doing this in Class C")
        
class D(B,C):
    pass

obj = D()
obj.do_this()