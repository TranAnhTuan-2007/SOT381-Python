# Bài tập Thực hành (Bài 03 – Toán Tử Và Biểu Thức Trong Python)

# Bài 1
n = int(input("Nhập một số: "))
rau_ma = n % 2 == 0 and n > 10 and n % 3 == 0
print(rau_ma)

# Bài 2
a = 15 - 3 * 4 + 2 ** 3		# a=15-12+8=11

b = (15 - 3) * (4 + 2) ** 3		# b=12*6**3=12*(6**3)=12*216=2592

c = 10 %  3 + 5 // 2 * 4	# c=1+2*4=1+8=9


# Bài 3
total = 100    
total -= 25    
total *= 2     
total /= 5     
total += 10    
print("Kết quả cuối cùng:", total)
text = input("Nhập chuỗi: ")
pha_duong_tau = "Python" in text and "Programming" in text
print("Chuỗi chứa cả 'Python' và 'Programming':", pha_duong_tau)
