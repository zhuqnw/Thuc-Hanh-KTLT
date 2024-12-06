print("Sinh Vien : Pham Phuc Hung")
print("MSSV : 235752021610057")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

P = tuple(i for i in range(2, 1000000) if is_prime(i))
print(P)
