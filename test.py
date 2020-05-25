# 本示例用于读取图片和视频并进行操作后进行展示或另存为

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
car = cv2.imread('car.jpg')
print(car)

# 裁剪图片
# small = car[0:200,0:200]

# 分离颜色通道
# b,g,r = cv2.split(car)
# print(b)
# print(g)
# print(r)

# 将颜色通道组合成图片
# new = cv2.merge((b,g,r))
# print(new)

# 显示图片
# cv2.imshow('car', new)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 保存图片
# cv2.imwrite('car1.jpg', car)


# 读取视频
# v = cv2.VideoCapture('video.mp4')
# print(v)
# if v.isOpened():
#     isOpen, frame = v.read()
# else:
#     isOpen = False
#
# while isOpen:
#     ret ,frame = v.read()
#     if frame is None:
#         break
#     if ret == True:
#         g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         cv2.imshow('grey',g)
#         if cv2.waitKey(10) & 0xFF == 27:
#             break
# v.release()
# cv2.destroyAllWindows()
