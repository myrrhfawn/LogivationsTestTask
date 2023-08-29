import Pyro4
import cv2
import base64



@Pyro4.expose
class EditImage(object):
    def get_image(self, img):

        return img

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(EditImage)
ns.register("edit.image", uri)
daemon.requestLoop()


