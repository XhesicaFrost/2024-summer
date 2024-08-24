from PIL import Image
import numpy as np

# 读取图片
image = Image.open("player_2.png").convert('RGBA')  # 确保图像是RGBA格式
data = np.array(image)

    # 创建掩码：所有非黑色的部分
mask = np.any(data[:, :, :3] != [0, 0, 0], axis=-1)

    # 将有颜色的部分改为黑色
data[mask, :3] = [0, 0, 0]  # 保留透明度

    # 保存为新的PNG图片
new_image = Image.fromarray(data)
new_image.save("player_2_black.png")