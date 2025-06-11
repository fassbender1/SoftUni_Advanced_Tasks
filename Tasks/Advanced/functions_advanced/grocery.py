def grocery_store(**kwargs):
    sorted_result = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))
    result = ""
    for key, value in sorted_result:
        result += f"{key}: {value}\n"
    return result


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12
))