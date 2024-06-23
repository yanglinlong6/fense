# MattingRangeThresh.py
# Copyright 2021 youcans, XUPTy
# Crated：2021-12-10

import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1. 读取原始图像
imgOri = cv2.imread('2023-11-03 21.49.43.jpg')  # 读取原始图像
height, width, channels = imgOri.shape

# 2. 从原始图像提取绿色通道
imgGray = cv2.cvtColor(imgOri, cv2.COLOR_BGR2GRAY)  # 彩色图像转换为灰度图像
imgGreen = imgOri[:, :, 1]
print(imgOri.shape, imgGray.shape, imgGreen.shape)

# 3. 转换到 HSV 空间，对背景颜色范围进行阈值处理，生成遮罩 Mask、逆遮罩 MaskInv
# 使用 cv.nrange 函数在 HSV 空间检查设定的颜色区域范围，转换为二值图像，生成遮罩
# cv.inRange(src, lowerb, upperb[, dst]    ) -> dst
# inRange(frame,Scalar(low_b,low_g,low_r), Scalar(high_b,high_g,high_r))
hsv = cv2.cvtColor(imgOri, cv2.COLOR_BGR2HSV)  # 将图片转换到 HSV 色彩空间
lowerColor = np.array([35, 43, 46])  # (下限: 绿色33/43/46,红色156/43/46,蓝色100/43/46)
upperColor = np.array([77, 255, 255])  # (上限: 绿色77/255/255,红色180/255/255,蓝色124/255/255)
binary = cv2.inRange(hsv, lowerColor, upperColor)
binaryInv = cv2.bitwise_not(binary)

# 4. 用遮罩进行抠图和更换背景
# 生成抠图图像 (前景保留，背景黑色)
imgMatte = cv2.bitwise_and(imgOri, imgOri, mask=binaryInv)  # 生成抠图前景，标准抠图以外的逆遮罩区域输出黑色
imgReplace = imgOri.copy()
imgReplace[binaryInv == 0] = [0, 0, 255]

plt.figure(figsize=(12, 8))
plt.subplot(231), plt.imshow(cv2.cvtColor(imgOri, cv2.COLOR_BGR2RGB)), plt.title("Origin image"), plt.axis('off')
plt.subplot(232), plt.imshow(imgGray, cmap='gray'), plt.title("Gray image"), plt.axis('off')
plt.subplot(233), plt.imshow(imgGreen, cmap='gray'), plt.title("Green channel level"), plt.axis('off')
# plt.subplot(234), plt.imshow(binary, cmap='gray'), plt.title("binary mask"), plt.axis('off')
plt.subplot(234), plt.imshow(binaryInv, cmap='gray'), plt.title("inv-binary mask"), plt.axis('off')
plt.subplot(235), plt.imshow(cv2.cvtColor(imgMatte, cv2.COLOR_BGR2RGB)), plt.title("Matting Image"), plt.axis('off')
plt.subplot(236), plt.imshow(cv2.cvtColor(imgReplace, cv2.COLOR_BGR2RGB)), plt.title("BgColor changed"), plt.axis('off')
plt.tight_layout()
