import cv2

# 读取图像
image = cv2.imread('path_to_save_masked_image.jpg')
height, width, channels = image.shape

# 转换到HSV颜色空间
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 将V通道（亮度）中的最小值替换为最大值，实现背景变白
hsv_image[..., 2][hsv_image[..., 2] == 0] = 255

# 转换回BGR颜色空间
white_background_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

# 保存或显示结果
cv2.imwrite('white_background_image.jpg', white_background_image)
cv2.imshow('White Background Image', white_background_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
