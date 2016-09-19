class Animal:
    def __init__(self,name,legs):
        self.name = name
        self.legs = legs
    def sound(self):
        print("not sure")
    
class Cat(Animal):
    def sound(self):
        print "purr"

class Dog(Animal):
    def sound(self):
        print "woof"
#         super(Animal, self).sound()
        

# fid = Dog("fido",4)
# print fid.name
# fid.sound()
# 
# gar = Cat("garf",4)
# print gar.name
# gar.sound()


        