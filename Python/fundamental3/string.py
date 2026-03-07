word = "python"

#length of string
print(len(word))

#accessing each character
for i in range(len(word)):
    print(word[i])


#slicing
print(word[2:5])
print(word[-4:-1])

#string formatting
a = 10
b = 23
sum = a + b
print('sum of {} and {} is {}'.format(a, b, sum)) #format function
print('sum of {1} and {0} is {2}'.format(a, b, sum)) #index based format
print('sum of {a} and {b} is {sum}'.format(a=4, b=6, sum=10)) #value based format

#format by f-strings
print(f'sum of {a} & {b} is {a+b}')
