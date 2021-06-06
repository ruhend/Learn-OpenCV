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

__dout('+', 'packages imported successfully')

inputImage = cv2.imread('../../samples/input.jpg')
__dout('+', 'image imported successfully')

__dout('>', 'using cvtColor to convert it to greyscale')
greyImage = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)
__dout('>', 'converted and stored in \'greyImage\'')

row, col = 2, 1
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()

axs[0].imshow(cv2.cvtColor(inputImage, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original')
__dout('+', 'prints out the original image')
axs[1].imshow(cv2.cvtColor(greyImage, cv2.COLOR_BGR2RGB))
axs[1].set_title('greyscale')
__dout('+', 'prints out the greyscaled version')
plt.show()

cv2.imwrite('greyscaling.png', greyImage)
cv2.imwrite('greyscaling.jpg', greyImage)
__dout('+', 'saved the files with png and jpg extensions')

### End Code ###
__dout('\nxoxo END oxox', '')
