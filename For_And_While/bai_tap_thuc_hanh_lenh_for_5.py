#Bài toán 5: Tính tổng các số lẻ
n = int(input("nhập n: "))
tong_le = 0
for i in range(1, n + 1, 2):
    tong_le += i
print(f"Tổng số lẻ: {tong_le}")