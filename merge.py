# 本示例用于进行图像的融合
import cv2
import numpy as np
import matplotlib.pyplot as plt

car = cv2.imread('car.jpg')
cas = cv2.imread('castle.jpg')

car = cv2.resize(car, (500, 500))
cas = cv2.resize(cas, (500, 500))

r = cv2.addWeighted(car, 0.4, cas, 0.6, 0)
cv2.imshow('r', r)
cv2.waitKey()
cv2.destroyAllWindows()
