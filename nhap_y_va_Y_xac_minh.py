while True:
    n=input("nhập chữ y hoặc Y: ")
    if n != "y" and n!="Y":
        print("Nhập lại")
        continue
    if n == 'Y' or n == 'y':
        print("Login success!")
        break