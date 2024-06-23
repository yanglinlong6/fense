import cv2
import numpy as np

# 读取目标图像
image = cv2.imread('yuantu.png')

# 确定图像的尺寸
height, width, channels = image.shape

# 创建一个白色背景的遮罩，大小与图像一致
# mask = np.ones((height, width, channels), dtype='uint8') * 255
mask = np.ones((height, width, channels), dtype='uint8') * 0

# 应用遮罩到图像上，这里使用位与操作
# 这将只保留原始图像中非白色（即有实际内容的部分）
masked_image = cv2.bitwise_and(image, mask)
# masked_image = cv2.bitwise_or(image, mask)

# 显示原始图像和遮罩后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Masked Image', masked_image)

# 保存结果
cv2.imwrite('path_to_save_masked_image.jpg', masked_image)

# 等待按键，然后关闭所有窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
