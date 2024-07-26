#!/usr/bin/python3
"""
utf 8 validation:

Write a method that determines if a given data set
represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else
return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
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

    # Masks to check the most significant bits (MSB) of a byte
    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:
        mask_byte = 1 << 7

        if number_bytes == 0:
            # Count the number of leading 1's in the current byte to determine
            # the number of bytes in the UTF-8 character
            while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            # If the byte starts with 0, it is a 1-byte character
            if number_bytes == 0:
                continue

            # UTF-8 characters can be 1 to 4 bytes long
            if number_bytes == 1 or number_bytes > 4:
                return False
        else:
            # Check if the byte is a valid continuation byte,
            # which should start with '10'
            if not (i & mask_1 and not (i & mask_2)):
                return False

        # Decrement the number of bytes expected
        number_bytes -= 1

    # If number_bytes is not 0, then not all bytes have been matched correctly
    if number_bytes == 0:
        return True

    return False
