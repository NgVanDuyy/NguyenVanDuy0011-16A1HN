import json
# Chuỗi JSON bao quanh bằng dấu nháy đơn
json_string_1 = '{"name": "A", "age": 35, "company": "Đất Việt"}'
# Chuỗi JSON bao quanh bằng dấu nháy kép
json_string_2 = "{\"name\": \"A\", \"age\": 35, \"company\": \"Đất Việt\"}"
# Chuyển chuỗi JSON thành đối tượng Python (đối tượng JSON)
json_object_1 = json.loads(json_string_1)
json_object_2 = json.loads(json_string_2)
print(json_object_1)
print(json_object_2)