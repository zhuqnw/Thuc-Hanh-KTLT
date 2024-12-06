print("Sinh Viên : Phạm Phúc Hưng")
print("MSSV : 235752021610057")
j = []
for i in range(680, 1500):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(','.join(j))
