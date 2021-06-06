# 30 May 2021 10:33:00

### IMPORT HERE ###
import cv2
from matplotlib import pyplot as plt

debugFlag = 1


def __dout(status, output):
    if debugFlag:
        print(' ' + status + ' ' + output)
    else:
        pass


### Enter your code here ###

__dout('+', 'Packages imported successfully')

inputImage = cv2.imread('../../samples/input.jpg')
__dout('>', 'Image read')

plt.imshow(inputImage)
plt.title('Input Image')
plt.show()
__dout('+', 'Image printed')

__dout('>', 'Printing the dimensions of input 2D image.')
print('Shape of the image : ', inputImage.shape)
print('Height of the image : ', inputImage.shape[0])
print('Width of the image : ', inputImage.shape[1])

__dout('>', 'Saving files in $PWD')
cv2.imwrite('saved.jpg', inputImage)
__dout('+', 'Saved with jpg extension')
cv2.imwrite('saved.png', inputImage)
__dout('+', 'Saved with png extension')

### End Code ###
__dout('\nxoxo END oxox', '')
