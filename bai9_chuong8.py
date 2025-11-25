from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Phần mềm tính BMI")
root.geometry("350x300")
root.configure(bg="yellow")

# ====== HÀM TÍNH BMI ======
def tinhBMI():
    try:
        h = float(txtCao.get())
        w = float(txtNang.get())
        bmi = w / (h * h)
        lblBMI.delete(0, END)
        lblBMI.insert(0, f"{bmi:.2f}")

        # Xác định tình trạng cân nặng
        if bmi < 18.5:
            tinhtrang = "Gầy"
            nguyco = "Thấp"
        elif bmi < 25:
            tinhtrang = "Bình thường"
            nguyco = "Trung bình"
        elif bmi < 30:
            tinhtrang = "Hơi béo"
            nguyco = "Hơi cao"
        else:
            tinhtrang = "Béo phì"
            nguyco = "Rất cao"

        lblTinhTrang.delete(0, END)
        lblTinhTrang.insert(0, tinhtrang)
        lblNguyCo.delete(0, END)
        lblNguyCo.insert(0, nguyco)

    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng số!")

def thoat():
    root.destroy()

# ====== GIAO DIỆN ======
Label(root, text="Nhập chiều cao:", bg="yellow").place(x=30, y=30)
txtCao = Entry(root, width=10)
txtCao.place(x=150, y=30)

Label(root, text="Nhập cân nặng:", bg="yellow").place(x=30, y=60)
txtNang = Entry(root, width=10)
txtNang.place(x=150, y=60)

Button(root, text="Tính BMI", width=10, command=tinhBMI).place(x=130, y=90)

Label(root, text="BMI của bạn:", bg="yellow").place(x=30, y=130)
lblBMI = Entry(root, width=15)
lblBMI.place(x=150, y=130)

Label(root, text="Tình trạng của bạn:", bg="yellow").place(x=30, y=160)
lblTinhTrang = Entry(root, width=15)
lblTinhTrang.place(x=150, y=160)

Label(root, text="Nguy cơ phát triển bệnh:", bg="yellow").place(x=30, y=190)
lblNguyCo = Entry(root, width=15)
lblNguyCo.place(x=150, y=190)

Button(root, text="Thoát", width=10, command=thoat).place(x=130, y=230)

root.mainloop()
