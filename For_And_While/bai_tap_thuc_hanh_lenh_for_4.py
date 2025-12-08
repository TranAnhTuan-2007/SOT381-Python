#Bài toán 4: Tính tổng từ 1 đến n
n = int(input("Nhập n:"))
tong = 0
for i in range(1, n + 1):
    tong += i
print(f"Kết quả: 1 + 2 + ... + {n} = {tong}")