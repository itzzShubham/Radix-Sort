def radix_sort(arr):
   
    max_num = max(arr)
   
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    
    for i in range(1, 10):
        count[i] += count[i - 1]

   
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

   
    for i in range(n):
        arr[i] = output[i]
arr = [5, 2, 9, 1, 5, 6, 8, 10]
sorted_arr = radix_sort(arr)
print(sorted_arr) 
