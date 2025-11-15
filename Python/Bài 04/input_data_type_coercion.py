# Ép kiểu số nguyên
age = int(input("Nhập tuổi: "))
print(f"Sau 5 năm nữa bạn sẽ {age + 5} tuổi")

# Ép kiểu số thực
height = float(input("Nhập chiều cao (m): "))
print(f"Chiều cao của bạn là {height:.2f} mét")

# Ép kiểu boolean
is_student = bool(int(input("Là sinh viên? (0: Không, 1: Có): ")))
print(f"Là sinh viên: {is_student}")

try:
    number = int(input("Nhập một số nguyên: "))
    print(f"Số bạn nhập: {number}")
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")