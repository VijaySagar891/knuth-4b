# Uses basic backtrack to solve N-queens problem.
import time


def visit(x):
    for p in x:
        print(p, end='')
    print()


def p(x):
    for i in range(len(x) - 1):
        if x[i] == x[-1]:
            return False
        if abs(x[i] - x[-1]) == abs(len(x) - 1 - i):
            return False
    return True



def solve_n(n):
    result = []
    l = 0
    x = []
    while True:
        if l == -1:
            return result

        if len(x) == n and l == n:
            result.append(x.copy())
            l = l - 1
            continue

        if l > len(x) - 1: # Go down one level
            for i in range(1, n + 1):
                x.append(i)
                if p(x):
                    l = l + 1
                    break
                else:
                    x.pop()
            else:
                l = l - 1
        else:
            for val in range(x[-1] + 1, n + 1):
                x[-1] = val
                if p(x):
                    l = l + 1
                    break
            else:
                x.pop()
                l = l - 1
    return result


for i in range(14):
    print("Solving for queens: ", i)
    start = time.time()
    out = solve_n(i)
    end = time.time()
    print(i, ": ", len(out), " (", end - start, ")")

# Solving for queens:  0
# 0 :  1  ( 2.002716064453125e-05 )
# Solving for queens:  1
# 1 :  1  ( 5.4836273193359375e-06 )
# Solving for queens:  2
# 2 :  0  ( 2.09808349609375e-05 )
# Solving for queens:  3
# 3 :  0  ( 2.765655517578125e-05 )
# Solving for queens:  4
# 4 :  2  ( 8.535385131835938e-05 )
# Solving for queens:  5
# 5 :  10  ( 0.00024628639221191406 )
# Solving for queens:  6
# 6 :  4  ( 0.0007545948028564453 )
# Solving for queens:  7
# 7 :  40  ( 0.002729654312133789 )
# Solving for queens:  8
# 8 :  92  ( 0.013498783111572266 )
# Solving for queens:  9
# 9 :  352  ( 0.06571388244628906 )
# Solving for queens:  10
# 10 :  724  ( 0.34218597412109375 )
# Solving for queens:  11
# 11 :  2680  ( 1.844947099685669 )
# Solving for queens:  12
# 12 :  14200  ( 10.549625158309937 )
# Solving for queens:  13
# 13 :  73712  ( 67.10508251190186 )





