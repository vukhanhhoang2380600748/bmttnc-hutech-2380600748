import re

chuoi = input("Nhập vào chuỗi cần tính: ")
cac_so = re.findall(r'-?\d+', chuoi)

tong_duong = 0
tong_am = 0

for s in cac_so:
    so = int(s)
    if so > 0:
        tong_duong += so
    elif so < 0:
        tong_am += so

print(f"Giá trị dương: {tong_duong}. Giá trị âm: {tong_am}.")