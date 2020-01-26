from .ImageToGrayscale import ImageToGrayscale
from .GrayscaleToAscii import GrayscaleToAscii
import pyvips
import numpy as np
import time
from PIL import Image

class ImageToAscii:
    def __init__(self, imagePath):
        # convert image in grayscale
        self.imageToGray = ImageToGrayscale(imagePath)
        # than this will convert it into text
        self.grayToAscii = GrayscaleToAscii()

        # and after that this will convert text into image(png, jpg, ...)
        self.asciiToImage = None
        #
    def change_focus_image(self, imagePath):
        self.imageToGray.__init__(imagePath)


    # grayscale array
    def get_grayscaleArray(self):
        return self.imageToGray.arrayImage

    def resize_grayscaleArray_h(self, width, height):
        self.imageToGray.resize_h(width, height)

    def resize_grayscaleArray(self, basewidth):
        self.imageToGray.resize(basewidth)
    # array of ascii chars
    def get_asciiArray(self):
        """
        :return: numpy array with chars
        """
        return self.grayToAscii.arrayAscii

    def save_asciiText(self, filename):
        self.grayToAscii.save(filename)

    # image of pixel but its ascii
    def get_asciiImage(self):
        return self.asciiToImage

    def save_asciiImage(self, filename, scale=1):
        # resize image to original sizes
        self.asciiToImage = self.asciiToImage.resize(scale)
        #  make bg white and text black

        self.asciiToImage.write_to_file(filename)

    def convert(self, time_dublicate = 1,
                textcolor=[0,0,0], backgroundcolor=[255,255,255],
                **kwargs):
        """
        this convert image to Ascii png
        original width / original height = your width / calced height
        :param filename: path to save ascii image
        :param time_dublicate: dublicate char in ascii txt (except '\n')
        :param kwargs: for pyvips.Image.text
        :return: None
        """
        self.imageToGray.convert()
        self.grayToAscii.convert(self.get_grayscaleArray(),
                                 times_dublicate=time_dublicate)

        # it s tuple, we convert it into string
        textAscii = str(self.grayToAscii.get_text())
        self.asciiToImage = pyvips.Image.text(
            textAscii, **kwargs,
        )

        # recolor image
        self.asciiToImage = self.asciiToImage.ifthenelse(
            textcolor, backgroundcolor, blend=True
        )


if __name__ == '__main__':
    start_time = time.time()
    # 300 px
    # 2.457428455352783 vs 2.7407114505767822
    # 500 px
    # 11.001618385314941 vs 10.7692391872406 vs
    # todo convert list into numpy array in gray to ascii
    # 600 px
    # 37.03298568725586 vs 42.14830756187439 vs 7.7971556186676025 vs 8.37460708618164 vs 9.05478835105896
    app = ImageToAscii(r'C:\Users\Lenovo\OneDrive\Pictures\Saved Pictures\Alan-Turing-passport-1200x720.jpg')
    origin_width = app.get_grayscaleArray().shape[1]
    new_width = 400
    app.resize_grayscaleArray(new_width)

    app.convert(2, font='consolas')
    im = Image.fromarray(app.get_grayscaleArray())
    new_width = app.get_asciiImage().width
    app.save_asciiImage(r'alan turing.png',
                        scale=origin_width/new_width*0+1)
    print(time.time()-start_time, " second")