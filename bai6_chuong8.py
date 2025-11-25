from tkinter import *

root = Tk()
root.title("frame 2")

# ======= TẠO KHUNG CHÍNH =======
frame = Frame(root, padx=10, pady=10)
frame.pack()

# ======= DANH SÁCH CÁC KIỂU STYLE =======
styles = ["raised", "sunken", "flat", "ridge", "groove", "solid"]

# ======= TẠO CÁC DÒNG VỚI borderwidth KHÁC NHAU =======
for bw in range(5):  # từ 0 đến 4
    # Nhãn mô tả độ dày viền
    Label(frame, text=f"borderwidth = {bw}", width=15, anchor="w").grid(row=bw, column=0, padx=5, pady=3)
    
    # Các nút với các kiểu relief khác nhau
    for j, style in enumerate(styles):
        btn = Button(frame, text=style, relief=style, borderwidth=bw, width=8)
        btn.grid(row=bw, column=j+1, padx=3, pady=3)

root.mainloop()
