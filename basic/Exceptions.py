# Raise exception
print
print "Raise exception ==="
print 1
# raise ValueError    # specific exception can be raised anytime
print 2   


# print 3
# raise       # it is important to pass type of exception otherwise basic will just halt here without any exception
# print 4


# print 3
# raise ValueError("Example of giving details to exception") # Can write some comments along with exception
# print 4


try:
    print(1/0)
except:
    raise # re raising exception


# Try Except, finally block
print
print "Try Except Finally ==="
try:
    print("finally")
    
    print (1/0)
except ZeroDivisionError:
    print("ZDE")
finally:
    print("executing finally block")


try:
    print("finally with error")
    print (1/0)
except ZeroDivisionError:
    #print(1/0)
    print ("zd")
finally:
    print("executing finally with double error block")


# try except block
print
print "Try Except Block ==="
try:
    num1 = 7
    num2 = 0
    print (num1/num2)
except:
    print("exception occured") 
    print num1
    
try:
    num1 = 7
    num2 = 0
    print (num1/num2)
except ZeroDivisionError:
    print("exception occured") 
    print num1   

try:
    variable = 10
    print (variable+"a")
except ZeroDivisionError:
    print("zd")
except:
    print("type error")
 

try:
    variable = 10
    print (variable+"a")
except ZeroDivisionError:
    print("zd")
except TypeError,ValueError:
    print("type error")
except:
    print("this should not be printed")
    
    
