# Các tham số cơ bản của print()


# In nhiều giá trị với separator mặc định (khoảng trắng)
print("Hello", "World", "!")  # Output: Hello World !

# Thay đổi separator
print("Hello", "World", "!", sep=".")  # Output: Hello-World-!

# Thay đổi ký tự kết thúc (mặc định là \n - xuống dòng)
print("Hello", end=" ")
print("World")  # Output: Hello World

# Kết hợp nhiều tùy chọn
print("Python", "Programming", sep="*", end="!\n")  # Output: Python*Programming!