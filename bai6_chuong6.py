import random

N = int(input("Nhập số lượng phần tử N: "))
lst = random.sample(range(1, 100), N)  # tạo N số ngẫu nhiên không trùng nhau từ 1..100
print("List ngẫu nhiên:", lst)
