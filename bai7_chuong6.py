n = int(input("Nhập số lượng phần tử: "))
lst = []

for i in range(n):
    while True:
        x = int(input(f"Nhập phần tử thứ {i}: "))
        if i == 0 or x > lst[-1]:  # phải lớn hơn phần tử trước
            lst.append(x)
            break
        else:
            print("Sai thứ tự tăng! Nhập lại.")

print("Dãy sau khi nhập xong:", lst)
