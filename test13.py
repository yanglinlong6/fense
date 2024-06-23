import cv2
import numpy as np
from matplotlib import pyplot as plt

# 通过OpenCV读取图片信息
img = cv2.imread("yuantu.png")
# BGR图转为HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 提取hsv中H通道数据
h = hsv[:, :, 0].ravel()
# 直方图显示
plt.hist(h, 180, [0, 180])
plt.show()
