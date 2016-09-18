# Count , Cycle, repeat, accumulate, takewhile

#Count  takes initial value and  keeps on incrementing
from itertools import count, takewhile,permutations,product


for i in count(3):
    print i
    if(i>=10):
        break
    
# accumulate will accumulate list so 
#print(list(accumulate(range(8)))) would be 
nums = [0,1,2,3,6,12,18]

#takwhile is very much like filter method
print (list(takewhile(lambda x : x<=6,nums)))


# Product will do product and so perumtations will
print "product"
letters = ["A","B","C"]
print list(product(letters, range(3)))
a = list(product(letters, range(3)))
print a[0][0]


print "permutations"
print list(permutations(letters))