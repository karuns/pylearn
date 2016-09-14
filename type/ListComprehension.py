
print "simple list comprehension"
words = [i*i for i in range(5)]
print words

print
print "list comprehension with if"
words = [i*1 for i in range(10) if i%2==0 ]
print words