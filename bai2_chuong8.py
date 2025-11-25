from tkinter import *
from math import sqrt

def giaiAction():
    try:
        a = float(stringHSA.get())
        b = float(stringHSB.get())
        c = float(stringHSC.get())

        if a == 0:  # bx + c = 0
            if b == 0 and c == 0:
                stringKQ.set("Vô số nghiệm")
            elif b == 0 and c != 0:
                stringKQ.set("Vô nghiệm")
            else:
                x = -c / b
                stringKQ.set("x = " + str(x))
        else:
            delta = b**2 - 4*a*c
            if delta < 0:
                stringKQ.set("Vô nghiệm")
            elif delta == 0:
                x = -b / (2*a)
                stringKQ.set("Nghiệm kép: x1 = x2 = " + str(x))
            else:
                x1 = (-b - sqrt(delta)) / (2*a)
                x2 = (-b + sqrt(delta)) / (2*a)
                stringKQ.set("x1 = " + str(x1) + " ; x2 = " + str(x2))
    except:
        stringKQ.set("Nhập sai dữ liệu!")

def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringHSC.set("")
    stringKQ.set("")

# ===== CỬA SỔ CHÍNH =====
root = Tk()
root.title("Phương Trình Bậc 2")
root.minsize(height=150, width=280)

# ===== BIẾN LIÊN KẾT =====
stringHSA = StringVar()
stringHSB = StringVar()
stringHSC = StringVar()
stringKQ = StringVar()

# ===== GIAO DIỆN =====
Label(root, text="Phương Trình Bậc 2", fg="red", font=("tahoma", 16)).grid(row=0, column=0, columnspan=2, pady=5)

Label(root, text="Hệ số a:").grid(row=1, column=0, sticky=E)
Entry(root, width=30, textvariable=stringHSA).grid(row=1, column=1)

Label(root, text="Hệ số b:").grid(row=2, column=0, sticky=E)
Entry(root, width=30, textvariable=stringHSB).grid(row=2, column=1)

Label(root, text="Hệ số c:").grid(row=3, column=0, sticky=E)
Entry(root, width=30, textvariable=stringHSC).grid(row=3, column=1)

frameButton = Frame(root)
Button(frameButton, text="Giải", command=giaiAction).pack(side=LEFT, padx=3)
Button(frameButton, text="Tiếp", command=tiepAction).pack(side=LEFT, padx=3)
Button(frameButton, text="Thoát", command=root.quit).pack(side=LEFT, padx=3)
frameButton.grid(row=4, columnspan=2, pady=5)

Label(root, text="Kết quả:").grid(row=5, column=0, sticky=E)
Entry(root, width=30, textvariable=stringKQ).grid(row=5, column=1)

root.mainloop()
