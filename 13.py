import os

def get_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                total_size += os.path.getsize(fp)
            except (FileNotFoundError, PermissionError):
                pass
    return total_size

def format_size(size):
    if size >= 1024 * 1024:
        return f"{size / (1024 * 1024):.2f} MB"
    elif size >= 1024:
        return f"{size / 1024:.2f} KB"
    else:
        return f"{size} bytes"

def analyze_directory():
    items = os.listdir('.')
    sizes = []
    for item in items:
        item_path = os.path.join('.', item)
        if os.path.isfile(item_path):
            sizes.append((item, os.path.getsize(item_path)))
        elif os.path.isdir(item_path):
            sizes.append((item, get_size(item_path)))
    sizes.sort(key=lambda x: x[1], reverse=True)
    for item, size in sizes:
        print(f"{item}: {format_size(size)}")

analyze_directory()