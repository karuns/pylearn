words = ["a","b","c","d","e"]

#list slice
print(words[0:1])
print(words[1:4])
print(words[:4])
print(words[3:])

words[1] = "e"
print words

words = words+[1,2]
print words

words.append([2,3])
print words

print len(words)
print len(words[3])

words.insert(2, ["l","m"])
print words
words.append("a")

#print words.index('cs') 
print "index="+ str(words.index('c'))
print words.count("a")

print "max="+max(words)
print "min="+str(min(words))
words.remove("a")
print "remove"
print words
words.reverse()
print words

word = ["a",]
print word

my_str = "Hello, World"
print(my_str[7])
print my_str

print("a" in words)
print ("a" not in words)
print (not "a" in words)
