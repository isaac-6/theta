## theta: Calculate the theta angle between a reference direction and vectorised datapoints

This repository provides implementations of a function, `f_theta`, that calculates the angle (theta) between each row vector of an input matrix `X` and a vector of all ones of the same dimension. The angle is returned in radians.

This can be appropriate as a normative model, to detect feature deviations across any dimensions.

## Formula

For each row vector `x` in the input matrix `X`, and a normalized all-ones vector `v1` (where `v1 = [1, 1, ..., 1] / ||[1, 1, ..., 1]||`), the angle theta is calculated as:

`theta = arccos( (x ⋅ v1) / (||x|| ⋅ ||v1||) )`

Since `||v1|| = 1`, this simplifies to:

`theta = arccos( (x ⋅ v1) / ||x|| )`

## Implementations

This repository provides implementations in:

*   **R:** [`R/f_theta.R`](R/f_theta.R)
*   **Python (NumPy):** [`python/f_theta.py`](python/f_theta.py)

## Usage

Please see the example scripts in the `examples/` directory for each language.

### R Example
See R/f_theta.R and R/example.R

```R
# Source the function
source("R/f_theta.R")

# Create a sample matrix
X_matrix <- matrix(c(1, 2, 3,
                     4, 5, 6,
                     1, 1, 1,
                     -1, -1, -1,
                     1, 0, 0), ncol = 3, byrow = TRUE)

# Calculate theta
thetas_r <- f_theta(X_matrix)
print(thetas_r)
# Expected output for [1,1,1] is approx 0 radians
# Expected output for [-1,-1,-1] is approx pi radians
```

### Python Example
See python/f_theta.py and python/example.py
```
import numpy as np
from f_theta import f_theta # Assuming f_theta.py is in the same directory or PYTHONPATH

X_matrix_py = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [1, 1, 1],
                        [-1, -1, -1],
                        [1, 0, 0]], dtype=float)

thetas_py = f_theta(X_matrix_py)
print(thetas_py)
```
