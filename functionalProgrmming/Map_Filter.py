#Map
nums = [5,7,2,4]

def add_5(x):
    return x+5

print(list(map(add_5,nums)))


# Filter

nums = [5,7,2,4]
def if_even(x):
    return (x %2==0)

""" Functio nreturns true """
print list(filter(lambda x:True,nums))  
print list(filter(if_even,nums))
    