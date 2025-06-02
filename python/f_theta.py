import numpy as np

def f_theta(X):
    """
    Calculates the angle (theta) in radians between each row vector of an input
    matrix X and a normalized vector of all ones of the same dimension.

    Args:
        X (numpy.ndarray): A 2D numeric NumPy array. Each row is treated as a vector.

    Returns:
        numpy.ndarray: A 1D array containing the angles (theta) in radians
                       for each row of X. Returns an empty array if X is empty.
                       Returns NaN for rows with zero norm.
    """
    if not isinstance(X, np.ndarray):
        X = np.array(X, dtype=float)
    elif X.dtype != float and X.dtype != int : # ensure numeric
        X = X.astype(float)


    if X.ndim != 2:
        raise ValueError("Input X must be a 2D array (matrix).")
    if X.shape[1] == 0:
        raise ValueError("Input X must have at least one column.")
    if X.shape[0] == 0:
        return np.array([]) # Return empty for empty matrix

    n_rows, n_cols = X.shape

    # Define vector1 as a vector of ones
    vector1 = np.ones(n_cols)

    # Compute the dot product of each row in X with vector1
    # X @ vector1 or np.dot(X, vector1)
    dot_prod = X @ vector1

    # Compute the norm of each row of X
    norm_X = np.linalg.norm(X, axis=1)

    # Compute the norm of vector1
    norm_vector1 = np.linalg.norm(vector1) # This is sqrt(n_cols)

    # Compute cosine theta
    # Initialize with NaNs for rows where norm_X is zero
    cos_theta = np.full(n_rows, np.nan)
    
    # Avoid division by zero for rows with zero norm
    # or if norm_vector1 is zero (though it won't be for vector of ones unless n_cols=0, handled above)
    valid_denominator = (norm_X * norm_vector1) > np.finfo(float).eps
    
    cos_theta[valid_denominator] = dot_prod[valid_denominator] / (norm_X[valid_denominator] * norm_vector1)

    # Clip values to [-1, 1] to handle potential floating point inaccuracies
    cos_theta = np.clip(cos_theta, -1.0, 1.0)

    # Calculate theta in radians
    theta = np.arccos(cos_theta)

    return theta

if __name__ == '__main__':
    # Example usage if script is run directly
    X_matrix_py = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [1, 1, 1],
                            [-1, -1, -1],
                            [1, 0, 0],
                            [0, 0, 0]], dtype=float)
    thetas = f_theta(X_matrix_py)
    print("Python Thetas:")
    print(thetas)
    # Expected for [0,0,0] is NaN because norm_X is 0, making angle undefined.
