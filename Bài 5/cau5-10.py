print("Sinh Viên: Phạm Phúc Hưng")
print("MSSV: 235752021610057")

def bubbleSort(nlist):
    loop = len(nlist)
    for i in range(loop - 1):
        swapped = False
        for j in range(loop - 1 - i):
            if nlist[j] > nlist[j + 1]:
                # Trao đổi các phần tử cạnh nhau nếu chúng không theo thứ tự
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                swapped = True
        # Nếu không cần trao đổi phần tử nào nữa thì mảng đã được sắp xếp
        if not swapped:
            break
    return nlist

# Hàm nhập danh sách các phần tử từ bàn phím
def nhap_danh_sach():
    nlist = input("Nhập danh sách các phần tử, ngăn cách nhau bởi dấu phẩy: ")
    # Chuyển đổi chuỗi nhập vào thành danh sách các số nguyên
    nlist = [int(item) for item in nlist.split(',')]
    return nlist

# Chương trình chính
if __name__ == "__main__":
    # Nhập danh sách các phần tử
    nlist = nhap_danh_sach()
    # Sắp xếp danh sách bằng thuật toán nổi bọt
    sorted_list = bubbleSort(nlist)
    # In kết quả
    print("Danh sách đã sắp xếp:", sorted_list)
