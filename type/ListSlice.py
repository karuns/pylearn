
# list[first:last :step]
"""
First is inclusive
last index is exclusive 
anything is between is used for next operation. 
so if first is higher then second, then still above rule applies and any item in between is used for processing
value in negative then index is counted from last.
"""

squares = [1,2,3,4,5,6,7,8,9]
words = squares

#list slice
print(words[0:1])
print(words[1:4])
print(words[:4])
print(words[3:])

#Take the first item and then nth item after that 
print
print "special slice"
print(squares[::1])
print(squares[::2])
print(squares[::3])

# Negative value for first two (start and end then it shold be counted from end of string). 
#if it is sued for step then string is put in reverse order
print
print "negative slice"

print(words[0:-1]) #1-8
print(words[1:-4]) # 2-5
print(words[:-4]) #1-5
print(words[-3:]) # 7-9

print
print "negative slice reverse"
print(words[::-1]) #9-1
print(words[::-2]) #9,7,5,3,1
print(words[::-3]) #9,6,3

print(words[7:5:-1]) #9,6,3




