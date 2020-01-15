col = "ARNDCQEGHILKMFPSTWYV"
row = "ARNDCQEGHILKMFPSTWYV"
file_name = "Blosum62.txt"

def read_tmatrix(mat_file, col, row):
    """This function takes a file name in the current directory which contains a triangular matrix, and stores it in a dictionary.
    col = labels of the columns, row = name of rows, mat_file = name of the file where matrix is stored"""
    mat_name = {}
    with open(mat_file,"r") as matrix:
        x = 0
        for i in matrix:    #for each line in the file
            i = i.rstrip().rsplit()
            for j in range(len(i)): #returns an index equal to the length of each row in the file (0,1,2,3...20)
                mat_name[col[j]+row[x]] = i[j]
            x += 1  #for the length of each line in the file, the value increases one to get combinations such as 00,01,11,20,21,22...)
        return(mat_name)  
