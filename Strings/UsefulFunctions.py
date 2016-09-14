#join
print (",".join(["a","b","c"]))

#Split
print ("a,b,c".split(","))

#Replace 
print "Hello Me".replace("Me", "world")

#starts with , ends with
print "Does this sentence starts with".startswith("Does")
print "Does this sentence starts with".endswith("with")

#upper and lower
print "Does this sentence starts with".upper()
print "Does this sentence starts with".lower()


print
print "numeric function min, max, abs, sum,round"
print min(1,2,3,4,5)
print max([1,2,3,4,5])
print abs(-99)
print abs(99)
print sum([1,2,3,4])
print round(1.2)
print round(1.6)

print
print "all, any & enumerate functions"
nums = [55,44,33,22,11,5]

if all (i>5 for i in nums):
    print "all nums greatr than 5"

if any (i%2 ==0 for i in nums):
    print "at least one number is enum"
    
for v in enumerate(nums):
    print v
    
if all (i>5 for i in nums if i>5):
    print "all nums greatr than 5"
