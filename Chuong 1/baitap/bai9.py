class DaGiac:
    def __init__(self, so_canh):
        self.so_canh = so_canh
        self.canh = [0] * so_canh

    def nhap_canh(self):
        for i in range(self.so_canh):
            self.canh[i] = float(input(f"Nhập độ dài cạnh {i + 1}: "))

    def chu_vi(self):
        return sum(self.canh)

class HinhBinhHanh(DaGiac):
    def __init__(self, canh_a, canh_b, canh_c):
        super().__init__(4)
        self.canh[0] = canh_a
        self.canh[1] = canh_b
        self.canh[2] = canh_c
        self.canh[3] = canh_c

    def dien_tich(self):
        return self.canh[0] * self.canh[1]

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(chieu_dai, chieu_rong, chieu_dai)

    def dien_tich(self):
        return self.canh[0] * self.canh[1]

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)

# Nhập thông tin hình vuông
canh_hinh_vuong = float(input("Nhập độ dài cạnh hình vuông: "))
hinh_vuong = HinhVuong(canh_hinh_vuong)

# Nhập thông tin hình chữ nhật
chieu_dai_chu_nhat = float(input("Nhập chiều dài hình chữ nhật: "))
chieu_rong_chu_nhat = float(input("Nhập chiều rộng hình chữ nhật: "))
hinh_chu_nhat = HinhChuNhat(chieu_dai_chu_nhat, chieu_rong_chu_nhat)

# Nhập thông tin hình bình hành
canh_a_binh_hanh = float(input("Nhập độ dài cạnh a của hình bình hành: "))
canh_b_binh_hanh = float(input("Nhập độ dài cạnh b của hình bình hành: "))
canh_c_binh_hanh = float(input("Nhập độ dài cạnh c của hình bình hành: "))
hinh_binh_hanh = HinhBinhHanh(canh_a_binh_hanh, canh_b_binh_hanh, canh_c_binh_hanh)

# Tính và in chu vi và diện tích của từng hình
print("\nChu vi và diện tích của hình vuông:")
print(f"Chu vi: {hinh_vuong.chu_vi()}")
print(f"Diện tích: {hinh_vuong.dien_tich()}")

print("\nChu vi và diện tích của hình chữ nhật:")
print(f"Chu vi: {hinh_chu_nhat.chu_vi()}")
print(f"Diện tích: {hinh_chu_nhat.dien_tich()}")

print("\nChu vi và diện tích của hình bình hành:")
print(f"Chu vi: {hinh_binh_hanh.chu_vi()}")
print(f"Diện tích: {hinh_binh_hanh.dien_tich()}")
