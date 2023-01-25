def validUTF8(data):
    # Initialize a counter for the number of bytes in a multi-byte character
    count = 0
    # Iterate through each byte in the data
    for byte in data:
        # Get the 8 least significant bits of the byte
        byte = byte & 0b11111111
        # Check if this byte is a continuation byte (starts with 10)
        if count > 0:
            if (byte >> 6) != 0b10:
                return False
            count -= 1
        # Check if this byte is a single-byte character (starts with 0)
        elif (byte >> 7) == 0:
            count = 0
        # Check if this byte is the start of a multi-byte character (starts with 110, 1110, or 11110)
        elif (byte >> 5) == 0b110:
            count = 1
        elif (byte >> 4) == 0b1110:
            count = 2
        elif (byte >> 3) == 0b11110:
            count = 3
        # If this byte is none of the above, it is not a valid UTF-8 character
        else:
            return False
    # If the count is not zero at the end, it means there were not enough continuation bytes
    if count != 0:
        return False
    # If all bytes were checked and the count is zero, the data is a valid UTF-8 encoding
    return True
