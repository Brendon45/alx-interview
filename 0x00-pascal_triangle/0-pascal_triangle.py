def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.
    
    Parameters:
    n (int): Number of rows in Pascal's triangle
    
    Returns:
    List[List[int]]: Pascal's triangle represented as a list of lists
    """
    # If n is less than or equal to 0, return an empty list
    if n <= 0:
        return []

    # Initialize an empty list to hold all the rows of Pascal's triangle
    triangle = []

    # Loop through each row index from 0 to n-1
    for i in range(n):
        # Create a new row with i+1 elements, all set to 1
        row = [1] * (i + 1)
        # Calculate the values for the internal elements of the row
        # (skip the first and last elements, as they are always 1)
        for j in range(1, i):
            # Each element is the sum of the two elements directly above it
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        # Append the newly created row to the triangle
        triangle.append(row)

    # Return the complete Pascal's triangle
    return triangle
