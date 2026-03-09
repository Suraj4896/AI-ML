import json
json_str = '{"name": "Suraj","isTeacher": false}'
dict = {
    'name': 'suraj',
    'age': 23
}
#for dealing with string values
#converts json to python dictionary
py_obj = json.loads(json_str)
#converts dict to json
json_data = json.dumps(dict)
print(type(py_obj))
print(py_obj)

print(type(json_data))
print(json_data)

#dealing with json file
dict2 = {
    'name': 'suraj',
    'isTrue': True
}
with open('data.json') as f:
    py_obj1 = json.load(f) #read the jason file and convert to dict
    print(py_obj1)


with open('data.json', 'w') as f:
    json.dump(dict2, f, indent=2, sort_keys=True) #write the dict to the json file