# 本示例用于实验高斯金字塔和拉普拉斯金字塔。这两种金字塔可以用于对图像进行放大和缩小。但是同一幅图进行完放大然后再缩小后会因为填充了0所以细节会有所损失
import cv2
import numpy as np
import matplotlib.pyplot as plt

i = cv2.imread('car.jpg')
u = cv2.pyrUp(i)
d = cv2.pyrDown(i)
n = cv2.pyrDown(u)

plt.subplot(221), plt.imshow(i, 'gray'), plt.title('i')
plt.subplot(222), plt.imshow(u, 'gray'), plt.title('u')
plt.subplot(223), plt.imshow(d, 'gray'), plt.title('d')
plt.subplot(224), plt.imshow(n, 'gray'), plt.title('n')

plt.show()
