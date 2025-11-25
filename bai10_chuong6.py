def nhap_ma_tran(ten):
    m = int(input(f"Nhập số dòng của ma trận {ten}: "))
    n = int(input(f"Nhập số cột của ma trận {ten}: "))
    print(f"Nhập các phần tử cho ma trận {ten}:")
    mat = []
    for i in range(m):
        hang = list(map(int, input().split()))
        mat.append(hang)
    return mat

def in_ma_tran(mat, ten):
    print(f"Ma trận {ten}:")
    for hang in mat:
        print(*hang)

def cong_ma_tran(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Không thể cộng 2 ma trận khác kích thước.")
        return None
    m, n = len(A), len(A[0])
    C = [[A[i][j] + B[i][j] for j in range(n)] for i in range(m)]
    return C

def hoan_vi(mat):
    m, n = len(mat), len(mat[0])
    T = [[mat[j][i] for j in range(m)] for i in range(n)]
    return T


# --- Chạy chương trình ---
A = nhap_ma_tran("A")
B = nhap_ma_tran("B")

in_ma_tran(A, "A")
in_ma_tran(B, "B")

C = cong_ma_tran(A, B)
if C:
    in_ma_tran(C, "A + B")

AT = hoan_vi(A)
BT = hoan_vi(B)

in_ma_tran(AT, "A^T")
in_ma_tran(BT, "B^T")
