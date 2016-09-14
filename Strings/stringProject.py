def count_char(text, char):
    count = 0
    for c in text:
        if c==char:
            count = count+1
    return count

def count_char2(text,char):
    return len(text.split(char))-1
    
print count_char("abcdabcdab", "a")
print count_char2("abcdabcdab", "a")


print "how many time a character appear in string "
c = raw_input("enter char:")
#c="a"
with open("charactercount.txt","r") as f:
    text = f.read()

print count_char(text,c)
print count_char2(text,c)


print "what percentage of each character appear in file"
for c in "abcdefghijklmnopqrstuvwxyz":
    print "charact {0} appear {1}%times".format(c,count_char(text, c)*100/len(text))
print len(text)


    