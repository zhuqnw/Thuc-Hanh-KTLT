print("Sinh Viên: Phạm Phúc Hưng")
print("MSSV: 235752021610057")

k = open('D:/a.txt', 'r')
char, wc, lc = 0, 0, 0

for line in k:
    char += len(line)
    for i in range(0, len(line)):
        if line[i] == ' ':
            wc += 1
        if line[i] == '\n':
            wc += 1
            lc += 1

print("The number of characters is %d\nThe number of words is %d\nThe number of lines is %d" % (char, wc, lc))
k.close()
