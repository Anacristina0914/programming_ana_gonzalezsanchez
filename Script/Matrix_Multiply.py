#Write a function that multiplies two N*N matrices, as a test we can use:
#    A = [[2,4],
#         [3,1]]
#    B = [[2,1],
#         [1,3]]


A = [[2,4,3],
    [3,1,1],
    [1,2,4]]
B = [[2,1,1],
    [1,3,5],
    [9,3,1]]
C = [[0,0,0],
    [0,0,0],
    [0,0,0]]

def mat_multiply(A,B,C):
    """This functions performs the multiplication of matrixes taking A = Matrix 1, B = Matrix 2 and 
    C = Resulting Matrix of 0's"""
    if len(A[0]) == len(B):
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    C[i][j] += A[i][k]*B[k][j]
        return(C)
    else:
        return ("The matrixes cannot be multiplied due to a discrepancy in dimensions")

print(mat_multiply(A,B,C))
