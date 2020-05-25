# 本实例用于利用canny进行图像的边界检测
import cv2
import numpy as np
import matplotlib.pyplot as plt

i = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
r1 = cv2.Canny(i, 80, 100)
r2 = cv2.Canny(i, 200, 300)
result = np.hstack((i, r1, r2))
cv2.imshow('对比', result)
cv2.waitKey()
cv2.destroyAllWindows()
