import uuid

import Pyro4
import cv2
import base64
import numpy as np

# python -m Pyro4.naming
# python software.py
# uvicorn server:app --reload


@Pyro4.expose
class EditImage(object):
    def __init__(self):
        self.data = []


    def upload_image(self, img):
        id = uuid.uuid4()
        self.data.append({"id": id,
                          "source_image": img["data"],
                          "blured_image": '',
                          "searched_image": ''})
        self.blur_image(id)
        return {"status": 200, "id": id.hex, }

    def blur_image(self, id):
        for item in self.data:
            if item["id"] == id:
                image = base64.b64decode(item["source_image"])
                nparr = np.frombuffer(image, np.uint8)
                src = cv2.imdecode(nparr, flags=1)
                ksize = (10, 10)
                src = cv2.blur(src, ksize)
                window_name = 'Image'
                cv2.imshow(window_name, src)
                cv2.waitKey(5000)
                item["blured_image"] = src
        print(item["id"])

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(EditImage)
ns.register("edit.image", uri)
daemon.requestLoop()




