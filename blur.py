# 本示例用于实验图像的平滑处理
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lenaNoise.png')
# 均值滤波
r = cv2.blur(img, (3, 3))
# 盒式滤波-越界后取余
boxt = cv2.boxFilter(img, -1, (3, 3), normalize=True)
# 盒式滤波-越界后维持255，容易形成白色图
boxf = cv2.boxFilter(img, -1, (3, 3), normalize=False)
# 高斯滤波
g = cv2.GaussianBlur(img, (3, 3), 1)
# 中值滤波
m = cv2.medianBlur(img, 3)

reault = np.hstack((r, g, m))
cv2.imshow('result', reault)
cv2.waitKey()
cv2.destroyAllWindows()

# plt.subplot(321), plt.imshow(img, 'gray'), plt.title('org')
# plt.subplot(322), plt.imshow(r, 'gray'), plt.title('r')
# plt.subplot(323), plt.imshow(boxt, 'gray'), plt.title('boxt')
# plt.subplot(324), plt.imshow(boxf, 'gray'), plt.title('boxf')
# plt.subplot(325), plt.imshow(g, 'gray'), plt.title('g')
# plt.subplot(326), plt.imshow(m, 'gray'), plt.title('m')
#
# plt.show()
