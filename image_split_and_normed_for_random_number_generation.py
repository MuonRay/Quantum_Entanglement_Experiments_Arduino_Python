# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 03:14:40 2021

@author: cosmi
"""

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


#a much simpler and faster way to generate random numbers by quantum fluctuations in 
#the entangled photon pixels is to do this without openCV and any library 
#for computer vision is to norm the picture arrays by

picture1 = cv2.imread('splitimage1.jpg')
picture2 = cv2.imread('splitimage1.jpg')
picture1_norm = picture1 / np.sqrt(np.sum(picture1 ** 2))
picture2_norm = picture2 / np.sqrt(np.sum(picture2 ** 2))


# If you compare similar pictures the sum will return 1, i.e. compare the same pictures,
# i.e. np.sum(picture1_norm ** 2) will always return a 1 (its the same picture!)
# If they aren't similar, you'll get a value between 0 and 1, which should be entirely random beyond even
#the intrinsic noise of the ccd sensor (as entanglement effectively negates shot noise)
# therefore the non-correlations would be completely random, i.e. vacuum randomness.
#this can produce a non-integer value

random_non_int = np.sum(picture2_norm * picture1_norm)

print(100/random_non_int)



