n = int(input("nhập n: "))
tong_phan_so = 0
for i in range(1, n + 1):
    gia_tri = 1 / i
    tong_phan_so += gia_tri
print(f"Kết quả cuối cùng: {tong_phan_so:.3f}")