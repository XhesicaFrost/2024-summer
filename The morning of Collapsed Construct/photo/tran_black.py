from PIL import Image
import os

# 获取当前目录
current_directory = os.getcwd()

# 遍历当前目录下的所有文件
for filename in os.listdir(current_directory):
    if filename.lower().endswith('.png'):
        # 打开 PNG 图片
        img_path = os.path.join(current_directory, filename)
        img = Image.open(img_path)

        # 重新保存 PNG 图片
        img.save(img_path)
        print(f"Saved: {filename}")

print("All PNG images have been processed.")