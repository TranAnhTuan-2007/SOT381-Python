# Ứng Dụng Thực Tế 2

# Form nhập thông tin cá nhân, tính chỉ số cơ thể BMI, và xuất

full_name = input("Họ và tên: ")
birth_year = int(input("Năm sinh: "))
height = float(input("Chiều cao (m): "))
weight = float(input("Cân nặng (kg): "))
bmi = weight / (height ** 2)
current_year = 2025
age = current_year - birth_year
print("\n" + "="*40)
print("THÔNG TIN ĐÃ NHẬP:")
print(f"Họ tên: {full_name:>20}")
print(f"Tuổi: {age:>23}")
print(f"Chiều cao: {height:>18.2f} m")
print(f"Cân nặng: {weight:>18.1f} kg")
print(f"Chỉ số BMI: {bmi:>17.2f}")
print("="*40)