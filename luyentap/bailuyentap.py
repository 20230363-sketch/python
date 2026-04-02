import math

# 1. Tổng 2 số
def tong_2_so(a, b):
    return a + b

# 2. Tổng n số
def tong_n_so(n):
    total = 0
    for i in range(1, n + 1):
        x = int(input(f"Nhập số thứ {i}: "))
        total += x
    return total

# 3. Kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 4. Tìm số nguyên tố trong [a, b]
def tim_so_nguyen_to(a, b):
    print(f"Các số nguyên tố trong [{a}, {b}]:")
    for i in range(a, b + 1):
        if la_so_nguyen_to(i):
            print(i, end=" ")
    print()

# 5. Kiểm tra số hoàn hảo
def la_so_hoan_hao(n):
    if n <= 0:
        return False
    total = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i
    return total == n

# 6. Tìm số hoàn hảo trong [a, b]
def tim_so_hoan_hao(a, b):
    print(f"Các số hoàn hảo trong [{a}, {b}]:")
    for i in range(a, b + 1):
        if la_so_hoan_hao(i):
            print(i, end=" ")
    print()

# 7. Menu
def menu():
    print("\n===== MENU =====")
    print("1. Tổng 2 số")
    print("2. Tổng n số")
    print("3. Kiểm tra số nguyên tố")
    print("4. Tìm số nguyên tố trong [a, b]")
    print("5. Kiểm tra số hoàn hảo")
    print("6. Tìm số hoàn hảo trong [a, b]")
    print("0. Thoát")
    print("================")

# 8. Chương trình chính
def main():
    while True:
        menu()
        choice = int(input("Chọn: "))

        if choice == 1:
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            print("Tổng =", tong_2_so(a, b))

        elif choice == 2:
            n = int(input("Nhập số lượng: "))
            print("Tổng =", tong_n_so(n))

        elif choice == 3:
            n = int(input("Nhập n: "))
            if la_so_nguyen_to(n):
                print(f"{n} là số nguyên tố")
            else:
                print(f"{n} không phải số nguyên tố")

        elif choice == 4:
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            tim_so_nguyen_to(a, b)

        elif choice == 5:
            n = int(input("Nhập n: "))
            if la_so_hoan_hao(n):
                print(f"{n} là số hoàn hảo")
            else:
                print(f"{n} không phải số hoàn hảo")

        elif choice == 6:
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            tim_so_hoan_hao(a, b)

        elif choice == 0:
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()