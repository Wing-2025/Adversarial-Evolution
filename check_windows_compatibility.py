import os
from pathlib import Path

# 定义Windows非法字符映射表：仅替换非法字符，尽量少修改
ILLEGAL_CHAR_MAP = {
    # Windows严格禁止的字符
    '\\': '_',
    '/': '_',
    ':': ',',  # 冒号替换为-，符合你的需求
    '*': '_',
    '?': '',
    '"': "'",
    '<': '_',
    '>': '_',
    '|': '_',
    # # Git/Windows敏感的全角符号
    # '——': '--',
    # '。': '.',
    # '，': ',',
    # '！': '!',
    # '？': '?'
}

# Windows传统路径长度限制（可根据需求调整为32767，即NTFS长路径上限）
MAX_PATH_LENGTH = 260

def clean_name(raw_name):
    """
    清理名称中的非法字符，返回合法名称
    :param raw_name: 原始文件/文件夹名
    :return: 清理后的合法名称
    """
    clean_name = raw_name
    for illegal_char, replace_char in ILLEGAL_CHAR_MAP.items():
        clean_name = clean_name.replace(illegal_char, replace_char)
    return clean_name

def check_windows_compatibility():
    """
    扫描脚本运行的当前目录，修复非法字符命名，记录超长路径（不修改）
    """
    # 获取当前工作目录（脚本运行的目录）
    root_dir = os.getcwd()
    root_path = Path(root_dir)
    print(f"开始扫描当前目录：{root_dir}\n")

    # 统计信息
    stats = {
        "total_items": 0,
        "renamed_items": 0,
        "long_path_items": 0,
        "skip_items": 0,
        "error_items": 0
    }

    # 深度优先遍历（先处理子项，再处理父项）
    all_items = []
    for parent, dirs, files in os.walk(root_dir, topdown=False):
        for file in files:
            all_items.append((Path(parent), file, 'file'))
        for dir in dirs:
            all_items.append((Path(parent), dir, 'dir'))

    # 遍历处理每个项目
    print("开始检测并处理Windows不兼容问题...\n")
    for parent_path, item_name, item_type in all_items:
        stats["total_items"] += 1
        original_path = parent_path / item_name
        original_path_str = str(original_path)

        # 1. 检测路径长度是否超标
        if len(original_path_str) > MAX_PATH_LENGTH:
            stats["long_path_items"] += 1
            print(f"[超长路径] {item_type}：{original_path_str}")
            print(f"          长度：{len(original_path_str)}（超过{MAX_PATH_LENGTH}字符）\n")

        # 2. 清理非法字符
        new_name = clean_name(item_name)
        new_path = parent_path / new_name

        # 3. 执行重命名（仅当名称需要修改且无重名时）
        if original_path != new_path:
            if not new_path.exists():
                try:
                    original_path.rename(new_path)
                    stats["renamed_items"] += 1
                    print(f"[修复成功] {item_type}：{original_path} -> {new_path}\n")
                except Exception as e:
                    stats["error_items"] += 1
                    print(f"[修复失败] {item_type}：{original_path}，原因：{str(e)}\n")
            else:
                stats["skip_items"] += 1
                print(f"[跳过] {item_type}：{original_path}，新名称{new_name}已存在\n")

    # 输出统计报告
    print("="*50)
    print("扫描处理完成！统计报告：")
    print(f"总扫描项目数：{stats['total_items']}")
    print(f"非法字符修复数：{stats['renamed_items']}")
    print(f"超长路径提醒数：{stats['long_path_items']}")
    print(f"重名跳过数：{stats['skip_items']}")
    print(f"修复失败数：{stats['error_items']}")
    print("="*50)

if __name__ == "__main__":
    # 直接执行当前目录的扫描处理
    check_windows_compatibility()