# 本实例用于实验图像的腐蚀、膨胀、开运算和闭运算操作

import cv2
import numpy as np
import matplotlib.pyplot as plt

i = cv2.imread('dige.png')

it = 1

kernal = np.ones((3, 3), dtype=np.uint8)
# 用erode对图片进行腐蚀
t = cv2.erode(i, kernal, iterations=it)
# 用dilate对腐蚀后的图片进行膨胀（可抵消腐蚀带来的图片损失），可理解为腐蚀的逆运算
o = cv2.dilate(t, kernal, iterations=it)

result = np.hstack((i, t, o))
cv2.imshow('同一幅图，其腐蚀后和再膨胀的结果对比', result)
cv2.waitKey()
cv2.destroyAllWindows()

# 开闭运算相当于连续执行了腐蚀和膨胀操作。开运算为先腐蚀后膨胀，闭运算为先膨胀后腐蚀
open = cv2.morphologyEx(i, cv2.MORPH_OPEN, kernal, iterations=it)
close = cv2.morphologyEx(i, cv2.NORMAL_CLONE, kernal, iterations=it)
r = np.hstack((i, open, close))
cv2.imshow("同一幅图的开运算和闭运算结果对比", r)
cv2.waitKey()
cv2.destroyAllWindows()

# 梯度运算其实就是通过将同一幅图的开运算和闭运算的结果取其差异化的值，从而获得图像中物品的轮廓
cover = cv2.morphologyEx(i, cv2.MORPH_GRADIENT, kernal, iterations=it)
r2 = np.hstack((i, cover))
cv2.imshow('同一幅图的梯度运算得到的轮廓对比', r2)
cv2.waitKey()
cv2.destroyAllWindows()

# 礼帽和黑帽，礼帽：原始图-开运算（其结果为毛刺） 黑帽：闭运算-原始图（其结果为除了毛刺的图案轮廓）
tophat = cv2.morphologyEx(i, cv2.MORPH_TOPHAT, kernal, iterations=it)
blkhat = cv2.morphologyEx(i, cv2.MORPH_BLACKHAT, kernal, iterations=it)
r3 = np.hstack((i, tophat, blkhat))
cv2.imshow('同一幅图的礼帽和黑帽结果对比', r3)
cv2.waitKey()
cv2.destroyAllWindows()
