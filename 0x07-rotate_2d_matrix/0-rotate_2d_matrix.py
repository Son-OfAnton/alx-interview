#!/usr/bin/python3
"""
This function rotates a matrix 90 degrees clockwise
by transposing it first and reversing each row hence
it is inplace.
"""


def rotate_2d_matrix(matrix):
	""" This function rotates a matrix 90 degrees clockwise """
	size = len(matrix)
		
	# transposing
	for rx in range(size):
	    for cx in range(rx+1, size):
		matrix[rx][cx], matrix[cx][rx] = matrix[cx][rx], matrix[rx][cx]
		
	for row in matrix:
	    row.reverse()
