print("Sinh Vien : Pham Phuc Hung")
print("MSSV:235752021610057")
def square(n): 
    return n * n 

def cube(n): 
    return n * n * n 

def average(values): 
    nvals = len(values) 
    sum = 0.0 
    for v in values: 
        sum += v  
    return float(sum) / nvals

number = 5
values = [1, 2, 3, 4, 5]

print(f"Square of {number}: {square(number)}")
print(f"Cube of {number}: {cube(number)}")
print(f"Average of {values}: {average(values)}")
