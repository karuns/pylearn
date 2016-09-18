# sets are very similar to list etc. however it wouldn't have repeated elements
# List[] dictionary{key:value,}, tuples(), set {}
num_set = {1,2,3,4,5}
string_set = set(["a","b","c","d",1,"b"])

print num_set
print string_set

num_set.add(6)
print num_set
num_set.pop()
print num_set
num_set.remove(4)
print num_set

print
print
print 
print"more on set"

first = {1,2,3,4,5,6}
second = {4,5,6,7,8,9}

#or
print(first|second)  
print(first & second)
print(first - second)
print (second - first)

# non common on both
print (first ^ second)
