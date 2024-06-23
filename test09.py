import cv2
import numpy as np

# 读入图片
# img = cv2.imread("2023-11-03 21.49.43.jpg")
img = cv2.imread("yuantu.png")

# 转换颜色空间
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 定义绿色范围
lower_green = np.array([40, 50, 50])
upper_green = np.array([90, 255, 255])

# 定义黄色范围
lower_yellow = np.array([15, 50, 50])
upper_yellow = np.array([40, 255, 255])

# 根据颜色范围创建掩码
mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

# 合并掩码
mask = cv2.bitwise_or(mask_green, mask_yellow)

# 应用掩码
result = cv2.bitwise_and(img, img, mask=mask)

# 显示结果
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
