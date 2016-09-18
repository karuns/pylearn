# decorators are the functions which modifies other function 

def decor(func,x):
    def format():
        print("=========")
        func(x)
        print("=========")
    return format

#first way of calling decor
def print_text(x):
    print(x)
dec = decor(print_text,"Hello, World")
dec()


print "second way of doing sam"
# @decor

