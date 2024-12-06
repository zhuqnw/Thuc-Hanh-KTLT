print("Sinh Vien : Pham Phuc Hung")
print("MSSV: 23575021610057")

def Sequential_Search(dlist, item):
    for i in range(len(dlist)):
        if dlist[i] == item:
            return (True, i)
    return (False, -1)

def find_max(dlist):
    max_value = dlist[0]
    max_index = 0
    for i in range(1, len(dlist)):
        if dlist[i] > max_value:
            max_value = dlist[i]
            max_index = i
    return max_value, max_index

def find_min(dlist):
    min_value = dlist[0]
    min_index = 0
    for i in range(1, len(dlist)):
        if dlist[i] < min_value:
            min_value = dlist[i]
            min_index = i
    return min_value, min_index

def sort_list(dlist):
    return sorted(dlist)

# Chuong trinh nhap dlist n phan tu tu ban phim va tim kiem phan tu item
dlist = list(map(int, input("Nhap cac phan tu cua danh sach, cach nhau bang dau cach: ").split()))
item = int(input("Nhap phan tu can tim kiem: "))

# Sap xep danh sach
sorted_list = sort_list(dlist)
print(f"Danh sach sau khi sap xep: {sorted_list}")

# Tim phan tu lon nhat va nho nhat cung voi vi tri cua chung
max_value, max_index = find_max(dlist)
min_value, min_index = find_min(dlist)
