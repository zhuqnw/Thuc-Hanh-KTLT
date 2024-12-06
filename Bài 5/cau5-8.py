print("Sinh Vien : Pham Phuc Hung")
print("MSSV: 235752021610057")

def Sequential_Search(dlist, item):
    for i in range(len(dlist)):
        if dlist[i] == item:
            return (True, i)
    return (False, -1)

# Chuong trinh nhap dlist n phan tu tu ban phim va tim kiem phan tu item
dlist = list(map(int, input("Nhap cac phan tu cua danh sach, cach nhau bang dau cach: ").split()))
item = int(input("Nhap phan tu can tim kiem: "))

result = Sequential_Search(dlist, item)
if result[0]:
    print(f"Phan tu {item} duoc tim thay tai chi muc {result[1]}.")
else:
    print(f"Phan tu {item} khong duoc tim thay.")
