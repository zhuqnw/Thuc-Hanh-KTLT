print("Sinh vien : Pham Phuc Hung")
print("MSSV : 235752021610057")
import cmath

# Nhap cac he so a, b, c:
a = float(input("Nhap he so a: "))
b = float(input("Nhap he so b: "))
c = float(input("Nhap he so c: "))

# Tinh delta
delta = b**2 - 4*a*c

# Tinh nghiem
if delta > 0:
    x1 = (-b + cmath.sqrt(delta)) / (2*a)
    x2 = (-b - cmath.sqrt(delta)) / (2*a)
    print(f"Hai nghiem pb: x1 = {x1} va x2 = {x2}")
elif delta == 0:
    x1 = -b / (2*a)
    print(f"Nghiem kep: x1 = x2 = {x1}")
else:
    print("Vo nghiem")
