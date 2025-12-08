#Bài tập 3: Tính lãi suất
von = 100_000_000
lai_suat = 7
nam = int(input("Nhập số năm: "))

for i in range(1, nam + 1):
    von *= (1 + lai_suat/100)
    print(f"Năm {i}: {von:,.0f} VND")