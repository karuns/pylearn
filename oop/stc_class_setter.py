class Rectangles:
    def __init__(self,a,b):
        print "something"
        print a
        print b
         
     
    @staticmethod
    def print_something(top):
        print top
    
    @classmethod
    def print_something_else(cls,top):
        return cls(top,top) 
    
    # property makes attribute read only
    @property
    def pineapple_allowed(self):
        return False
    
    @pineapple_allowed.setter
    def pineapple_allowed(self,value):
        self.pineapple_allowed = value
    
    
    
 
print("te")
Rectangles.print_something("23")
r = Rectangles(4,5)
print r.print_something_else("B")
