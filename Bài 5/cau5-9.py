print("Sinh Viên: Phạm Phúc Hưng")
print("MSSV: 32375201610057")

def binary_search(lst, value):
    lower_bound = 0
    upper_bound = len(lst) - 1

    while lower_bound <= upper_bound:
        mid_point = lower_bound + (upper_bound - lower_bound) // 2
        if lst[mid_point] < value:
            lower_bound = mid_point + 1
        elif lst[mid_point] > value:
            upper_bound = mid_point - 1
        else:
            return True
    return False

# Hàm nhập danh sách các phần tử từ bàn phím
def nhap_danh_sach():
    nlist = input("Nhập danh sách các phần tử đã được sắp xếp, ngăn cách nhau bởi dấu phẩy: ")
    # Chuyển đổi chuỗi nhập vào thành danh sách các số nguyên
    nlist = [int(item) for item in nlist.split(',')]
    return nlist

# Chương trình chính
if __name__ == "__main__":
    # Nhập danh sách các phần tử
    nlist = nhap_danh_sach()
    # Nhập giá trị cần tìm kiếm
    value = int(input("Nhập giá trị cần tìm kiếm: "))
    # Tìm kiếm giá trị trong danh sách bằng thuật toán nhị phân
    result = binary_search(nlist, value)
    # Kết quả
    if result:
        print(f"Giá trị {value} có tồn tại trong danh sách.")
    else:
        print(f"Giá trị {value} không tồn tại trong danh sách.")
