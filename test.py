import json

python_data = {
    "name" : "izqia",
    "roll_no" : 247719
}

load_data = json.dumps(python_data)
print(load_data)

parsed_data = json.loads(load_data)
print(parsed_data)
print(type(parsed_data))