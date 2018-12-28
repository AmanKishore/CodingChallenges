'''
Rotate Matrix:
    Rotate an image by 90 degrees clockwise.
'''

def rotate_matrix(matrix):
    for layer in range(len(matrix) // 2):
        last = len(matrix) - layer - 1 # The last element in the row that needs to be rotated
        for i in range(layer, last):
            offset = i - layer # The element in that layer
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[last - offset][layer]

            # bottom -> left
            matrix[last - offset][layer] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top
    return matrix