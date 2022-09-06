from Matrix import Matrix

# Here's an example:
exampleMatrix = Matrix(matrix=[[1,0,0,0,-1,50],
                                [-1,1,0,0,0,-30],
                                [0,-1,1,0,0,40],
                                [0,0,-1,1,0,-25],
                                [0,0,0,-1,1,-35]
                                ])  

exampleMatrix.reducedRowEchelon()
exampleMatrix.rank()    
exampleMatrix.size()
exampleMatrix.parameter()