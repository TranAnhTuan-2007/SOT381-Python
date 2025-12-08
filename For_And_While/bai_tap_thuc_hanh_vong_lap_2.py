#Bài 2: Tính tổng dãy số – Tính tổng các số từ 1 đến n (n nhập từ bàn phím)
n=int(input("Nhập n: "))
tong=0
for i in range (1,n+1):
    tong += i
print(f"tổng dãy số bằng {tong}")
      