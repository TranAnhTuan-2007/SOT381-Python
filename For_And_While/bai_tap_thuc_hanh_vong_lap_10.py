#Bài 10: Tìm số Armstrong – Kiểm tra xem một số có phải là số Armstrong không
so = input("Nhập số: ")
n = len(so)
tong = sum(int(chu_so)**n for chu_so in so)

if tong == int(so):
    print(f"{so} là số Armstrong")
else:
    print(f"{so} không phải số Armstrong")