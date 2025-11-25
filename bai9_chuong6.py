def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập mảng
M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]

# Số lẻ
odd = [x for x in M if x % 2 == 1]
print("Số lẻ:", odd, "→ Có", len(odd), "số lẻ")

# Số chẵn
even = [x for x in M if x % 2 == 0]
print("Số chẵn:", even, "→ Có", len(even), "số chẵn")

# Số nguyên tố
prime = [x for x in M if is_prime(x)]
print("Nguyên tố:", prime)

# Không phải nguyên tố
not_prime = [x for x in M if not is_prime(x)]
print("Không nguyên tố:", not_prime)
