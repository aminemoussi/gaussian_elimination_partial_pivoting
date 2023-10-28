import numpy as np
import time

def gaussian_elimination(a_matrix, b_matrix):
    if (a_matrix.shape[1] != b_matrix.shape[0]):
        print("Error: rows in A is not equate column in B.")
    elif (b_matrix.shape[1] != 1) or (b_matrix.shape[0] != a_matrix.shape[0]):
        print("Error: number of columns in B does not equate to one, or A is not squared.")
    else:
        print("Matrix dimentions Accepted.")
        time.sleep(1.5)


    #creating thre augmented matrix
    augmented_matrix = np.concatenate((a_matrix, b_matrix), axis= 1)
    print("The initial augmented matrix is:\n")
    print(augmented_matrix)

    n = len(b) #num of rows
    doable = True

    for k in range(n):        #interchanging the rows to eliminate the null pivots
        if augmented_matrix[k][k] == 0:
            for i in range(k + 1, n ):
                if augmented_matrix[i][k] != 0:
                    augmented_matrix[[i, k]] = augmented_matrix[[k, i]]
                    break
                elif i == n :
                    doable = False
                    break


    if not doable :
        print("IMPOSSIBLE: to be done ",k,"th pivot couldn't be fixed.")
        time.sleep(1.5)
    else:
        print("All pivots have been fixed, current matrix:")
        print(augmented_matrix)
        time.sleep(3)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if augmented_matrix[j][i] != 0:
                    scalability_factor = augmented_matrix[j][i] / augmented_matrix[i][i]
                    for k in range(i, n + 1):
                        print(augmented_matrix[j][k], augmented_matrix[i][k], scalability_factor)
                        augmented_matrix[j][k] = augmented_matrix[j][k] - augmented_matrix[i][
                            k] * scalability_factor
                        print(augmented_matrix)


                #scalability_factor = a_matrix[j][i] / a_matrix[i][i]
                #augmented_matrix[j] = augmented_matrix[j] - (scalability_factor * augmented_matrix[i])
                #print(augmented_matrix)
                #j = j + 1




    print("Final matrix: \n")
    print(augmented_matrix)



a = np.array([[0, -1, 1],
              [2, 3, -1],
              [3, -2, -9]
              ])
b = np.array([[8],
              [-2],
              [9]
              ])

gaussian_elimination(a, b)