
def my_fun():
    print"a"
    print "b"
    print "c"

my_fun()


def print_with_exclaim(word):
    print(word+"!")
    
print_with_exclaim("word")
print_with_exclaim("pard")

a=5
def prints(x):
    x+=1
    print x
    
prints(a)
print(a)   


a=5
def prints2(x):
    x+=1
    print x
    return x
    
a= prints2(a)
print(a)  



def dd_number(x,y):
    total = x+y
    print total
    return total
    print "abcd"
dd_number(1,2)

func_var = dd_number
func_var(3,4)   

def print_2(func_var, x,y):
    return func_var(func_var(x,y),func_var(x, y)) 

print_2(func_var,3,2)
