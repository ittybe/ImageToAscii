import cv2
import numpy as np
from .ImageToGrayscale import ImageToGrayscale
import time
import re
class GrayscaleToAscii:
    # chars for replace pixels
    CHARS_MAP = None
    CHARS = ' .+=*!%#$@'
    DUB_FILL = '\0'
    def __init__(self):
        # in class static method doesnt work
        if self.CHARS_MAP == None:
            # ' -=*@#%'
            # ' -~/+=*$#%@'
            self.CHARS_MAP = self.create_chars_map(self.CHARS)
        self.arrayAscii = None

    @staticmethod
    def create_chars_map(chars):
        values = ImageToGrayscale.ROUND_BRIGHTNESS.values()
        if len(chars) != len(values):
            raise IndexError(f"values {values} not equel chars '{chars}' ")
        pairs = zip(values, chars)
        return {key:value for key, value in pairs}

    def convert(self, arrayImage, times_dublicate = 1):
        """
        :return: None
        """
        # list: we need to change "col" value for '\n' char
        shape = list(arrayImage.shape)
        shape.append(times_dublicate) # append: for 3 d array
        shape[1] += 1  # '\n' char
        self.arrayAscii = np.chararray(shape)
        shape[1] -= 1  # '\n' char

        for row in range(shape[0]):
            for col in range(shape[1]):
                # convert pixel into ascii char and
                for dublicate in range(times_dublicate):
                    self.arrayAscii[row][col][dublicate] = self.CHARS_MAP[arrayImage[row][col]]
            # last elem
            self.arrayAscii[row][shape[1]][0] = '\n'
            # fill void in '\n' array
            for dublicate in range(1, times_dublicate):
                self.arrayAscii[row][shape[1]][dublicate] = self.DUB_FILL

    def get_text(self):
        # get very long string and it's tuple, we convert it into string by str()
        textAscii = str(self.arrayAscii.astype('|S1').tostring().decode('utf-8'))
        # remove all DUBLICATE FILLING chars
        textAscii = re.sub(GrayscaleToAscii.DUB_FILL, '',textAscii)
        return textAscii
    
    def save(self, Asciipath, times_dublicate = 1):
        file = open(Asciipath, 'w')
        arraySave = self.get_text()
        file.write(arraySave)
        # if times_dublicate != 1:
        #     for col in arraySave:
        #         for char in col:
        #             # dont dublicate '\n' char
        #             if char == '\n':
        #                 file.write(char)
        #                 break
        #             for i in range(times_dublicate):
        #                 file.write(char)
        # else:
        #     file.write(arraySave)
        file.close()

if __name__ == "__main__":
    start_time = time.time()
    img = GrayscaleToAscii(r"C:\Users\Lenovo\PycharmProjects\ConvertImageToASCII\venv\images\aqua_(konosuba).jpg")

    img.convert()
    img.save("ascii/aqua_(ascii).txt")
    print("--- %s seconds ---" % (time.time() - start_time))
