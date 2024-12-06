print(" Sinh Vien : Pham Phuc Hung")
print("MSSV :235752021610057")
# Nhập tên người từ bàn phím
full_name = input("Nhập họ và tên: ").strip()

# Tách phần họ và tên riêng
name_parts = full_name.split()
last_name = name_parts[0]
first_name = " ".join(name_parts[1:])

# In ra phần họ và tên riêng
print(f"Họ: {last_name}")
print(f"Tên: {first_name}")
