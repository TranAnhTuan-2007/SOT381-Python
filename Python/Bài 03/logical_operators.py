age = 25
has_license = True
is_employed = False

# Điều kiện phức hợp
can_drive = age >= 18 and has_license
print("Có thể lái xe:", can_drive)  # True

can_get_loan = age >= 18 and is_employed
print("Có thể vay vốn:", can_get_loan)  # False

# Sử dụng OR
is_eligible = age >= 65 or is_employed
print("Đủ điều kiện ưu tiên:", is_eligible)  # False

# Sử dụng NOT
is_unemployed = not is_employed
print("Đang thất nghiệp:", is_unemployed)  # True