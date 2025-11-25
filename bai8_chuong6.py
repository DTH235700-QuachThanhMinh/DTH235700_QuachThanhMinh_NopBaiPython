n = int(input("Nhập số lượng phần tử: "))
M = []

for i in range(n):
    x = float(input(f"Nhập M[{i}]: "))
    M.append(x)

M.sort(reverse=True)  # sắp xếp giảm dần
print("Dãy sau khi sắp xếp giảm dần:", M)
