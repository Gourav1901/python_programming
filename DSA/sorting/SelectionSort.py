n = int(input())
arr = list(map(int, input().split()))


for i in range(n):
    # Find the minimum element in the remaining unsorted array
    min_index = i
    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    # Swap the found minimum element with the first element of the unsorted array
    arr[i], arr[min_index] = arr[min_index], arr[i]


for i in arr:
    print(i, end=" ")