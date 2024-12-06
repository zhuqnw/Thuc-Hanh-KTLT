print("Sinh Viên: Phạm Phúc Hưng")
print("MSSV: 235752021610057")

import numpy as np

# Định nghĩa kiểu dữ liệu cho mảng cấu trúc
data_type = [('name', 'S15'), ('class', int), ('height', float)]

# Dữ liệu chi tiết của sinh viên
students_details = [
    ('James', 8, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 6, 42.10),
    ('Pit', 5, 40.11)
]

# Tạo mảng cấu trúc từ dữ liệu
students = np.array(students_details, dtype=data_type)
print("Mảng ban đầu:")
print(students)

# Sắp xếp mảng theo lớp, sau đó theo chiều cao
sorted_students = np.sort(students, order=['class', 'height'])
print("Mảng sau khi sắp xếp theo lớp và chiều cao:")
print(sorted_students)
