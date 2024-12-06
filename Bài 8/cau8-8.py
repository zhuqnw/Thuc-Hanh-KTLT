print("Sinh Viên: Phạm Phúc Hưng")
print("MSSV: 23575022160057")
import tkinter as tk

def submit_info():
    name = entry_name.get()
    dob = entry_dob.get()
    mssv = entry_mssv.get()
    major = entry_major.get()
    print(f"Tên: {name}")
    print(f"Ngày sinh: {dob}")
    print(f"MSSV: {mssv}")
    print(f"Ngành học: {major}")

root = tk.Tk()
root.title("Thông tin cá nhân")

label_name = tk.Label(root, text="Họ tên:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_dob = tk.Label(root, text="Ngày tháng năm sinh:")
label_dob.pack()
entry_dob = tk.Entry(root)
entry_dob.pack()

label_mssv = tk.Label(root, text="MSSV:")
label_mssv.pack()
entry_mssv = tk.Entry(root)
entry_mssv.pack()

label_major = tk.Label(root, text="Ngành học:")
label_major.pack()
entry_major = tk.Entry(root)
entry_major.pack()

btn_submit = tk.Button(root, text="Submit", command=submit_info)
btn_submit.pack()

root.mainloop()

