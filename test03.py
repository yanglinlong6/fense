import cv2
import numpy as np

# 读取图像
# image = cv2.imread('2023-11-03 21.49.43.jpg')
image = cv2.imread('yuantu.png')

# 转换为HSV颜色空间
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 定义颜色范围
# 例如，提取红色。根据需要调整范围
lower_yellow = np.array([15, 50, 50])
upper_yellow = np.array([40, 255, 255])
mask1 = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

lower_yellow = np.array([15, 50, 50])
upper_yellow = np.array([40, 255, 255])
mask2 = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

# 合并两个掩码
mask = mask1 + mask2

# 使用掩码提取颜色区域
result = cv2.bitwise_and(image, image, mask=mask)

# 显示结果
cv2.imshow('Original Image', image)
cv2.imshow('Mask', mask)
cv2.imshow('Extracted Color', result)

# 等待键盘输入并关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
