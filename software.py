import Pyro4
import cv2
import base64
import numpy as np


@Pyro4.expose
class EditImage(object):
    def get_image(self, img):
        image = base64.b64decode(img["data"])
        nparr = np.frombuffer(image, np.uint8)
        src = cv2.imdecode(nparr, flags=1)
        ksize = (10, 10)
        src = cv2.blur(src, ksize)
        window_name = 'Image'
        cv2.imshow(window_name, src)
        cv2.waitKey(5000)
        return image

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(EditImage)
ns.register("edit.image", uri)
daemon.requestLoop()


class ImageEditor():
    def __init__(self, img):
        self.image = img