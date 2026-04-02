def nhap_thong_tin():
    info = {}
    info["ten"] = input("Tên: ")
    info["tuoi"] = input("Tuổi: ")
    info["email"] = input("Email: ")
    info["skype"] = input("Skype: ")
    info["dia_chi"] = input("Địa chỉ: ")
    info["noi_lam_viec"] = input("Nơi làm việc: ")
    return info


def luu_file(file_path, info):
    with open(file_path, 'w', encoding='utf-8') as f:
        for key, value in info.items():
            f.write(f"{key}:{value}\n")


def doc_file(file_path):
    info = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                key, value = line.strip().split(":", 1)
                info[key] = value
    except FileNotFoundError:
        print("Không tìm thấy file!")
        return

    print("\n--- Thông tin đã lưu ---")
    for k, v in info.items():
        print(f"{k}: {v}")


# Chạy
file_path = "setInfo.txt"
info = nhap_thong_tin()
luu_file(file_path, info)
doc_file(file_path)