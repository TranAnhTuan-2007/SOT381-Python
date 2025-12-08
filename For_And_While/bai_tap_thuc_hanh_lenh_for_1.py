#Bài tập 1: Quản lý kho hàng
so_luong = [15, 8, 22, 5, 12, 3]
ten_san_pham = ["Áo", "Quần", "Giày", "Túi", "Mũ", "Ví"]

for i in range(6):
    ten =so_luong[i]
    hang_ton = ten_san_pham[i]
    if ten < 10:
        print(f"{hang_ton}({ten}) cần nhập thêm số lượng ")