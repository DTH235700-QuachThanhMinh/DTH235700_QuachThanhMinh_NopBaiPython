from tkinter import *
from tkinter import messagebox

# Tạo cửa sổ chính
root = Tk()
root.title("Enter New Password")
root.geometry("320x200")
root.resizable(False, False)
root.configure(bg="#d9d9d9")  # nền xám nhẹ giống mẫu

# ====== HÀM XỬ LÝ ======
def doiMatKhau():
    old = txtOld.get()
    new = txtNew.get()
    again = txtAgain.get()
    
    # Giả sử mật khẩu cũ là "123"
    if old != "123":
        messagebox.showerror("Lỗi", "Mật khẩu cũ không đúng!")
    elif new != again:
        messagebox.showwarning("Cảnh báo", "Mật khẩu mới không khớp!")
    elif new == "":
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập mật khẩu mới!")
    else:
        messagebox.showinfo("Thành công", "Đổi mật khẩu thành công!")

def huyBo():
    root.destroy()

# ====== GIAO DIỆN ======
Label(root, text="Old Password:", bg="#d9d9d9").place(x=20, y=30)
Label(root, text="New Password:", bg="#d9d9d9").place(x=20, y=60)
Label(root, text="Enter New Password Again:", bg="#d9d9d9").place(x=20, y=90)

txtOld = Entry(root, show="*")
txtOld.place(x=180, y=30, width=120)

txtNew = Entry(root, show="*")
txtNew.place(x=180, y=60, width=120)

txtAgain = Entry(root, show="*")
txtAgain.place(x=180, y=90, width=120)

btnOK = Button(root, text="OK", width=10, command=doiMatKhau)
btnOK.place(x=80, y=140)

btnCancel = Button(root, text="Cancel", width=10, command=huyBo)
btnCancel.place(x=180, y=140)

# ====== CHẠY ======
root.mainloop()
