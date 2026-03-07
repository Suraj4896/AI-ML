tup = (1,2,3,4,5,2,3,4,4,3)
print(tup)
print(type(tup))

#methods
print(tup.index(2))
print(tup.count(4))

sum = 0
for val in tup:
    sum += val