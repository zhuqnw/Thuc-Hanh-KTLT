print("Sinh Vien : Pham Phuc Hung")
print("MSSV:235752021610057")

def benefit(t, n, k):
    interest_rate = t / 100
    amount = n * (1 + interest_rate) ** k
    
    return amount

t = float(input("Nhập lãi suất tiết kiệm (%/tháng): "))
n = float(input("Nhập số vốn ban đầu: "))
k = int(input("Nhập số tháng gửi: "))

result = benefit(t, n, k)
print(f"Số tiền nhận được sau {k} tháng là: {result}")
