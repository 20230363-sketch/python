def tao_file_demo(file_path):
    content = "Thực hành\n với \n file\n I/O\n"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def in_mot_dong(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
        print("In 1 dòng:")
        print(data.replace("\n", " "))

def in_tung_dong(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        print("In từng dòng:")
        for line in f:
            print(line.strip())

# Chạy thử
file_path = "demo_file1.txt"

tao_file_demo(file_path)
in_mot_dong(file_path)
in_tung_dong(file_path)