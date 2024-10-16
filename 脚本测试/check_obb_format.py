import os

def check_obb_format(labels_folder):
    # 获取所有的标注文件
    label_files = [f for f in os.listdir(labels_folder) if f.endswith('.txt')]
    
    invalid_files = []

    for label_file in label_files:
        file_path = os.path.join(labels_folder, label_file)
        
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        for line in lines:
            # 分割行内容
            parts = line.strip().split()
            
            # 检查是否有正确的字段数
            if len(parts) != 9:
                invalid_files.append(label_file)
                print(f"Invalid format in {label_file}: expected 9 values, got {len(parts)}")
                break
            
            # 检查类型
            try:
                indx = int(parts[0])  # indx 应为整数
                coordinates = list(map(float, parts[1:]))  # 其余应为浮点数
                if len(coordinates) != 8:
                    raise ValueError("Expected 8 coordinate values")
            except ValueError:
                invalid_files.append(label_file)
                print(f"Invalid numeric values in {label_file}: {line.strip()}")
                break

    if not invalid_files:
        print("All label files are in valid OBB format.")
    else:
        print("Invalid label files:", invalid_files)

# 设置标注文件夹路径
labels_folder = r'C:\Users\86136\Desktop\1015完不成不睡\DOTA\labels\train'  # 替换为你的标签文件夹路径

# 检查标签文件格式
check_obb_format(labels_folder)
