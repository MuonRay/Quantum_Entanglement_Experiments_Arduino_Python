# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 02:46:23 2021
Split Image and do Cross-Correlation.
@author: cosmi
"""

from skimage import io, feature
from scipy import ndimage
import numpy as np
import cv2
def correlation_coefficient(patch1, patch2):
    product = np.mean((patch1 - patch1.mean()) * (patch2 - patch2.mean()))
    stds = patch1.std() * patch2.std()
    if stds == 0:
        return 0
    else:
        product /= stds
        return product

# Read the image
img = cv2.imread('leixlip2016test.jpg')
print(img.shape)
height = img.shape[0]
width = img.shape[1]

# Cut the image in half
width_cutoff = width // 2
s1 = img[:, :width_cutoff]
s2 = img[:, width_cutoff:]


cv2.imwrite("splitimage1.jpg", s1)
cv2.imwrite("splitimage2.jpg", s2)




#now read output images in same directory to correlate (note this takes a fairbit of processing)

im1 = cv2.imread('splitimage1.jpg')
im2 = cv2.imread('splitimage1.jpg')


sh_col = im1.shape[1]
sh_row = im1.shape[0]


d = 1

correlation = np.zeros_like(im1)

for i in range(d, sh_row - (d + 1)):
    for j in range(d, sh_col - (d + 1)):
        correlation[i, j] = correlation_coefficient(im1[i - d: i + d + 1,
                                                        j - d: j + d + 1],
                                                    im2[i - d: i + d + 1,
                                                        j - d: j + d + 1])

io.imshow(correlation, cmap='gray')
io.show()
io.imsave("correlated_image", correlation) 
