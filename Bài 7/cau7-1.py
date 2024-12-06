print("Sinh Viên: Phạm Phúc Hưng")
print("MSSV: 235752021610057")

# Mở file để đọc
input_file = open('D:/a.txt', 'r')

# Đọc từng dòng trong file và đảo ngược từng dòng
for line in input_file:
    l = len(line)
    s = ''
    while l >= 1:
        s += line[l-1]
        l = l - 1
    print(s)

# Đóng file sau khi đọc xong
input_file.close()
