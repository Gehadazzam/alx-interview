#!/usr/bin/python3
"""/new Moduel"""
def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.
    
    Parameters:
    n (int): The number of rows to generate. Must be a positive integer.
    
    Returns:
    list: A list of lists representing Pascal's Triangle up to the nth row.
    
    Raises:
    ValueError: If n is less than or equal to 0.
    """
    
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    
    pyramid = [[1]]  # Initialize the pyramid with the first row
    
    for i in range(1, n):
        line = [1]  # Start each row with a 1
        
        # Calculate the middle elements of the row
        for j in range(1, i):
            line.append(pyramid[i-1][j-1] + pyramid[i-1][j])
        
        line.append(1)  # End each row with a 1
        
        pyramid.append(line)  # Add the row to the pyramid
    
    return pyramid
