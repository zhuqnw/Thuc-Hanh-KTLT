print("Sinh Viên: Phạm Phúc Hưng")
print("MSSV: 23575022160057")

import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()

# Biến để lưu trữ giá trị lựa chọn
v = tk.IntVar()
v.set(1)  # Giá trị khởi tạo, ví dụ: Python

# Danh sách các ngôn ngữ lập trình
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5),
]

# Hàm hiển thị lựa chọn
def ShowChoice():
    print(v.get())

# Tạo nhãn hướng dẫn
tk.Label(root,
         text="Choose your favourite programming language:",
         justify=tk.LEFT,
         padx=20).pack()

# Tạo các radio button
for language, val in languages:
    tk.Radiobutton(root,
                   text=language,
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

# Bắt đầu vòng lặp sự kiện
root.mainloop()
