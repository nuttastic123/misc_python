# Python Scripts

This repository contains the following Python scripts:

## high_value.py

This script calculates the maximum value in a given array. It follows the following steps:

1. Initialize an array `arr` with the values: [32, 8709, 2, 87907, 76903333, 1321, 3870, 32, 100, 32, 1].
2. Initialize a variable `max_value` with the first element of the array (`arr[0]`).
3. Iterate over the elements of the array using a `for` loop.
4. Check if the current element (`arr[i]`) is greater than or equal to the current maximum value (`max_value`).
5. If the condition is true, update the `max_value` with the new maximum value.
6. After iterating through all elements, print the maximum number in the array using the `print` statement.

## reverse_list.py

This script sorts a dictionary by file size in descending order. It follows the following steps:

1. Define a function `sort_by_filesize` that takes a dictionary as input.
2. Inside the function, define another function `convert_filesize_to_float` that converts the file size from a string representation to a float value.
3. Create a list `items` from the dictionary items.
4. Sort the list `items` based on the file size value using the `convert_filesize_to_float` function as the sorting key in descending order.
5. Convert the sorted list `items` back into a dictionary and return the ordered dictionary.
6. Create a dictionary `file_size_dict` with file names as keys and their corresponding file sizes as values.
7. Call the `sort_by_filesize` function with the `file_size_dict` dictionary as input and assign the result to the `ordered_dict` variable.
8. Iterate over the items of the `ordered_dict` using a `for` loop.
9. Print each key-value pair in the format "key: value" using the `print` statement.

