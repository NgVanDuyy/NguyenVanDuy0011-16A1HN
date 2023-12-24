class HinhChuNhat:
    def __init__(self):
        self.chieu_dai = 0
        self.chieu_rong = 0

    def nhap_du_lieu(self):
        self.chieu_dai = float(input("Nhập chiều dài: "))
        self.chieu_rong = float(input("Nhập chiều rộng: "))

    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

    def in_thong_tin(self):
        print("Thông tin hình chữ nhật:")
        print(f"Chiều dài: {self.chieu_dai}")
        print(f"Chiều rộng: {self.chieu_rong}")
        print(f"Chu vi: {self.tinh_chu_vi()}")
        print(f"Diện tích: {self.tinh_dien_tich()}")


# Tạo một đối tượng hình chữ nhật
hcn = HinhChuNhat()

# Nhập dữ liệu cho hình chữ nhật
hcn.nhap_du_lieu()

# In thông tin của hình chữ nhật ra màn hình
hcn.in_thong_tin()
