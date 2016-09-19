class Cat:
    number = 0
    def __init__(self,color,legs):
        self.color = color
        self.legs = legs
        

felix = Cat("red",4)
felix.number = felix.number+2
print felix.color
print felix.legs
garf =Cat("b",3)
Cat.number = Cat.number+1
print Cat.number