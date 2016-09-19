"""

Data hiding or encapsulation is done using _<method name>. this is just notificaiton to caller .however this doesn;t restrict user from strictly calling it.
one underscrore is weak private method/variable
two underscore is strong privagte method
"""
class Spam:
    __eggs =7
    def print_something(self):
        print("egg")
    
    def __strong_pv_method(self):
        print "Strong pv method"
        

s = Spam()
s.print_something()

#Note here how is strong private mewthod is called. _<class name> is prefixed so method name looks like _Spam_<method name>
s._Spam__strong_pv_method()