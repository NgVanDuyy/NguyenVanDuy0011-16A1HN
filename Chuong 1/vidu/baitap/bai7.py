class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"Ngày: {self.day:02d}")
        print(f"Tháng: {self.month:02d}")
        print(f"Năm: {self.year}")

    def is_leap_year(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            return True
        return False

    def next(self):
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.is_leap_year():
            days_in_month[2] = 29

        self.day += 1

        if self.day > days_in_month[self.month]:
            self.day = 1
            self.month += 1

            if self.month > 12:
                self.month = 1
                self.year += 1


# Tạo một đối tượng Date với giá trị mặc định
date = Date()
date.display()

# Tính ngày tiếp theo và in ra màn hình
date.next()
print("Ngày tiếp theo:")
date.display()
