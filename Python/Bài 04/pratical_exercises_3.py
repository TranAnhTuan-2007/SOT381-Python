# Bài 1
print("Bài 1")
so_dien = int(input("Nhập số kWh điện tiêu thụ: "))
tien = 0
if so_dien <= 50:
    tien = so_dien * 1678
elif so_dien <= 100:
    tien = 50 * 1678 + (so_dien - 50) * 1734
elif so_dien <= 200:
    tien = 50 * 1678 + 50 * 1734 + (so_dien - 100) * 2014
elif so_dien <= 350:
    tien = 50 * 1678 + 50 * 1734 + 100 * 2014 + (so_dien - 200) * 2536
else:
    tien = 50 * 1678 + 50 * 1734 + 100 * 2014 + 150 * 2536 + (so_dien - 350) * 2927
print(f"Tổng tiền điện: {tien:,} VND")

# Bài 2
print("Bài 2")
ten = input("Nhập tên học sinh: ")
diem_toan = float(input("Nhập điểm Toán: "))
diem_ly = float(input("Nhập điểm Lý: "))
diem_hoa = float(input("Nhập điểm Hóa: "))
diem_trung_binh = (diem_toan + diem_ly + diem_hoa) / 3
if diem_trung_binh >= 8:
    xeploai = "Giỏi"
elif diem_trung_binh >= 6.5:
    xeploai = "Khá"
elif diem_trung_binh >= 5:
    xeploai = "Trung bình"
else:
    xeploai = "Yếu"
print("\n--- KẾT QUẢ HỌC SINH ---")
print(f"Tên học sinh: {ten}")
print(f"Điểm Toán: {diem_toan:.2f}")
print(f"Điểm Lý: {diem_ly:.2f}")
print(f"Điểm Hóa: {diem_hoa:.2f}")
print(f"Điểm trung bình: {diem_trung_binh:.2f}")
print(f"Xếp loại: {xeploai}")

# Bài 3
print("bài 3")
nhiet_do = float(input("Nhập nhiệt độ: "))
loai = input("Nhập loại nhiệt độ (C/F/K): ") 
if loai == "C" or loai == "c":
    f = nhiet_do * 9/5 + 32
    k = nhiet_do + 273.15
    print(f"{nhiet_do:.2f}°C = {f:.2f}°F = {k:.2f}K")
elif loai == "F" or loai == "f":
    c = (nhiet_do - 32) * 5/9
    k = c + 273.15
    print(f"{nhiet_do:.2f}°F = {c:.2f}°C = {k:.2f}K")
elif loai == "K" or loai == "k":
    c = nhiet_do - 273.15
    f = c * 9/5 + 32
    print(f"{nhiet_do:.2f}K = {c:.2f}°C = {f:.2f}°F")
else:
    print("Loại nhiệt độ không hợp lệ!")
