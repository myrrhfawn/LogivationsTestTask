import urllib

import Pyro4
import base64

data = {}
with open('src/cat.jpg', mode='rb') as file:
    img = file.read()
    print(img[:20])

data['img'] = base64.b64encode(img)

print(data["img"][:20])

data["img"] = base64.b64decode(data["img"]) #ANSWEr
print(data["img"][:20])

"""
#edit_image = Pyro4.Proxy("PYRONAME:edit.image")
#response = edit_image.get_image("gggg")

#print(response)
import cv2
import json


print(type(data["img"]))

#print(data["img"])

import numpy as np

#nparr = np.frombuffer(data["img"], dtype=np.uint8)

#print(type(nparr))
#src = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

#cv2.imwrite("image.jpg", data["img"])

src = cv2.imread(data["img"])
print(src)
window_name = 'Image'
ksize = (10, 10)
src = cv2.blur(src, ksize)
cv2.imshow(window_name, src)
cv2.waitKey(5000)

print("blured")
"""
import numpy as np
import cv2

# Load image as string from file/database

# CV2
nparr = np.frombuffer(data["img"], np.uint8)
src = cv2.imdecode(nparr, flags=1)

#src = cv2.imread(nparr)
window_name = 'Image'
ksize = (10, 10)
src = cv2.blur(src, ksize)
cv2.imshow(window_name, src)
cv2.waitKey(5000)


# check types
print(type(nparr))

print(type(data["img"]))
