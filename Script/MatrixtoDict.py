#The goal of the excercise is to read a file containing a given scoring matrix in order to generate a library that contains all of the values for each pair

#Pseudo code for generating and filling the matrix
#We have a file containing the Blosum Matrix.
#We need to read each line of the matrix.
#we can create a header row in order to not have to make a for loop for that.
#Then we do a for loop to get element 0 of header + element 0 of 1st line, e1 of header + e0 of the 2nd line, e2 header + e0 of 3rd line.
#For the value of each key we need to add the intercepting value: for r1,c1 = 1, 2, 3, 4, 5...21


x ="blosum.txt"
y = "Blosum50"
def matrix(file_name,matrix_name):
"""This function uses the name of a file in the current directory and the name of a matrix to create a dictionary containing all
the possible combinations and their given values. This is used to perform alignments based on scoring matrixes such as BLOSUM and PAM"""    
    with open (file_name,"r") as mat: #Opens a file and gives it the name "mat"
        header = mat.readline()  #reads only the first line of the file (header) and assigns it to the variable header.
        header = header.rstrip().split()    #deletes the additional character \n at the end of the line, and splits into a list.
        matrix_name = {}   #creates an empty dictionary
        for i in mat:    #For each line in the file starting from the second once(i.e. the for loop will be run 20 times for Blosum50 matrix)
            i = i.rstrip().split()  #the line is equal to the line without \n and as single elements in a list.
        #print(i) #The following line prints the whole file except for the first line that was already read above.
            for x in range(len(i)-1):   #loops through 0 to the lenght of each line in the file - 1, as the header only contains 20 elements, and the first element of each line is equal to the name of the aminoacid, and only starting from the second element we find the actual values. 
                matrix_name[i[0]+header[x]]=i[x+1] #Assigns to the keys of Blosum50 the first element of each line(first column) + the 0,1,2,3,4,5,6...20th element of the list header to the value of the 2nd,3rd,4th...21st element of each line
        return(matrix_name)

print(matrix(x,y)) 
