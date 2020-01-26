from PIL import Image
import numpy as np
from .ImageToGrayscale import ImageToGrayscale
import time

class GrayscaleToAscii:
    # chars for replace pixels
    CHARS_CODE = None
    CHARS = ' .+|=*$#%@'
    def __init__(self):
        # in class static method doesnt work
        if self.CHARS_CODE == None:
            chars = "!@#$%*()_-+=\\/ "  # 16
            # ' -=*@#%'
            # ' -~/+=*$#%@'
            self.CHARS_CODE = self.create_chars_code(self.CHARS)
        self.arrayAscii = None

    @staticmethod
    def create_chars_code(chars):
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
        shape[1] += 1
        shape[2] = times_dublicate
        self.arrayAscii = np.chararray(shape)
        shape[1] -= 1

        for row in range(shape[0]):
            for col in range(shape[1]):
                # convert pixel into ascii char and
                for dublicate in range(times_dublicate):
                    self.arrayAscii[row][col][dublicate] = self.CHARS_CODE[arrayImage[row][col][0]]
            # last elem
            self.arrayAscii[row][shape[1]][0] = '\n'
            # fill void in '\n' array
            for dublicate in range(1, times_dublicate):
                self.arrayAscii[row][shape[1]][dublicate] = ' '

    def get_text(self):
        return self.arrayAscii.astype('|S1').tostring().decode('utf-8')
    
    def save(self, Asciipath, times_dublicate = 1):
        file = open(Asciipath, 'w')
        arraySave = self.arrayAscii.astype('|S1').tostring().decode('utf-8')
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
