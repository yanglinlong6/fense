import cv2 as cv

# 加载两张图片
img1 = cv.imread('2023-11-03 21.46.26.jpg')
img2 = cv.imread('root.png')

# 我希望把 LOGO 防止到左上角，所以创建了一个区域（roi)
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# 将 LOGO 图转换为灰度图，阈值为 10， 最大值为 255
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

# 现在将 ROI 抠出黑色区域
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)

# 抠出 LOGO 图像
img2_fg = cv.bitwise_and(img2, img2, mask=mask)

# 将抠出的 LOGO 防入 ROI 区域中
dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

# 显示图像
cv.imshow('res', img1)

# 退出，并释放资源
cv.waitKey(0)
cv.destroyAllWindows()
