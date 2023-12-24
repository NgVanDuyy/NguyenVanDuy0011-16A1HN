import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Ellipse(Point):
    def __init__(self, center, semi_major_axis, semi_minor_axis):
        super().__init__(center.x, center.y)
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis

    def area(self):
        return math.pi * self.semi_major_axis * self.semi_minor_axis

class Circle(Ellipse):
    def __init__(self, center, radius):
        super().__init__(center, radius, radius)

# Nhập thông tin của Elip
center_x = float(input("Nhập hoành độ của tâm Elip: "))
center_y = float(input("Nhập tung độ của tâm Elip: "))
semi_major_axis = float(input("Nhập bán trục chính của Elip: "))
semi_minor_axis = float(input("Nhập bán trục phụ của Elip: "))

elip_center = Point(center_x, center_y)
elip = Ellipse(elip_center, semi_major_axis, semi_minor_axis)

# Tính và in diện tích của Elip
print("\nDiện tích của Elip:")
print(f"Diện tích: {elip.area()}")

# Nhập thông tin của Circle
center_x = float(input("Nhập hoành độ của tâm Circle: "))
center_y = float(input("Nhập tung độ của tâm Circle: "))
radius = float(input("Nhập bán kính của Circle: "))

circle_center = Point(center_x, center_y)
circle = Circle(circle_center, radius)

# Tính và in diện tích của Circle
print("\nDiện tích của Circle:")
print(f"Diện tích: {circle.area()}")
