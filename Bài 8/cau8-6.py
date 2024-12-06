print("Sinh Viên: Phạm Phúc Hưng")
print("MSSV: 23575022160057")
from tkinter import *

# Định nghĩa các phương thức xử lý sự kiện
def NewFile():
    print("New File!")

def OpenFile():
    print("Open File!")

def Exit():
    root.quit()

def About():
    print("This is a simple example of a menu")

def InsText():
    print("Insert Text")

def InsPic():
    print("Insert Picture")

# Tạo cửa sổ chính
root = Tk()
root.title("Menu Example")
menu = Menu(root)
root.config(menu=menu)

# Tạo menu 'File'
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)

# Tạo menu 'Insert'
insertmenu = Menu(menu)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)

# Tạo menu 'Help'
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

# Hiển thị cửa sổ
mainloop()
