# Assertion check
print ("assertion without comment")

print(1)
assert True
print (2)
assert 2+2 ==4
print (3)
# assert 2+2==5

#Assert with comment ad inside try catch, finally block with raise
try:
    print("Assert with comment")
    print(1)
    assert True, "this comment should not be printed"
    print(2)
    assert False,"this comment Should be printed"
    print(3)
except:
    print 98
    raise
finally:
    print(99)
