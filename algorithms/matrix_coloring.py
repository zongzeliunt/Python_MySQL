def element_coloring(matrix, line, col, num):
    line_limit = len(matrix)
    col_limit = len(matrix[0])
    if line == -1 or col == -1:
        return
    if line == line_limit or col == col_limit:
        return
    
    if matrix[line][col] == 1:
        matrix[line][col] = num
        element_coloring(matrix, line - 1, col, num)
        element_coloring(matrix, line + 1, col, num)
        element_coloring(matrix, line, col - 1, num)
        element_coloring(matrix, line, col + 1, num)


def coloring (matrix):
    line_limit = len(matrix)
    col_limit = len(matrix[0])
    current_color = 2
    for i in range (0, line_limit):
        for j in range (0, col_limit):
            if matrix[i][j] == 1:
                element_coloring(matrix, i, j, current_color)
                current_color += 1
    



matrix = [  [0,1,0,0],
            [1,1,0,0],
            [0,1,0,1],
            [1,0,0,1]]

coloring (matrix)

print matrix
