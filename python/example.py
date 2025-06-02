import numpy as np
from f_theta import f_theta # Assumes f_theta.py is in the same directory

# --- Test Cases ---

# Basic matrix
X_matrix1_py = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [1, 1, 1],
                         [-1, -1, -1],
                         [1, 0, 0],
                         [0, 0, 0],
                         [3, 4, 0]], dtype=float) # Vector with norm 5
print("--- Python: Test Case 1 (Basic Matrix) ---")
print(X_matrix1_py)
thetas_py1 = f_theta(X_matrix1_py)
print("Thetas (radians):")
print(thetas_py1)
print("Thetas (degrees):")
print(thetas_py1 * 180 / np.pi)
print("\n")

# Test with a list of lists (f_theta should convert it)
X_list = [[1., 1., 1.], [1., 0., 0.]]
print("--- Python: Test Case 2 (List of Lists Input) ---")
print(X_list)
thetas_py_list = f_theta(X_list)
print("Thetas (radians):")
print(thetas_py_list)
print("\n")

# Test with a single row matrix
X_single_row_py = np.array([[5., 12., 0.]]) # Norm 13
print("--- Python: Test Case 3 (Single Row Matrix) ---")
print(X_single_row_py)
thetas_py_single = f_theta(X_single_row_py)
print("Thetas (radians):")
print(thetas_py_single)
print("\n")
