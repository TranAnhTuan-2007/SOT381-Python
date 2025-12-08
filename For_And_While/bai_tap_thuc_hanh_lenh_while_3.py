#Bài 3: Menu tương tác
while True:
    print("\n=== MENU ===")
    print("1. Xem chào")
    print("2. Tính bình phương")
    print("0. Thoát")
    
    lựa_chọn = input("Chọn chức năng: ")
    
    if lựa_chọn == "1":
        print("Xin chào Python!")
    elif lựa_chọn == "2":
        x = int(input("Nhập số: "))
        print(f"Bình phương: {x*x}")
    elif lựa_chọn == "0":
        print("Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ!")