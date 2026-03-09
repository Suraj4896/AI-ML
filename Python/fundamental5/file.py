f = open('example2.txt', 'a') #file object
f.write('world is cruel.')


f.close()

#with
with open('example.txt') as f2:
    print(f2.read())


#delete
import os
os.remove('example.txt')