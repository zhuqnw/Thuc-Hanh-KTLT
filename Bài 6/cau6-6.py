print("Sinh Viên: Phạm Phúc Hưng")
print("MSSV: 235752021610057")

class IOString:
    def __init__(self):
        self.s = ""

    def get_String(self):
        self.s = input("Nhập một chuỗi: ")

    def print_String(self):
        print(self.s.upper())

# Tạo đối tượng của lớp IOString
str1 = IOString()
str1.get_String()
str1.print_String()
