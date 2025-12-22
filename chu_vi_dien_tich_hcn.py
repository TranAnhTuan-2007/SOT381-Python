w=float(input("nhập chiều rộng: "))
h=float(input("nhập chiều cao: "))
if 0 <= h <= 100 and 0 <= w <= 100:
    chu_vi=(w+h)*2
    dien_tich=w*h
    print(f"chu vi hình chữ nhật là {chu_vi:.2f}")
    print(f"diện tích hình chữ nhật là {dien_tich:.2f}")
else:
    print("giá trị không nằm trong khoảng 0 đến 100")