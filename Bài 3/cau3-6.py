print("Sinh vien : Pham Phuc Hung")
print("MSSV : 235752021610057")

def get_sum(*num):
    tmp = 0
    # Duyệt các tham số
    for i in num:
        tmp += i
    return tmp

result = get_sum(1, 2, 3, 4, 5)
print(result)
