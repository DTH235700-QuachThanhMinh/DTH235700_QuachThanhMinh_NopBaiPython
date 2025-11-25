from tkinter import *

# Hàm xử lý khi nhấn nút
def click_button(value):
    current = str(entry.get())
    entry.delete(0, END)
    entry.insert(0, current + value)

# Hàm tính kết quả
def equal_button():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Hàm xóa toàn bộ
def clear_button():
    entry.delete(0, END)

# Tạo cửa sổ chính
root = Tk()
root.title("Máy tính bỏ túi")
root.geometry("250x350")  # 👈 Tăng chiều cao lên để thấy nút Clr

# Ô hiển thị
entry = Entry(root, width=20, borderwidth=5, font=("Tahoma", 14), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Các nút số và phép toán
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Tạo các nút
for (text, r, c) in buttons:
    if text == "=":
        Button(root, text=text, padx=20, pady=20, command=equal_button).grid(row=r, column=c)
    else:
        Button(root, text=text, padx=20, pady=20, command=lambda val=text: click_button(val)).grid(row=r, column=c)

# Nút xóa Clr (hiện ở dòng cuối)
Button(root, text="Clr", padx=85, pady=20, command=clear_button).grid(row=5, column=0, columnspan=4, pady=5)

root.mainloop()
