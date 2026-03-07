dict = {
    'name': 'suraj',
    'age': 23,
    'height': 178,
    3.14: 'PI'
}

print(dict)
print(dict['age'])

#methods
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get('name'))
dict.update({
    'city': 'Puri'
})
print(dict)