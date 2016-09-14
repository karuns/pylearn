#Dictionary

ages = {"a":3,"b":"bb","c":4}
print ages["a"]
print ages.get("a")
print ages["b"]
print ages.get("b")
# print ages["dd"]
print ages.get("dd") #None
print ages.get("dd","custome message if not found")
print ages.get("a","custom value if not found")

#check key
print ages.has_key("c")
print "c" in ages
print ages.has_key("d")
print "d" in ages

#add item to dictionary
ages[8] = 8
ages[9]= 9
print ages





