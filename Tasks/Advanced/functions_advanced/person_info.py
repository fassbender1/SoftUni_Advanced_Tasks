# def get_info(**kwargs):
#
#     return f"This is {kwargs['name']} from {kwargs['town']} and he is {kwargs['age']} years old"
#
#
# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))

def get_info(**kwargs):
    person = {}
    for key, value in kwargs.items():
        person[key] = value
    return f"This is {person['name']} from {person['town']} and he is {person['age']} years old"

