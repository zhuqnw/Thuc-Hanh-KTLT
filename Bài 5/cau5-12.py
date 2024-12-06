print("Sinh Viên : Pham Phuc Hung")
print("MSSV: 23575021610057")

import numpy as np

# Dữ liệu đầu vào
student_id = [1023, 5202, 6230, 1671, 1682, 5241, 4532]
student_height = [40.0, 42.5, 41.5, 38.0, 40.0, 42.0, 40.0]

# Tạo mảng cấu trúc từ tên sinh viên, chiều cao
data_type = [('id', int), ('height', float)]
students = np.array(list(zip(student_id, student_height)), dtype=data_type)

print("Mảng ban đầu:")
print(students)

# Sắp xếp mảng theo chiều cao tăng dần
sorted_index = np.lexsort((students['height'], ))
sorted_students = students[sorted_index]

print("Mảng sau khi sắp xếp:")
print(sorted_students)
