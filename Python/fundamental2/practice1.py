#multiplication table

n = int(input('enter number: '))

i = 1

while i <= 10:
    print(n, " X ", i, " = ", n*i)
    i += 1


#count number of I's
word = 'Artificial intelligence'

ans = 0

for w in word:
    if w == 'i':
        ans += 1

print(ans)


#sum of n numbers
sum = 0
n = int(input('enter number: '))

for i in range(1,n+1):
    sum += i

print('sum of ', n, ' natural numbers is: ', sum)


#factorial of n
def calc_fact(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

n = int(input('enter a number: '))
print('factorial of ', n, ' is: ', calc_fact(n))