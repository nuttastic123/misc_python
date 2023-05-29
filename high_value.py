arr = [32, 8709, 2, 87907, 76903333, 1321, 3870, 32, 100, 32, 1]

max = arr[0]

for i in range(len(arr)):
    if arr[i] >= max:
        max = arr[i]

print(f"The max number in the array is: {max}")