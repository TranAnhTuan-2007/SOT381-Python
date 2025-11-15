# Biểu thức phức tạp
result = 5 + 3 * 2 ** 2 // 4 - 1
# Thực hiện: 2 ** 2 = 4 → 3 * 4 = 12 → 12 // 4 = 3 → 5 + 3 = 8 → 8 - 1 = 7
print("Kết quả:", result)  # 7

# Sử dụng ngoặc đơn để thay đổi thứ tự ưu tiên
result2 = (5 + 3) * (2 ** 2) // (4 - 1)
# Thực hiện: 5+3=8 → 2**2=4 → 4-1=3 → 8*4=32 → 32//3=10
print("Kết quả với ngoặc:", result2)  # 10