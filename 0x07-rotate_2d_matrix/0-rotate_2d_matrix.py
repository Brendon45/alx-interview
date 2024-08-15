#!/usr/bin/python3
"""
Module 0-rotate_2d_matrix
A function to rotate an n x n 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """ Rotate an n x n 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (int): A 2D matrix represented as a list of lists.

    Rotates the matrix in place without using extra space.
    """

    N = len(matrix)  # Determine the size of the matrix (assuming it's square)

    # Step 1: Transpose the matrix
    # Swap elements across the diagonal
    for i in range(N):
        for j in range(i, N):
            # Swap elements matrix[i][j] and matrix[j][i]
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    # Step 2: Reverse each row
    # This step achieves the 90-degree rotation
    for i in range(N):
        for j in range(N // 2):
            # Swap elements matrix[i][j] and matrix[i][N - 1 - j]
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][N - 1 - j]
            matrix[i][N - 1 - j] = temp
