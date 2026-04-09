import json
import yaml
import dicttoxml

def to_format(format_type=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if format_type == "json" or format_type is None:
                return json.dumps(result, ensure_ascii=False)
            elif format_type == "yaml":
                return yaml.dump(result, allow_unicode=True)
            elif format_type == "xml":
                return dicttoxml.dicttoxml(result).decode()
            return result
        return wrapper
    return decorator

@to_format("json")
def get_data_json():
    return {"name": "Петр", "age": 30}

@to_format("yaml")
def get_data_yaml():
    return {"name": "Анна", "age": 25}

print(get_data_json())
print(get_data_yaml())