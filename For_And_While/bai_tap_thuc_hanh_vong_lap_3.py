#Tìm ước số chung lớn nhất – Tìm ƯCLN của hai số a và b
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
while b != 0:
    a, b = b, a%b
print(f"Ước chung lớn nhất là: {a}")