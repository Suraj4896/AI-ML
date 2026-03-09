try:
    x = int(input('enter x: '))
    ans = 10/x
except ZeroDivisionError:
    print('devide by 0...')
else:
    print('program terminate successfully...')
finally:
    print('end of program')