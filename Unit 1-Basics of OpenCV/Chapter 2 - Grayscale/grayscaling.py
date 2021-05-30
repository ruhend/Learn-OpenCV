# 30 May 2021 10:33:00
import cv2
# import numpy as np
from matplotlib import pyplot as plt

debugFlag = 1


def __dout(status, output):
    if debugFlag:
        print(' ' + status + ' ' + output.title())
    else:
        pass


__dout('+', 'packages imported successfully')

inputImage = cv2.imread('../../samples/input.jpg')
__dout('+', 'image imported successfully')

__dout('>', 'using cvtColor to convert it to grayscale')
grayImage = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)
__dout('>', 'converted and stored in \'grayImage\'')

row, col = 2, 1
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()

axs[0].imshow(cv2.cvtColor(inputImage, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original')
__dout('+', 'prints out the original image')
axs[1].imshow(cv2.cvtColor(grayImage, cv2.COLOR_BGR2RGB))
axs[1].set_title('Grayscale')
__dout('+', 'prints out the grayscaled version')
plt.show()

cv2.imwrite('grayscaling.png', grayImage)
cv2.imwrite('grayscaling.jpg', grayImage)
__dout('+', 'saved the files with png and jpg extensions')

__dout('\nxoxo END oxox', '')
