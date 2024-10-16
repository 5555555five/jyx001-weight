import os

# 设置文件夹路径
images_folder = r'C:\Users\86136\Desktop\1015完不成不睡\DOTA\images\val'  # 替换为你的images文件夹路径
labels_folder = r'C:\Users\86136\Desktop\1015完不成不睡\DOTA\labels\val'    # 替换为你的labels文件夹路径

# 获取文件列表
images = set(os.listdir(images_folder))
labels = set(os.listdir(labels_folder))

# 创建对应的文件名集合（去掉后缀）
image_names = {img.rsplit('.', 1)[0] for img in images}  # 去掉扩展名
label_names = {lbl.rsplit('.', 1)[0] for lbl in labels}  # 去掉扩展名

# 查找不对应的文件
images_without_labels = image_names - label_names
labels_without_images = label_names - image_names

# 打印没有对应的文件
if images_without_labels:
    print("Images without corresponding labels:")
    for img in images_without_labels:
        print(f'{img}.jpg')  # 假设图像文件是.jpg
else:
    print("All images have corresponding labels.")

if labels_without_images:
    print("Labels without corresponding images:")
    for lbl in labels_without_images:
        print(f'{lbl}.txt')  # 假设标签文件是.txt
else:
    print("All labels have corresponding images.")
