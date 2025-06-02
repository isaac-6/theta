# R/f_theta.R

#' Calculate Angle with the All-Ones Vector
#'
#' Calculates the angle (theta) in radians between each row vector of an input
#' matrix X and a normalized vector of all ones of the same dimension.
#'
#' @param X A numeric matrix or an object coercible to a matrix. Each row is
#'   treated as a vector.
#'
#' @return A numeric vector containing the angles (theta) in radians for each
#'   row of X.
#'
#' @examples
#' X_matrix <- matrix(c(1,2,3, 4,5,6, 1,1,1, -1,-1,-1, 1,0,0), ncol = 3, byrow = TRUE)
#' f_theta(X_matrix)
#'
#' X_df <- data.frame(a=c(1,4,1), b=c(2,5,1), c=c(3,6,1))
#' f_theta(X_df)
#'
f_theta <- function(X) {
  # Ensure X is a matrix. If not, convert it.
  if (!is.matrix(X)) {
    X <- as.matrix(X)
  }
  if (!is.numeric(X)) {
    stop("Input X must be numeric.")
  }
  if (ncol(X) == 0) {
    stop("Input X must have at least one column.")
  }
  if (nrow(X) == 0) {
    return(numeric(0)) # Return empty vector for empty matrix
  }

  # Number of columns (features)
  n_cols <- ncol(X)

  # Define vector1 as a vector of ones with length equal to the number of columns and normalize it.
  vector1 <- rep(1, n_cols)

  # Compute the dot product of each row in X with vector1.
  # X %*% vector1 results in a column vector (matrix with 1 column)
  dot_prod <- as.vector(X %*% vector1)

  # Compute the norm of each row of X
  norm_X <- sqrt(rowSums(X^2))

  # Compute the norm of vector1
  norm_vector1 <- sqrt(sum(vector1^2)) # This is sqrt(n_cols)

  # Compute cosine theta: (x dot vector1) / (||x|| * ||vector1||)
  # Handle rows with zero norm to avoid division by zero (angle is undefined or can be set to pi/2 or 0)
  cos_theta <- numeric(nrow(X))
  valid_rows <- norm_X > .Machine$double.eps # Check for non-zero norm
  
  if (any(valid_rows)) {
      cos_theta[valid_rows] <- dot_prod[valid_rows] / (norm_X[valid_rows] * norm_vector1)
  }
  # If a row is all zeros, its angle with any vector is often considered undefined.
  cos_theta[!valid_rows] <- NA_real_

  # Fix rounding errors: force the computed cosine values to be in the range [-1, 1]
  cos_theta <- pmin(1, pmax(cos_theta, -1))

  # Calculate theta in radians.
  theta <- acos(cos_theta)

  return(theta)
}
