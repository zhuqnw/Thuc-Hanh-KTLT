
print("Sinh Vien : Pham Phuc Hung")
print("MSSV : 23575201610057")
# Nhập một chuỗi từ bàn phím
input_string = input("Nhập chuỗi: ")

# Loại bỏ tất cả các chữ số khỏi chuỗi
new_string = ''.join([ch for ch in input_string if not ch.isdigit()])

# In lại nội dung chuỗi mới
print("Chuỗi sau khi loại bỏ các chữ số:", new_string)
