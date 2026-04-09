import json

def to_json(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result, ensure_ascii=False)
    return wrapper

@to_json
def get_dict():
    return {"name": "Иван", "age": 25}

@to_json
def get_list():
    return [1, 2, 3, 4, 5]

print(get_dict())
print(get_list())