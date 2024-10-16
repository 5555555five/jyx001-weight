import os

# 设置文件夹路径
labels_folder = 'path/to/labels'  # 替换为你的labels文件夹路径
old_text = 'xxxx'                  # 要替换的旧文本
new_text = 'xxxxxx'                # 替换成的新文本

# 遍历文件夹中的所有文件
for filename in os.listdir(labels_folder):
    if filename.endswith('.txt'):  # 确保只处理文本文件
        file_path = os.path.join(labels_folder, filename)
        
        # 读取文件内容
        with open(file_path, 'r') as file:
            content = file.read()
        
        # 替换旧文本为新文本
        updated_content = content.replace(old_text, new_text)
        
        # 如果内容有变化，则写入更新后的内容
        if updated_content != content:
            with open(file_path, 'w') as file:
                file.write(updated_content)
            print(f'Updated file: {filename}')

print("替换完成！")
