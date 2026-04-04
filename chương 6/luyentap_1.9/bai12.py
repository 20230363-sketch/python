# Nhập n
n = int(input("Nhập n: "))

# List cho trước
lst = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']

# Đếm
count = 0
for s in lst:
    if len(s) >= n and s[0] == s[-1]:
        count += 1

# Kết quả
print("Số chuỗi thỏa mãn:", count)