tien_gui = float(input("Nhập số tiền gửi: "))
lai_suat = float(input("Nhập lãi suất (%/năm): "))
so_thang = int(input("Nhập số tháng gửi: "))

lai = (tien_gui * lai_suat/100 * so_thang) / 12

print("Tiền lãi: ", lai)