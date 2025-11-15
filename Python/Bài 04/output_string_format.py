# Định dạng cơ bản với f-string

name = "Tuấn"
age = 25
score = 85.5678
# Định dạng cơ bản
print(f"Tên: {name}, Tuổi: {age}, Điểm: {score}")
# Định dạng số
print(f"Điểm làm tròn: {score:.2f}")      # 85.57
print(f"Điểm phần trăm: {score:.1f}")     # 85.6
# Căn chỉnh
print(f"Tên: {name:<10} | Tuổi: {age:>5}")  # Căn trái, căn phải
print(f"Số nhị phân: {age:08b}")           # 00011001