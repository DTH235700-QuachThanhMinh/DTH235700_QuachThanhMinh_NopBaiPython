from tkinter import *

root = Tk()
root.title("Chuyển độ F sang độ C")
root.geometry("350x180")
root.configure(bg="yellow")

def chuyen():
    try:
        f = float(txtF.get())
        c = (f - 32) * 5 / 9
        lblKQ.config(text=f"{c:.2f} °C")
    except:
        lblKQ.config(text="Lỗi nhập!")

# ====== GIAO DIỆN ======
Label(root, text="Nhập độ F:", bg="yellow").place(x=30, y=30)
txtF = Entry(root, width=10)
txtF.place(x=150, y=30)
btnChuyen = Button(root, text="Chuyển", command=chuyen)
btnChuyen.place(x=240, y=27)

Label(root, text="Độ C:", bg="yellow").place(x=30, y=80)
lblKQ = Label(root, text="Độ C ở đây", bg="yellow", fg="blue")
lblKQ.place(x=150, y=80)

root.mainloop()
