class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = []
        self.top = -1  # Đỉnh ngăn xếp ban đầu là -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def push(self, item):
        if not self.is_full():
            self.items.append(item)
            self.top += 1
        else:
            print("Ngăn xếp đã đầy, không thể thêm phần tử.")

    def pop(self):
        if not self.is_empty():
            popped_item = self.items.pop()
            self.top -= 1
            return popped_item
        else:
            print("Ngăn xếp đã trống, không thể lấy phần tử.")
            return None

    def count(self):
        return self.top + 1

    def print_stack(self):
        if not self.is_empty():
            print("Nội dung của ngăn xếp:")
            for item in self.items:
                print(item)
        else:
            print("Ngăn xếp đang trống.")

# Tạo một đối tượng ngăn xếp với kích thước tối đa
max_size = 5
stack = Stack(max_size)

# Thêm các phần tử vào ngăn xếp
for i in range(1, max_size + 1):
    stack.push(float(i))

# In ngăn xếp và số phần tử trên ngăn xếp
stack.print_stack()
print(f"Số phần tử trên ngăn xếp: {stack.count()}")

# Lấy các phần tử ra khỏi ngăn xếp
while not stack.is_empty():
    popped_item = stack.pop()
    print(f"Lấy phần tử {popped_item} ra khỏi ngăn xếp.")

# Kiểm tra ngăn xếp sau khi lấy phần tử và số phần tử trên ngăn xếp
stack.print_stack()
print(f"Số phần tử trên ngăn xếp: {stack.count()}")
