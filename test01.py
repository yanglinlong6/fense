from PIL import Image


def start():
    pass


def get_pixel():
    img = Image.open('2023-11-03 21.49.43.jpg')
    # 将图像转换为RGB模式，确保它有三个通道
    img = img.convert('RGB')
    # 显示原始图像
    print("Original Image:")
    img.show()

    # 分离通道
    r, g, b = img.split()

    # 显示红色通道
    print("Red Channel:")
    r.show()

    # 显示绿色通道
    print("Green Channel:")
    g.show()

    # 显示蓝色通道
    print("Blue Channel:")
    b.show()

    start()
    end()  # noqa: F821

def end():
    """
    Purpose:
    """

# end def


if __name__ == '__main__':
    get_pixel()
    print("nihao")
