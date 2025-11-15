# Thứ tự ưu tiên
a=36+36+36*3**6 # a=36+36+(36*(3**6))=36+36+(36*729)=36+36+26244=26316
print(a) 
b=(3+6)*36+36*(3+6)+3**6 # b=(9*36)+(36*9)+729=324+324+729=1377
print(b)

# Số học với số
c=36+3.6 # 39.6

# Chuỗi với chuỗi
d="Mr"+" "+"Gold" # Mr Gold

# Số với boolean (True = 1, false = 0)
e=35+True # 35+1=36
f=False*36 # 0*36=0

# Ép kiểu rõ ràng
g= 3.6 + float(36) # 3.6 + 36.0 = 39.6
h= "Bộ luật hình sự"+" "+ str(2015) # "Bộ luật hình sự 2015

print(c,"\n",d,"\n",e,"\n",f,"\n",g,"\n",h)