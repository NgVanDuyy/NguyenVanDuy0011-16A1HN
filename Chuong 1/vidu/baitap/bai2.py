class ThiSinh:
    def __init__(self):
        self.ho_ten = ""
        self.diem_toan = 0
        self.diem_ly = 0
        self.diem_hoa = 0

    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ tên thí sinh: ")
        self.diem_toan = float(input("Nhập điểm Toán: "))
        self.diem_ly = float(input("Nhập điểm Lý: "))
        self.diem_hoa = float(input("Nhập điểm Hóa: "))

    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Điểm Toán: {self.diem_toan}")
        print(f"Điểm Lý: {self.diem_ly}")
        print(f"Điểm Hóa: {self.diem_hoa}")

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa


# Tạo danh sách thí sinh
danh_sach_thi_sinh = []

# Nhập thông tin thí sinh và thêm vào danh sách
so_thi_sinh = int(input("Nhập số lượng thí sinh: "))
for i in range(so_thi_sinh):
    print(f"Nhập thông tin thí sinh {i + 1}:")
    thi_sinh = ThiSinh()
    thi_sinh.nhap_thong_tin()
    danh_sach_thi_sinh.append(thi_sinh)

# In danh sách thí sinh trúng tuyển
diem_chuan = 20  # Điểm chuẩn
print("Danh sách thí sinh trúng tuyển:")
for thi_sinh in sorted(danh_sach_thi_sinh, key=lambda x: x.tinh_tong_diem(), reverse=True):
    if thi_sinh.tinh_tong_diem() >= diem_chuan:
        thi_sinh.in_thong_tin()
        print(f"Tổng điểm: {thi_sinh.tinh_tong_diem()}")
        print()
