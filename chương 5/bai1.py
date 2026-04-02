def doc_n_dong(file_path, n):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i in range(n):
                line = f.readline()
                if not line:
                    break
                print(line.strip())
    except FileNotFoundError:
        print("Không tìm thấy file!")

# Chạy thử
file_path = input("Nhập đường dẫn file: ")
n = int(input("Nhập số dòng cần đọc: "))
doc_n_dong(file_path, n)