print("Sinh Vien : Pham Phuc Hung")
print("MSSV: 23575201610057")

def Sequential_Search(dlist, item):
    for i in range(len(dlist)):
        if dlist[i] == item:
            return (True, i)
    return (False, -1)

def find_max(dlist):
    return max(dlist)

def find_min(dlist):
    return min(dlist)

def sort_list(dlist):
    return sorted(dlist)

# Chương trình nhập dlist n phần tử từ bàn phím và tìm kiếm phần tử item
dlist = list(map(int, input("Nhập các phần tử của danh sách, cách nhau bằng dấu cách: ").split()))
item = int(input("Nhập phần tử cần tìm kiếm: "))

# Sắp xếp danh sách
sorted_list = sort_list(dlist)
print(f"Danh sách sau khi sắp xếp: {sorted_list}")

# Tìm phần tử lớn nhất và nhỏ nhất
max_value = find_max(dlist)
min_value = find_min(dlist)

print(f"Phần tử lớn nhất: {max_value}")
print(f"Phần tử nhỏ nhất: {min_value}")

# Tìm kiếm tuyến tính
result = Sequential_Search(dlist, item)
if result[0]:
    print(f"Phần tử {item} được tìm thấy tại chỉ mục {result[1]}.")
else:
    print(f"Phần tử {item} không được tìm thấy.")
