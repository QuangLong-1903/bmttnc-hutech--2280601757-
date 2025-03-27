gio_lam = float(input("Nhập vào số giờ làm: "))
luong_gio = float(input("Nhập vào tiền lương mỗi giờ làm: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0,gio_lam -gio_tieu_chuan)
luong = gio_tieu_chuan *luong_gio + gio_vuot_chuan * luong_gio *1.5
print(f"số tiền thực được lãnh của nhân viên là: {luong}")