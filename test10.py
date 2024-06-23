import cv2
import numpy as np

import matplotlib.pylab as plt

fig, ax = plt.subplots()


def split_color(img_name, lower_color, upper_color, save_count):
    # 读入图片
    img = cv2.imread(img_name)
    # 获取图片尺寸
    height, width = img.shape[:2]

    # 转换颜色空间
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 根据颜色范围创建掩码
    mask = cv2.inRange(hsv, lower_color, upper_color)
    # 图片去噪 闭运算
    # k = np.ones((5, 5), np.uint8)
    # r = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, k)
    # 定义结构元素
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 35))
    # 图像闭运算
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    # mask[0:height, 0:width] = 255  # 设置左上角100x100像素为白色背景
    # 腐蚀膨胀
    erode = cv2.erode(mask, None, iterations=1)
    mask = cv2.dilate(erode, None, iterations=1)

    # 应用掩码
    result = cv2.bitwise_and(img, img, mask=mask)

    print("将黑色像素替换为白色")
    # 遍历像素，将黑色像素替换为白色
    # for i in range(height):
    #     for j in range(width):
    #         # img[i,j] is the RGB pixel at position (i, j)
    #         # check if it's [0, 0, 0] and replace with [255, 255, 255] if so
    #         if result[i, j].sum() == 0:
    #             print(i, j)
    #             result[i, j] = [255, 255, 255]

    # 转换到HSV颜色空间
    hsv_image = cv2.cvtColor(result, cv2.COLOR_BGR2HSV)

    # 将V通道（亮度）中的最小值替换为最大值，实现背景变白
    hsv_image[..., 2][hsv_image[..., 2] == 0] = 255

    # 转换回BGR颜色空间
    result = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    # 显示结果
    count_ = save_count + 1
    print('count_:', count_)
    cv2.imwrite('mask_{0}.png'.format(str(count_)), result)
    # cv2.imshow('result_{0}'.format(str(count_)), result)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    plt.imshow(result)
    plt.xticks([])  # 去掉x轴
    plt.yticks([])  # 去掉y轴
    plt.axis('off')  # 去掉坐标轴
    plt.savefig(r"mask_{0}矢量.eps".format(str(count_)), format='eps', dpi=600)


if __name__ == '__main__':
    print("start==")
    img_name = "yuantu.png"
    color_list = []
    # 定义蓝色范围
    lower = np.array([100, 70, 50])
    upper = np.array([130, 255, 255])
    color_list.append({"lower": lower, "upper": upper})
    # 定义黄色范围
    lower = np.array([15, 50, 50])
    upper = np.array([40, 255, 255])
    color_list.append({"lower": lower, "upper": upper})
    # 定义青色范围
    lower = np.array([0, 0, 46])
    upper = np.array([180, 43, 220])
    color_list.append({"lower": lower, "upper": upper})
    # 定义青色范围
    lower = np.array([35, 70, 50])
    upper = np.array([70, 255, 255])
    color_list.append({"lower": lower, "upper": upper})
    save_count = 0
    print("color_list:", color_list)
    for color in color_list:
        split_color(img_name, color['lower'], color['upper'], save_count)
        save_count += 1
    print("end==")
