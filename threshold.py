# 本示例用于研究图像的阈值处理
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('car.jpg')

ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, binary_inv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, trunc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, tozero = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, tozero_inv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['org', 'binary', 'binary_inv', 'trunc', 'tozero', 'tozero_inv']
r = [img, binary, binary_inv, trunc, tozero, tozero_inv]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(r[i], 'gray')
    plt.title(titles[i])
plt.show()
# cv2.imshow('binary', binary_inv)
# cv2.waitKey()
# cv2.destroyAllWindows()
