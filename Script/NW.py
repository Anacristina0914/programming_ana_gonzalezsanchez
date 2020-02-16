def read_matrix(matrix_file):
    """This function takes the name, location and extension of a file containing a square substitution matrix
    and returns a dictionary containing the substitution matrix"""
    var1 = open(matrix_file,"r")
    header = var1.readline()
    header = header.rstrip().split()
    dict_name = {}
    for i in var1:
        i = i.rstrip().split()
        for j in range(1,len(i)):
            dict_name[header[j-1]+i[0]] = i[j]
    return(dict_name)
# dict1 = read_matrix("./BLOSUM62_square.txt")

def print_matrix(matrix): 
    """This function takes as an argument a list of lists and prints it in a matrix format"""
    var2 = ""
    for i in matrix:
        for j in i:
            var2 += str(j) + "\t"
        var2 += "\n"
    return(var2)

def nw(seq1,seq2,matrix_file,gap):
    """This function returns a global alignment and score using the dynamic programming algorithm Needleman-Wunsch using a given scoring matrix (Blosum, PAM...)
    seq1 = an aminoacid sequence, seq2 = aminoacid sequence to be aligned against seq1, matrix_file = substitution matrix file name and location: e.g. "./BLOSUM62.txt"
    gap = gap penalty"""
    len1 = len(seq1)+1
    len2 = len(seq1)+1
    dict1 = read_matrix(matrix)
    score = [[0 for i in range(len1)]for j in range(len2)]
    tracing = [[0 for i in range(len1)] for j in range(len2)]

    for i in range(1,len1):
        score[0][i] = d*i
        tracing[0][i] = "l"
    for j in range(1,len1):
        score[j][0] = d*j
        tracing[j][0] = "u"

    for i in range(1,len1):
        for j in range(1,len2):
            score_u = score[i-1][j] + d
            score_l = score[i][j-1] + d
            score_d = score[i-1][j-1] + int(dict1[seq2[i-1]+seq1[j-1]])
            score_max = max(score_u,score_l,score_d)
            score[i][j]= score_max
            if score_max == score_d:
                tracing[i][j] = "d"
            elif score_max == score_u:
                tracing[i][j] = "u"
            else:
                tracing[i][j] = "l"
    # print(print_matrix(score)) #prints the scoring matrix in a matrix form
    # print(print_matrix(tracing)) #prints the tracing matrix in a matrix form

    r = len(tracing) - 1
    c = len(tracing[0]) - 1
    align1 = ""
    align2 = ""
    while r != 0 and c != 0:
        if tracing[r][c] == "d":
            align1 += seq1[r-1]
            align2 += seq2[c-1]
            r -= 1
            c -= 1
        elif tracing[r][c] == "u":
            align1 += seq1[r-1]
            align2 += "-"
            r -= 1
        else:
            align1 += "-"
            align2 += seq2[c-1]
            c -= 1  
    print(align1[::-1])
    print(align2[::-1])
    return("Score:"+ str(score[len(tracing)-1][len(tracing[0])-1]))

seq1 = "GSAQVKGHGKKVADALTNAVAHVTHADAADMPNALSALSDLHAHKL"
seq2 = "NNPELQAHAGKVFKLVYEAAIQLQVTGVVVTDATLKNLGSVHVSKG"
d = -2
matrix = "./BLOSUM62_square.txt"
print(nw(seq1,seq2,matrix,d))