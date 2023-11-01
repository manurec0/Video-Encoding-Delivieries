# This script contains the methods for exercise 5 and applies a run-length encoding in a given array
def run_length(byte_array):
    encoded_array = []
    count = 0
    for i in range(0, len(byte_array)):
        if byte_array[i] == 0:
            if count == 0:
                encoded_array.append(0)
            count += 1

        else:
            if count != 0:
                encoded_array.append(count)
            encoded_array.append(byte_array[i])
            count = 0
    return encoded_array


# ENTER ARRAY
bit_array = [2, 1, 4, 0, 0, 0, 0, 0, 1, 2, 0, 4]

print(run_length(bit_array))