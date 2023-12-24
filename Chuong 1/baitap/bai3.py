class PhanSo:
    def __init__(self):
        self.tu_so = 0
        self.mau_so = 1

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def nhap_phaso(self):
        while True:
            try:
                self.tu_so = int(input("Nhập tử số: "))
                self.mau_so = int(input("Nhập mẫu số (khác 0): "))
                if self.kiem_tra_hop_le():
                    break
                else:
                    print("Mẫu số phải khác 0. Vui lòng nhập lại.")
            except ValueError:
                print("Vui lòng nhập số nguyên.")

    def in_phaso(self):
        if self.kiem_tra_hop_le():
            print(f"{self.tu_so}/{self.mau_so}")
        else:
            print("Phân số không hợp lệ.")


# Tạo một đối tượng phân số
ps = PhanSo()

# Nhập phân số
print("Nhập phân số:")
ps.nhap_phaso()

# In phân số ra màn hình
print("Phân số vừa nhập:")
ps.in_phaso()
