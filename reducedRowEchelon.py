from Matrix import Matrix

matrix1 = Matrix(matrix=[[1, 2, 3, 0],
                         [2, 4, 9, -3],
                         [1, 2, 5, -2]])

matrix2 = Matrix(matrix=[[3, 3, 3, 0],
                        [2, 5, -1, -12],
                        [-2, -1, -2, -2]])

matrix3 = Matrix(matrix=[[2,2, 6, -2],
                        [-1, 4, -8, 6],
                        [-3, -6, -6, 0]])
                        
matrix4 = Matrix(matrix=[[1,0,-1,1,0,40],
                        [0,0,0,-1,-1,-50],
                        [0,1,1,0,1,60],
                        [-1,-1,0,0,0,-50]])

matrix5 = Matrix(matrix=[[3,6,-3,-6,0],[3,7,-4,-7,0],[2,2,1,-2,0]])
matrix4.reducedRowEchelon()
