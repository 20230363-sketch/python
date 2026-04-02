def ghi_va_doc_file(file_path):
    print("Nhập nội dung (kết thúc bằng dòng trống):")
    
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    # Ghi file
    with open(file_path, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + "\n")

    # Đọc lại
    print("\nNội dung file:")
    with open(file_path, 'r', encoding='utf-8') as f:
        print(f.read())

# Chạy thử
file_path = input("Nhập tên file: ")
ghi_va_doc_file(file_path)