# ImageToAscii
fast rendering and converting image to ascii symbols


sorry for missing docs 
now i can only give you example of converting 


```
from ImageToAscii import *
if __name__ == '__main__':
  im = cv2.imread(r'pic\path.png', 0)

  app = ImageToAscii(im)
    
  app.resize_grayscaleArray_scale(0.25)

  app.convert(2, font='consolas')
    
  app.save_asciiImage(r'result/path')
