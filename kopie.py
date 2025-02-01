import os
import json

# 指定存放 JSON 文件的文件夹
folder_path = "/path/to/json/folder"  # 替换为你的 JSON 文件夹路径
output_file = os.path.basename(os.path.abspath(folder_path)) + ".json"  # 以文件夹名命名

def merge_json_files(folder_path, output_file):
    merged_data = {"annotations": []}

    # 遍历文件夹中的所有 JSON 文件
    for filename in sorted(os.listdir(folder_path)):  # 按照文件名顺序处理
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    if isinstance(data, dict) and "image_id" in data and "caption" in data:
                        merged_data["annotations"].append(data)  # 添加到 annotations 列表
                    else:
                        print(f"警告：跳过无效 JSON 文件 -> {filename}")
            except json.JSONDecodeError:
                print(f"错误：无法解析 JSON 文件 -> {filename}")

    # 保存合并后的 JSON 文件
    output_path = os.path.join(folder_path, output_file)
    with open(output_path, "w", encoding="utf-8") as outfile:
        json.dump(merged_data, outfile, indent=4, ensure_ascii=False)

    print(f"合并完成！文件已保存至 {output_path}")

# 执行合并函数
merge_json_files(folder_path, output_file)
