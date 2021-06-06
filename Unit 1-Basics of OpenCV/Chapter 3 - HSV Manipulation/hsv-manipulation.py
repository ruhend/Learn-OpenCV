# Sun May 30 16:49:39

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
inputImage = cv2.imread('../../samples/input.jpg')
__dout('+', 'image is imported')
hvsVersion = cv2.cvtColor(inputImage, cv2.COLOR_BGR2HSV)
__dout('+', 'converted image into hvs')

rows, cols = 2, 2
fig, axs = plt.subplots(rows, cols, figsize=(15, 10))
fig.tight_layout()
__dout('+', 'created a 2x2 matrix to fit the plots')

__dout('>', 'starting to print plots')
axs[0][0].imshow(cv2.cvtColor(hvsVersion, cv2.COLOR_BGR2RGB))
axs[0][0].set_title('HSV Image')
__dout('+', 'set image 1')
axs[0][1].imshow(cv2.cvtColor(hvsVersion[:, :, 0], cv2.COLOR_BGR2RGB))
axs[0][1].set_title('Hue channel')
__dout('+', 'set image 2')
axs[1][0].imshow(cv2.cvtColor(hvsVersion[:, :, 1], cv2.COLOR_BGR2RGB))
axs[1][0].set_title('Saturation channel')
__dout('+', 'set image 3')
axs[1][1].imshow(cv2.cvtColor(hvsVersion[:, :, 2], cv2.COLOR_BGR2RGB))
axs[1][1].set_title('Value channel')
__dout('+', 'set image 4')

plt.show()
__dout('+', 'showing drawn plot')

__dout('>', 'saving plots')
cv2.imwrite('hvsVersion.jpg', hvsVersion)
cv2.imwrite('hvsVersion.png', hvsVersion)
__dout('+', 'saved main')
cv2.imwrite('hvsVersion_HUE.jpg', hvsVersion[:, :, 0])
cv2.imwrite('hvsVersion_HUE.png', hvsVersion[:, :, 0])
__dout('+', 'saved hue')
cv2.imwrite('hvsVersion_SATURATION.jpg', hvsVersion[:, :, 1])
cv2.imwrite('hvsVersion_SATURATION.png', hvsVersion[:, :, 1])
__dout('+', 'saved saturation')
cv2.imwrite('hvsVersion_VALUE.jpg', hvsVersion[:, :, 2])
cv2.imwrite('hvsVersion_VALUE.png', hvsVersion[:, :, 2])
__dout('+', 'saved value')

### End Code ###
__dout('\nxoxo END oxox', '')
