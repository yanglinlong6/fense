# MattingAdaptThresh.py
# Copyright 2021 youcans, XUPT
# Crated：2021-12-10

import cv2
from matplotlib import pyplot as plt

# 1. 读取原始图像
imgOri = cv2.imread('2023-11-03 21.49.43.jpg')  # 读取原始图像
height, width, channels = imgOri.shape

# 2. 从原始图像提取绿色通道
imgGray = cv2.cvtColor(imgOri, cv2.COLOR_BGR2GRAY)  # 彩色图像转换为灰度图像
imgGreen = imgOri[:, :, 1]  # imgGreen 为 绿色通道的 色彩强度图 (注意不是原图的灰度转换结果)
print(imgOri.shape, imgGray.shape, imgGreen.shape)

# 3. 绿色通道转换为二值图像，生成遮罩 Mask、逆遮罩 MaskInv
# colorThresh = 245  # 绿屏背景的颜色阈值 (注意研究阈值的影响)
# ret, binary = cv2.threshold(imgGreen, colorThresh, 255, cv2.THRESH_BINARY)  # 转换为二值图像，生成遮罩，抠图区域黑色遮盖

# 自适应阈值化能够根据图像不同区域亮度分布自适应地改变阈值
# cv.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) -> dst
# 参数 adaptiveMethod: ADAPTIVE_THRESH_MEAN_C(均值法), ADAPTIVE_THRESH_GAUSSIAN_C(高斯法)
# 参数 thresholdType: THRESH_BINARY(小于阈值为0), THRESH_BINARY_INV(大于阈值为0)
# 参数 blockSize: 邻域大小，正奇数
# 参数 C: 偏移量，一般取 0
binary = cv2.adaptiveThreshold(imgGreen, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 5, 0)
binaryInv = cv2.bitwise_not(binary)  # 按位非(黑白转置)，生成逆遮罩，抠图区域白色开窗，抠图以外区域黑色

# 4. 用遮罩进行抠图和更换背景
# 生成抠图图像 (前景保留，背景黑色)
imgMatte = cv2.bitwise_and(imgOri, imgOri, mask=binaryInv)  # 生成抠图前景，标准抠图以外的逆遮罩区域输出黑色
# 将背景颜色更换为红色: 修改逆遮罩 (抠图以外区域黑色)
imgReplace = imgOri.copy()
imgReplace[binaryInv == 0] = [0, 0, 255]  # 黑色区域(0/0/0)修改为红色(BGR:0/0/255)

plt.figure(figsize=(12, 8))
plt.subplot(231), plt.imshow(cv2.cvtColor(imgOri, cv2.COLOR_BGR2RGB)), plt.title("Origin image"), plt.axis('off')
plt.subplot(232), plt.imshow(imgGray, cmap='gray'), plt.title("Gray image"), plt.axis('off')
plt.subplot(233), plt.imshow(imgGreen, cmap='gray'), plt.title("Green channel level"), plt.axis('off')
plt.subplot(234), plt.imshow(binary, cmap='gray'), plt.title("binary mask"), plt.axis('off')
plt.subplot(235), plt.imshow(binaryInv, cmap='gray'), plt.title("inv-binary mask"), plt.axis('off')
plt.subplot(236), plt.imshow(cv2.cvtColor(imgReplace, cv2.COLOR_BGR2RGB)), plt.title("BgColor changed"), plt.axis('off')
plt.tight_layout()
