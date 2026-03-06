def sum(a, b=1):
    return a + b


print(sum(4, 6))


#find average by function

def calc_avg(a, b, c):
    return (a + b + c)/3

print(calc_avg(3,4,5))


#lambda function
num = lambda a,b: a + b
print(num(3,4))