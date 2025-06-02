# Source the function definition from the same directory
# If running this script directly, ensure f_theta.R is in the same folder
# or adjust the path.
source("f_theta.R")

# --- Test Cases ---

# Basic matrix
X_matrix1 <- matrix(c(1, 2, 3,
                      4, 5, 6,
                      1, 1, 1,
                      -1, -1, -1,
                      1, 0, 0,
                      0, 0, 0,
                      3, 4, 0), # Vector with norm 5, angle with (1,1,1)
                     ncol = 3, byrow = TRUE)
cat("--- R: Test Case 1 (Basic Matrix) ---\n")
print(X_matrix1)
thetas_r1 <- f_theta(X_matrix1)
cat("Thetas (radians):\n")
print(thetas_r1)
cat("Thetas (degrees):\n")
print(thetas_r1 * 180 / pi)
cat("\n")

# Test with a data frame
X_df <- data.frame(V1 = c(1, 1, 0), V2 = c(1, 0, 1), V3 = c(1, 0, 0))
cat("--- R: Test Case 2 (Data Frame Input) ---\n")
print(X_df)
thetas_r_df <- f_theta(X_df)
cat("Thetas (radians):\n")
print(thetas_r_df)
cat("\n")
