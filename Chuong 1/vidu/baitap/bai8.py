class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")

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


class Employee:
    def __init__(self, full_name, birth_date, hire_date):
        self.full_name = full_name
        self.birth_date = birth_date
        self.hire_date = hire_date

    def display_info(self):
        print(f"Họ tên: {self.full_name}")
        print("Ngày sinh:")
        self.birth_date.display()
        print("Ngày vào công ty:")
        self.hire_date.display()


# Tạo một số đối tượng Date
birth_date_1 = Date(11, 2, 2004)
hire_date_1 = Date(2, 10, 2022)

birth_date_2 = Date(10, 10, 2002)
hire_date_2 = Date(2, 10, 2022)

# Tạo một số đối tượng Employee
employee1 = Employee("Nguyễn Văn A", birth_date_1, hire_date_1)
employee2 = Employee("Trần Thị B", birth_date_2, hire_date_2)

# In thông tin của nhân viên
print("Thông tin nhân viên 1:")
employee1.display_info()

print("\nThông tin nhân viên 2:")
employee2.display_info()
