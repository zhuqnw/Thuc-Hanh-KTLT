print("Sinh Viên: Phạm Phúc Hưng")
print("MSSV: 235752021610057")

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def circumference(self):
        return 2 * 3.14 * self.radius

# Tạo một đối tượng Circle với bán kính 5
circle = Circle(5)

print(f"Diện tích của hình tròn là: {circle.area()}")
print(f"Chu vi của hình tròn là: {circle.circumference()}")
