col = "ARNDCQEGHILKMFPSTWYV"
row = "ARNDCQEGHILKMFPSTWYV"
file_name = "PAM250.txt"

def read_tmatrix(mat_file, col, row):
    mat_name = {}
    with open(mat_file,"r") as matrix:
        x = 0
        for i in matrix:
            i = i.rstrip().rsplit()
            #print(i)
            for j in range(len(i)):
                #print(x,j)
                mat_name[col[j]+row[x]] = i[j]
            x += 1
        return(mat_name)  
PAM250 = read_tmatrix(file_name,col,row)
