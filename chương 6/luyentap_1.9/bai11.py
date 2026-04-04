# Input
n = int(input("Nhập n: "))
lst = ['abc', 'xyz', 'hello', 'python', 'hi']

# Xử lý
result = [word for word in lst if len(word) > n]

# Output
print("Các từ có độ dài > n:", result)