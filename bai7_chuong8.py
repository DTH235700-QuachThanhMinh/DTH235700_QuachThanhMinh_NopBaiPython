from tkinter import *

root = Tk()
root.title("Chuyển năm Dương lịch sang Âm lịch")
root.geometry("350x180")
root.configure(bg="yellow")

# ====== DANH SÁCH CAN & CHI ======
can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

def chuyen():
    try:
        nam = int(txtNam.get())
        namAm = can[nam % 10] + " " + chi[nam % 12]
        lblKQ.config(text=namAm)
    except:
        lblKQ.config(text="Nhập sai!")

# ====== GIAO DIỆN ======
Label(root, text="Nhập năm dương:", bg="yellow").place(x=30, y=30)
txtNam = Entry(root, width=10)
txtNam.place(x=150, y=30)
btnChuyen = Button(root, text="Chuyển", command=chuyen)
btnChuyen.place(x=240, y=27)

Label(root, text="Năm âm:", bg="yellow").place(x=30, y=80)
lblKQ = Label(root, text="...", bg="yellow", fg="blue")
lblKQ.place(x=150, y=80)

root.mainloop()
