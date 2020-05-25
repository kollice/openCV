# 本示例用于进行图像的边界变幻

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('car.jpg')

ts, bs, ls, rs = (50, 50, 50, 50)
replicate = cv2.copyMakeBorder(img, ts, bs, ls, rs, borderType=cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, ts, bs, ls, rs, borderType=cv2.BORDER_REFLECT)
reflect_101 = cv2.copyMakeBorder(img, ts, bs, ls, rs, borderType=cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, ts, bs, ls, rs, borderType=cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, ts, bs, ls, rs, borderType=cv2.BORDER_CONSTANT, value=136)

plt.subplot(231), plt.imshow(img, 'gray'), plt.title('original')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('replicate')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('reflect')
plt.subplot(234), plt.imshow(reflect_101, 'gray'), plt.title('reflect_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('wrap')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('constant')

plt.show()
