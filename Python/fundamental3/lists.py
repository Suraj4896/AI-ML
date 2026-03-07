marks = [23, 56, 78, 45]
print(marks)
marks[2] = 99
print(len(marks))
print(marks[0:3])


#methods
marks.append(55)
marks.insert(2, 10)
marks.sort()
print(marks)
marks.sort(reverse=True)


#looping over lists
for i in marks:
    print(i)