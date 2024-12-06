print("Sinh Vien : Pham Phuc Hung")
print("MSSV :235752021610057")
# Nhập danh sách từ người dùng, phân tách bằng dấu cách hoặc tab
ds = input("Nhập danh sách các phần tử: ").split()

# In danh sách hiện tại
print("Danh sách hiện tại:", ds)

# Nhập phần tử muốn bỏ khỏi danh sách
element_to_remove = input("Nhập phần tử muốn bỏ khỏi danh sách: ")

# Bỏ phần tử khỏi danh sách nếu nó tồn tại
if element_to_remove in ds:
    ds.remove(element_to_remove)
    print(f"Phần tử '{element_to_remove}' đã được bỏ khỏi danh sách")
else:
    print(f"Phần tử '{element_to_remove}' không có trong danh sách")

# In danh sách sau khi bỏ phần tử
print("Danh sách sau khi bỏ phần tử:", ds)
