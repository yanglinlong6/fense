from PIL import Image
import matplotlib.pylab as plt

path = r"yuantu.png"
image = Image.open(path).convert("RGB")

plt.imshow(image)
plt.xticks([])  # 去掉x轴
plt.yticks([])  # 去掉y轴
plt.axis('off')  # 去掉坐标轴
plt.savefig(r"a.eps", format='eps', dpi=600)
