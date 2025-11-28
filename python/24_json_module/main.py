import json

# covert json in to python object
json_str = '{"name": "Meet desai","age": 24}'

py_obj = json.loads(json_str)

print(py_obj)

# convert python object in to json
py_obj2 = {
    "married": False,
    "country": "India",
    "job": None
}
conver_json = json.dumps(py_obj2)
print(conver_json)


# red json file
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)
f.close()

# overwrite json file
with open('data.json', 'w') as f:
    json.dump(py_obj2, f, indent=4, sort_keys=True)
f.close()
