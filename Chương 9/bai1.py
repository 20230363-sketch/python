class HocVien:
    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop

    def show_info(self):
        print("===== Thông tin học viên =====")
        print("Họ tên:", self.ho_ten)
        print("Ngày sinh:", self.ngay_sinh)
        print("Email:", self.email)
        print("Điện thoại:", self.dien_thoai)
        print("Địa chỉ:", self.dia_chi)
        print("Lớp:", self.lop)
    def change_info(self, dia_chi="Hà Nội", lop="IT12.x"):
        self.dia_chi = dia_chi
        self.lop = lop

if __name__ == "__main__":
    # Tạo đối tượng học viên
    hv1 = HocVien(
        ho_ten="CAO TIEN HIEN",
        ngay_sinh="01/01/2005",
        email="20230363@eaut.edu.vn",
        dien_thoai="0382292632",
        dia_chi="Hai Phong",
        lop="IT12.1"
    )

    hv1.show_info()

    print("\n--- Sau khi cập nhật ---")

    # Gọi hàm change_info (không truyền tham số -> dùng mặc định)
    hv1.change_info()

    # Hiển thị lại
    hv1.show_info()