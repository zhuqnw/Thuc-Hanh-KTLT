print("Sinh Viên: Phạm Phúc Hưng")
print("MSSV: 235752021610057")

def write_list_to_file(fname, lst):
    with open(fname, 'w', encoding='utf-8') as file:
        for item in lst:
            file.write(f"{item}\n")

filename = 'a.txt'
content_list = ['Python Exercises', 'Java Exercises', 'C++ Exercises']
write_list_to_file(filename, content_list)
print(f"The content has been written to the file {filename}")
