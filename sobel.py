# 本示例利用sobel对图像进行梯度计算从而获得图像的轮廓
import cv2
import numpy as np
import matplotlib.pyplot as plt

# i = cv2.imread('lenaNoise.png', cv2.IMREAD_GRAYSCALE)
# gx = cv2.Sobel(i, cv2.CV_64F, 1, 0, ksize=3)
# gy = cv2.Sobel(i, cv2.CV_64F, 0, 1, ksize=3)
# gx = cv2.convertScaleAbs(gx)
# gy = cv2.convertScaleAbs(gy)
# r = cv2.addWeighted(gx, 0.5, gy, 0.5, 0)
#
# rs = np.hstack((i, r))
# cv2.imshow('rs', rs)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 比较不同算子之间计算梯度结果上的差距
im = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
gxx = cv2.Sobel(im, cv2.CV_64F, 1, 0, ksize=3)
gyy = cv2.Sobel(im, cv2.CV_64F, 0, 1, ksize=3)
gxx = cv2.convertScaleAbs(gxx);
gyy = cv2.convertScaleAbs(gyy);
sobel = cv2.addWeighted(gxx, 0.5, gyy, 0.5, 0)

gxxx = cv2.Scharr(im, cv2.CV_64F, 1, 0)
gyyy = cv2.Scharr(im, cv2.CV_64F, 1, 0)
gxxx = cv2.convertScaleAbs(gxxx)
gyyy = cv2.convertScaleAbs(gyyy)
scharr = cv2.addWeighted(gxxx, 0.5, gyyy, 0.5, 0)

laplacian = cv2.Laplacian(im, cv2.CV_64F, ksize=3)
laplacian = cv2.convertScaleAbs(laplacian)

result = np.hstack((im, sobel, scharr, laplacian))
cv2.imshow('对比', result)
cv2.waitKey()
cv2.destroyAllWindows()
