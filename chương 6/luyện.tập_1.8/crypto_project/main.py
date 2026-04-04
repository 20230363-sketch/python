cipher.json

def load_cipher():
    with open("cipher.json", "r", encoding="utf-8") as f:
        return json.load(f)

def encrypt(text, cipher):
    return ''.join(cipher.get(ch, ch) for ch in text)

def decrypt(text, cipher):
    reverse = {v: k for k, v in cipher.items()}
    return ''.join(reverse.get(ch, ch) for ch in text)

cipher = load_cipher()

print("1. Mã hóa")
print("2. Giải mã")
choice = input("Chọn: ")

with open("input.txt", "r", encoding="utf-8") as f:
    data = f.read()

if choice == "1":
    result = encrypt(data, cipher)
    with open("encrypted.txt", "w", encoding="utf-8") as f:
        f.write(result)
    print("Đã mã hóa -> encrypted.txt")

elif choice == "2":
    result = decrypt(data, cipher)
    with open("decrypted.txt", "w", encoding="utf-8") as f:
        f.write(result)
    print("Đã giải mã -> decrypted.txt")

else:
    print("Lựa chọn không hợp lệ!")
