from PIL import Image
import numpy as np
import sys
import time

class ImageToGrayscale:
    # ROUND_BRIGHTNESS = {
    #     223: 255,  # white
    #     191: 200,  # white white white black
    #     159: 150,  # white white black
    #     128: 128,  # gray
    #     96: 100,  # black black white
    #     64: 50,  # black black black white
    #     0: 0,  # black
    # }
    # ROUND_BRIGHTNESS = {
    #     239 : 255,
    #     223 : 225,
    #     207 : 210,
    #     191 : 192,
    #     175 : 175,
    #     159 : 160,
    #     143 : 150,
    #     127 : 130,
    #     111 : 112,
    #     95 : 100,
    #     79 : 80,
    #     63 : 64,
    #     47 : 50,
    #     31 : 32,
    #     15 : 16,
    #     0 : 0
    # }
    ROUND_BRIGHTNESS = {
        239: 255,
        207 : 210,
        175: 175,
        143: 150,
        127: 130,
        111: 112,
        79: 80,
        31: 32,
        15: 16,
        0: 0
    }
    def __init__(self, image):
        self.arrayImage = np.array(image.convert("L"))
    
    def changeArrayImage(self, image):
        self.arrayImage = np.array(image.convert("L"))

    def convert(self):  # roundValues
        shape = self.arrayImage.shape
        for row in range(shape[0]):
            for col in range(shape[1]):
                # round value of pixel
                self.arrayImage[row][col] = self.pixelRound(self.arrayImage[row][col]);
        # self.image = Image.fromarray(arrayIm)
        # return arrayIm

    @staticmethod
    def pixelRound(value):
        # todo make round_brightness as CONSTANT in class
        # key is compared( > ) value and value is tochange value
        for key in ImageToGrayscale.ROUND_BRIGHTNESS:
            if value >= key:
                return ImageToGrayscale.ROUND_BRIGHTNESS[key]

    def save(self, imagePath):
        image = Image.fromarray(self.arrayImage)
        image.convert("RGB").save(imagePath)

    def resize(self, basewidth):
        image = Image.fromarray(self.arrayImage)
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), Image.ANTIALIAS)
        self.arrayImage = np.array(image)

    def resize_h(self, width, height):
        image = Image.fromarray(self.arrayImage)
        image = image.resize((width, height), Image.ANTIALIAS)
        self.arrayImage = np.array(image)

if __name__ == '__main__':
    image = ImageToGrayscale(r"images\aqua_(konosuba).jpg")
    image.convert()

    im = Image.fromarray(image.arrayImage)
    im.show()

    image.save("method_2.png")
    image.resize(500)

    im = Image.fromarray(image.arrayImage)
    im.show()

