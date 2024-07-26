#!/usr/bin/python3
"""
UTF-8 validation:

Write a method that determines if a given data set
represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else
return False.
A character in UTF-8 can be 1 to 4 bytes long.
The data set can contain multiple characters.
The data will be represented by a list of integers.
Each integer represents 1 byte of data, therefore you
only need to handle the 8 least significant bits of each
integer.
"""

def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list[int]): A list of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    number_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:
        mask_byte = 1 << 7

        if number_bytes == 0:
            # Count the number of leading 1's in the current byte
            while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            # If the number of bytes is 1 or more than 4, it's invalid
            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            # Check if the current byte is a valid continuation byte
            if not (i & mask_1 and not (i & mask_2)):
                return False

        number_bytes -= 1

    # All characters must be fully formed
    return number_bytes == 0

# Example usage
print(validUTF8([197, 130, 1]))  # True
print(validUTF8([235, 140, 4]))  # False
