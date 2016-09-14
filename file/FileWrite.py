print "fileWrite"

my_file = open("new_file.txt","w")
my_file.write("first line")
my_file.close()

my_file = open("new_file.txt","a")
amount_content = my_file.write("first line")
print amount_content
my_file.close()


#Best practices
print "best practice of opening a file1"
try:
    my_file = open("new_file.txt","a")
    amount_content = my_file.write("first line")
    print amount_content
finally:
    my_file.close()
    
print "best practice of opening a file2"
with open("new_file.txt","r") as f:
    print (f.read())
    