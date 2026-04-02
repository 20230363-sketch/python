import re

def dem_tu(file_path):
    word_count = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

            # Chuẩn hóa: tách từ (bỏ ký tự đặc biệt)
            words = re.findall(r'\b\w+\b', text)

            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

    except FileNotFoundError:
        print("Không tìm thấy file!")
        return

    return word_count


# Chạy
file_path = "demo_file2.txt"
result = dem_tu(file_path)

print("\nKết quả:")
print(result)