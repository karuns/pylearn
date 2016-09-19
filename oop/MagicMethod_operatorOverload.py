# __init__ is one magic method. other magic methods are __add__ __multiply__

class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Vector2D(self.x+other.x,self.y+other.y)
    
    def __sad__(self,other):
        return Vector2D(self.x+other.x,self.y+other.y)
    
    def __mul__(self,other):
        return Vector2D(self.x * other.x,self.y * other.y)
    
    # Other magic methods are 
    """
        __sub__ -
        __mul__ *
        __truediv__ /
        __floordiv__ //
        __mod__ %
        __pow__ **
        __and__ &
        __or__ |
        __xor__ ^
        
        the expression x+y is translated to x.__add__(y)
        __lt__ <
        __le__ <=
        __gt__ >
        __ge__ >=
        __ne__ !=
        __eq__ ==
        
        __len__ len()
        __getitem__
        __setitem__
        __delitem__
        __iter__
        __contains__
        __call__
        __int__
        __str__
        
        Object life cycle
        __del__  decreases refrence count. when this count reaches to 0 python automatically free up memory.
        
    """ 


first = Vector2D(1,2)
second = Vector2D(5,6)

result1 = first+second
print result1.x
print result1.y

result1 = first * second
print result1.x
print result1.y


#first line is the only line changed
result2 = first.__sad__(second)
print result2.x
print result2.y

