#Bài 14: Tìm số nguyên tố – Tìm tất cả số nguyên tố trong khoảng từ 1 đến n
so = int(input("Nhập số cần kiểm tra: "))
if so < 2:
    print("Không phải số nguyên tố")
else:
    la_so_nguyen_to = True
    for i in range(2, int(so**0.5) + 1):
        if so %i==0:
            la_so_nguyen_to = False
            break
    print("Là số nguyên tố" if la_so_nguyen_to else "Không phải số nguyên tố")