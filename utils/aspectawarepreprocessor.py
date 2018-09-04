# import the necessary packages
import cv2


class AspectAwarePreprocessor:
    def __init__(self, width):
        self.width = width

    def preprocess(self, image):
        r = self.width / image.shape[1]
        dim = (self.width, int(image.shape[0] * r))
        image = cv2.resize(image, dim, cv2.INTER_AREA)
        return image