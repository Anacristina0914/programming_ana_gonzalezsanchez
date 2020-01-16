import input_data
PAM250 = input_data.PAM250_dict
BLOSUM62 = input_data.BLOSUM62_dict
alignments = input_data.alignments
alignment1_1 = alignments[0][0]
alignment1_2 = alignments[0][1]
alignment2_1 = alignments[1][0]
alignment2_2 = alignments[1][1]
alignment3_1 = alignments[2][0]
alignment3_2 = alignments[2][1]


alignpairs1 = []
for i in range(len(alignment1_1)):
        alignpairs1.append(alignment1_1[i]+alignment1_2[i])
alignpairs2 = []
for x in range(len(alignment2_1)):
        alignpairs2.append(alignment2_1[x]+alignment2_2[x])
alignpairs3 = []
for y in range(len(alignment3_1)):
        alignpairs3.append(alignment3_1[y]+alignment3_2[y])


score1PAM = 0
for i in alignpairs1:
    if "-" not in i:
        score1PAM += PAM250[i]
    else:
        score1PAM -= 2
score1Blosum = 0
for i in alignpairs1:
    if "-" not in i:
        score1Blosum += BLOSUM62[i]
    else:
        score1Blosum -= 2
print("Alignment1:", "PAM Score:",score1PAM, "Blosum Score:", score1Blosum)

score2PAM = 0
for i in alignpairs2:
    if "-" not in i:
        score2PAM += PAM250[i]
    else:
        score2PAM -= 2
score2Blosum = 0
for i in alignpairs2:
    if "-" not in i:
        score2Blosum += BLOSUM62[i]
    else:
        score2Blosum -= 2
print("Alignment2:", "PAM Score:",score2PAM, "Blosum Score:", score2Blosum)
        
score3PAM = 0
for i in alignpairs3:
    if "-" not in i:
        score3PAM += PAM250[i]
    else:
        score3PAM -= 2
score3Blosum = 0
for i in alignpairs3:
    if "-" not in i:
        score3Blosum += BLOSUM62[i]
    else:
        score2Blosum -= 2
print("Alignment3:", "PAM Score:",score3PAM, "Blosum Score:", score3Blosum)  

##Additional code that reads a triangular matrix from a given file and stores is in a dictionary called "name"
def read_tmatrix(file_name,col_name, row_name):
    name = {}
    with open (file_name,"r") as subs_matrix:
        pos = 0
    for i in subs_matrix:
        i = i.rstrip().rsplit()
        for x in range(len(i)):
            name[col_name[x]+row_name[pos]] = i[x]
        x +=1
    return(name)
           
