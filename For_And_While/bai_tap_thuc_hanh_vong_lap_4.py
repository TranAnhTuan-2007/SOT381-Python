#Bài 4: Kiểm tra số hoàn hảo – Kiểm tra xem một số có phải là số hoàn hảo không
n = int(input("Nhập số cần kiểm tra: "))
tong_uoc = 0
i=1
while i < n:
    if n % i == 0:
        tong_uoc += i
    i += 1
if tong_uoc == n:
    print(f"{n} là số hoàn hảo")
else:
    print(f"{n} không phải số hoàn hảo")