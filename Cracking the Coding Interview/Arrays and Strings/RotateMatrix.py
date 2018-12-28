'''
Rotate Matrix:
    Rotate an image by 90 degrees clockwise.
'''

def rotate_matrix(matrix):
    for layer in range(len(matrix) // 2):
        first, last = layer, len(matrix) - layer - 1
        for i in range(first, last):
            offset = i - first
            # save top
            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last - offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top
    return matrix