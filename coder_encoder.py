import json
import base64

data = {}
with open('src/cat.jpg', mode='rb') as file:
    img = file.read()
data['img'] = base64.encodebytes(img).decode('utf-8')

print("hello")
print(json.dumps(data))
