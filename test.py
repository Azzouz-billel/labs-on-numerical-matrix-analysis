import numpy as np
# gauss without pivoting
def gauss_elimination_no_pivot(A, b):
    n = len(b)
    # Forward elimination
    for k in range(n-1):
        for i in range(k+1, n):
            if A[k, k] == 0:
                raise ValueError("Zero pivot encountered.")
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]
    
    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        if A[i, i] == 0:
            raise ValueError("Zero pivot encountered during back substitution.")
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    
    return x
# gauss with partial pivoting
def gauss_elimination_partial_pivot(A, b):
    n = len(b)
    # Forward elimination with partial pivoting
    for k in range(n-1):
        # Find the index of the maximum element in the current column
        max_index = np.argmax(np.abs(A[k:n, k])) + k
        if A[max_index, k] == 0:
            raise ValueError("Zero pivot encountered.")
        # Swap rows if necessary
        if max_index != k:
            A[[k, max_index]] = A[[max_index, k]]
            b[[k, max_index]] = b[[max_index, k]]
        
        for i in range(k+1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]
    
    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        if A[i, i] == 0:
            raise ValueError("Zero pivot encountered during back substitution.")
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    
    return x
# gauss with full pivoting
def gauss_elimination_full_pivot(A, b):
    n = len(b)
    # Forward elimination with full pivoting
    for k in range(n-1):
        # Find the index of the maximum element in the submatrix A[k:n, k:n]
        sub_matrix = A[k:n, k:n]
        max_index = np.unravel_index(np.argmax(np.abs(sub_matrix)), sub_matrix.shape)
        max_row, max_col = max_index[0] + k, max_index[1] + k
        
        if A[max_row, max_col] == 0:
            raise ValueError("Zero pivot encountered.")
        
        # Swap rows and columns if necessary
        if max_row != k:
            A[[k, max_row]] = A[[max_row, k]]
            b[[k, max_row]] = b[[max_row, k]]
        
        if max_col != k:
            A[:, [k, max_col]] = A[:, [max_col, k]]
        
        for i in range(k+1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]
    
    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        if A[i, i] == 0:
            raise ValueError("Zero pivot encountered during back substitution.")
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    
    return x
#defining a function to test the three methods
def test_gauss_methods():
    # Define a test case
    A = np.array([[1e-10, 1, 0],
                  [1, 1E-10, 1],
                  [0, 1, 1e-10]], dtype=float)
    b = np.array([1, 1, 1], dtype=float)

    # Test Gauss elimination without pivoting
    try:
        x_no_pivot = gauss_elimination_no_pivot(A.copy(), b.copy())
        print("Solution without pivoting:", x_no_pivot)
    except ValueError as e:
        print("Error in no pivoting method:", e)

    # Test Gauss elimination with partial pivoting
    try:
        x_partial_pivot = gauss_elimination_partial_pivot(A.copy(), b.copy())
        print("Solution with partial pivoting:", x_partial_pivot)
    except ValueError as e:
        print("Error in partial pivoting method:", e)

    # Test Gauss elimination with full pivoting
    try:
        x_full_pivot = gauss_elimination_full_pivot(A.copy(), b.copy())
        print("Solution with full pivoting:", x_full_pivot)
    except ValueError as e:
        print("Error in full pivoting method:", e)
print("Testing Gauss elimination methods:")
test_gauss_methods()
#-------------------------------------------PART 2------------------------------------------------  
# defining a matrix with i and j
def create_matrix_with_indices(n):
    A = np.zeros((n, n))
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            A[i - 1, j - 1] = 1 / (i + j - 1)
    return A
# calculating the condition number of a matrix+
def condition_number(A):
    return np.linalg.cond(A)
#printing the condition number of the matrix created with indices
n = 5  # size of the matrix
print("the matrix with indices (size 3):", create_matrix_with_indices(n))
print(f"Condition number of the matrix with indices (size {n}):", condition_number(create_matrix_with_indices(n)))