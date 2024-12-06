print("Sinh Vien : Pham Phuc Hung")
print("MSSV : 235752021610057")

def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    while a < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

n = int(input("Nhập số n: "))
fib_list = fibonacci(n)
print(fib_list)
