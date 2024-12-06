print("Sinh Vien : Pham Phuc Hung")
print("MSSV :235752021610057")

ds = input("Nhập danh sách các phần tử: ").split()
print("Danh sách hiện tại:", ds)


element_to_remove = input("Nhập phần tử muốn bỏ khỏi danh sách: ")


if element_to_remove in ds:
    ds.remove(element_to_remove)
    print(f"Phần tử '{element_to_remove}' đã được bỏ khỏi danh sách")
else:
    print(f"Phần tử '{element_to_remove}' không có trong danh sách")

print("Danh sách sau khi bỏ phần tử:", ds)
