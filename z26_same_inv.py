import math

def inv_matrices_cnt():
    cnt = 0
    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    if (a * a + b * c) % 26 == 1 and \
                       (b * c + d * d) % 26 == 1 and \
                       (a * b + b * d) % 26 == 0 and \
                       (a * c + d * c) % 26 == 0 and \
                       math.gcd((a * d + b * c) % 26, 1) == 1: # condition for invertible matrix
                        cnt += 1
    return cnt

if __name__ == "__main__":
    print(f"Number of valid matrices: {inv_matrices_cnt()}")


