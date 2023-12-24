class Employee:
    def __init__(self, name, employeeID):
        self.name = name
        self.employeeID = employeeID
        self.salary = 0

    def calculateSalary(self):
        pass

class Worker(Employee):
    def __init__(self, name, employeeID, hourlyRate, hoursWorked):
        super().__init__(name, employeeID)
        self.hourlyRate = hourlyRate
        self.hoursWorked = hoursWorked

    def calculateSalary(self):
        return self.hourlyRate * self.hoursWorked

class Manager(Employee):
    def __init__(self, name, employeeID, bonus):
        super().__init__(name, employeeID)
        self.bonus = bonus

    def calculateSalary(self):
        return self.salary + self.bonus

def input_employee_count():
    while True:
        try:
            n = int(input("Nhập số lượng nhân viên (n): "))
            if n > 0:
                return n
            else:
                print("Số lượng nhân viên phải lớn hơn 0.")
        except ValueError:
            print("Vui lòng nhập một số nguyên dương.")

def create_employee_list(n):
    employee_list = []
    for i in range(n):
        print(f"Nhập thông tin cho nhân viên {i + 1}:")
        name = input("Tên: ")
        employeeID = input("Mã số nhân viên: ")
        role = input("Chức vụ (Worker/Manager): ")
        
        if role.lower() == "worker":
            hourlyRate = float(input("Tỉ lệ giờ công: "))
            hoursWorked = float(input("Số giờ làm việc: "))
            employee = Worker(name, employeeID, hourlyRate, hoursWorked)
        elif role.lower() == "manager":
            bonus = float(input("Thưởng: "))
            employee = Manager(name, employeeID, bonus)
        else:
            print("Chức vụ không hợp lệ. Vui lòng nhập 'Worker' hoặc 'Manager'.")
            continue

        employee_list.append(employee)
    
    return employee_list

def main():
    n = input_employee_count()
    employee_list = create_employee_list(n)

    print("\nDanh sách nhân viên và lương của họ:")
    for employee in employee_list:
        employee.salary = employee.calculateSalary()
        print(f"{employee.name} (Mã số {employee.employeeID}): Lương = {employee.salary}")

if __name__ == "__main__":
    main()
