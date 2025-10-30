import json
from fastapi import Depends, FastAPI


json_string = '{"name": "Sample, "age": 30, "city": "New York"}'
python_dict = json.loads(json_string)

print(python_dict)
print(type(python_dict))