a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a is b:", a is b)        # False (cùng giá trị nhưng khác đối tượng)
print("a is c:", a is c)        # True (cùng đối tượng)
print("a == b:", a == b)        # True (cùng giá trị)

# Với số nguyên nhỏ (Python sử dụng interning)
x = 256
y = 256
print("x is y:", x is y)        # True (với số từ -5 đến 256)

text = "Hello, Python!"
fruits = ["apple", "banana", "orange"]

# Kiểm tra trong chuỗi
print("'Python' in text:", "Python" in text)          # True
print("'World' not in text:", "World" not in text)    # True

# Kiểm tra trong danh sách
print("'apple' in fruits:", "apple" in fruits)        # True
print("'grape' not in fruits:", "grape" not in fruits) # True