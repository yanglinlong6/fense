from PIL import Image


def split_color(image_path, color, tolerance=30):
    # 读取图片
    img = Image.open(image_path)
    # 将图片转换为RGB模式
    img = img.convert('RGB')
    # 创建遮罩
    mask = Image.new('L', img.size, 0)

    # 定义颜色范围
    lower_bound = tuple((c - t for c, t in zip(color, (tolerance, tolerance, tolerance))))
    upper_bound = tuple((c + t for c, t in zip(color, (tolerance, tolerance, tolerance))))

    # 遍历图片像素
    pixels = img.load()
    mask_pixels = mask.load()
    for i in range(img.width):
        for j in range(img.height):
            if lower_bound[0] <= pixels[i, j][0] <= upper_bound[0] and \
                    lower_bound[1] <= pixels[i, j][1] <= upper_bound[1] and \
                    lower_bound[2] <= pixels[i, j][2] <= upper_bound[2]:
                # 如果像素在颜色范围内，设置遮罩为255
                mask_pixels[i, j] = 255

    # 应用遮罩
    masked_img = Image.eval(img, lambda x: x if mask.load()[x] == 255 else 0)

    # 保存结果
    masked_img.save('split_color_image.png')


# 指定颜色和容差
target_color = (255, 0, 0)  # 例如红色
tolerance = 50  # 容差值，根据颜色的相似度调整

# 调用函数
split_color('2023-11-03 21.49.43.jpg', target_color, tolerance)
