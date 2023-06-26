import math
import numpy as np

def filter_matrices():
    valid_matrices = []
    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    if (a * a + b * c) % 26 == 1 and \
                       (b * c + d * d) % 26 == 1 and \
                       (a * b + b * d) % 26 == 0 and \
                       (a * c + d * c) % 26 == 0 and \
                       math.gcd((a * d + b * c) % 26, 1) == 1: # condition for invertible matrix
                        matrix = np.array([[a, b], [c, d]])
                        valid_matrices.append(matrix)
    return valid_matrices

valid_matrices = filter_matrices()
print(f"Number of valid matrices: {len(valid_matrices)}")
# print("Valid matrices:")
# for matrix in valid_matrices:
#     print(matrix)



