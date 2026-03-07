info = [
    ('alice', 'math'),
    ('bob', 'science'),
    ('alice', 'science'),
    ('charlie', 'math'),
    ('bob', 'math'),
    ('alice', 'english'),
    ('charlie', 'english')
]

#unique courses
s = set()
for name, course in info:
    s.add(course)

print(s)

#student having course english
eng_students = []
for name, course in info:
    if course == 'english':
        eng_students.append(name)

print(eng_students)
print(type(eng_students))

#dictionary of students and their courses
course_dict = {}
for name, course in info:
    if(course_dict.get(name) == None):
        course_dict.update({
            name: set()
        })
    course_dict[name].add(course)
    

print(course_dict)

#palindrome string
str = input('enter a string: ')
rev_str = str[::-1]
if str == rev_str:
    print('palindrome')
else:
    print('not a palindrome')

#merge list
list1 = [1, 2, 7]
list2 = [2, 4, 5]

list3 = list1 + list2
list3.sort()
print(list3)

#touple
top = (2,5,7,8,10,4,77)
even_tup = []
odd_tup = []

for t in top:
    if t % 2 == 0:
        even_tup.append(t)
    else:
        odd_tup.append(t)

print(tuple(even_tup), tuple(odd_tup))

#marks
info = {}
def update_dict(key):
    if key == 'A':
        name = input('enter a name: ')
        info.update({name: 0})
    elif key == 'B':
        name = input('enter a name: ')
        mark = int(input('enter mark: '))
        info[name] = mark
    elif key == 'C':
        name = input('enter a name: ')
        if info.get(name) == None:
            print('not found')
        else:
            print('found')
    else:
        print(info)


while True:
    key = input('enter key (A/B/C/D/E to exit): ')

    if key == 'E':
        break

    update_dict(key)


#spaces
str = input('enter a string: ')
spaces = str.count(" ")

        
#duplicate elements
lst = [1, 2, 3, 2, 4, 5, 1, 6, 3]

seen = set()
duplicates = set()

for item in lst:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print("Duplicate elements:", duplicates)
