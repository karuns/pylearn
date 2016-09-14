print("File")
#Modes r,w,a,b (b is binary mode) most of this mode can be used together
my_file = open("input.txt","r")
# my_data = my_file.read()
# 
# print "printing whole file"
# print my_data  
#if you try to read file after it has reached end of line then it would print blank line
print "printing only specific bytes"
print my_file.read(5)

print
print "printing line by line"
my_file.close()

print "read line by line"
my_file = open("input.txt","r")
mylist  = my_file.readlines()
print mylist
my_file.close


print "list"
my_file = open("input.txt","r")
mylist  = my_file.readlines()
print mylist
my_file.close

print "read line by line"
my_file = open("input.txt","r")
for line in my_file:
    print line
my_file.close

