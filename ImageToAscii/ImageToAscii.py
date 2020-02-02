from .ImageToGrayscale import ImageToGrayscale
from .GrayscaleToAscii import GrayscaleToAscii
import pyvips
import numpy as np
import time
import re
import cv2
from PIL import Image

class ImageToAscii:
    def __init__(self, image):
        # convert image in grayscale
        self.imageToGray = ImageToGrayscale(image)
        # than this will convert it into text
        self.grayToAscii = GrayscaleToAscii()

        # and after that this will convert text into image(png, jpg, ...)
        self.asciiImage = None
        #
    def set_image_by_path(self, imagePath):
        self.imageToGray.set_arrayImage(cv2.imread(imagePath, 0))
    
    def set_image(self, arrayImage):
        # change focus array image, but not throught path
        self.imageToGray.set_arrayImage(arrayImage)

    def resize_grayscaleArray(self, width, height):
        self.imageToGray.resize(width, height)

    def resize_grayscaleArray_scale(self, scale):
        self.imageToGray.resize_scale(scale)
    
    def resize_asciiImage(self, scale):
        self.asciiImage = self.asciiImage.resize(scale)

    # image of pixel but its ascii
    def get_asciiImage(self):
        return self.asciiImage
    # grayscale array
    def get_grayscaleArray(self):
        return self.imageToGray.arrayImage
    def get_asciiArray(self):
        """
        :return: numpy array with chars
        """
        return self.grayToAscii.arrayAscii

    def save_asciiText(self, filename):
        self.grayToAscii.save(filename)
    
    def save_asciiImage(self, filename, scale=1):
        # resize image to original sizes
        self.asciiImage = self.asciiImage.resize(scale)
        #  make bg white and text black

        self.asciiImage.write_to_file(filename)

    def convert(self, time_dublicate = 1,
                textcolor=[0,0,0], backgroundcolor=[255,255,255],
                **kwargs):
        """
        this convert image to Ascii png
        :param time_dublicate: dublicate char in ascii txt (except '\n')
        :param kwargs: for pyvips.Image.text(kwargs)
        :return: None
        """
        self.imageToGray.convert()
        self.grayToAscii.convert(self.get_grayscaleArray(),
                                 times_dublicate=time_dublicate)

        textAscii = self.grayToAscii.get_text()
        # render image
        self.asciiImage = pyvips.Image.text(
            textAscii, **kwargs,
        )

        # recolor image
        self.asciiImage = self.asciiImage.ifthenelse(
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
    im = Image.open(r'C:\Users\Lenovo\OneDrive\Pictures\Saved Pictures\Alan-Turing-passport-1200x720.jpg')
    app = ImageToAscii(im)
    origin_width = app.get_grayscaleArray().shape[1]
    new_width = 400
    app.resize_grayscaleArray(new_width)

    app.convert(2, font='consolas')
    im = Image.fromarray(app.get_grayscaleArray())
    new_width = app.get_asciiImage().width
    
    app.save_asciiImage(r'alan turing.png',
                        scale=origin_width/new_width*0+1)
    print(time.time()-start_time, " second")