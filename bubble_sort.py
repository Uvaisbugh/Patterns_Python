#bubble Sort
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i]),
    
print("\n")

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = 10
for i in range(n):
    print(fib(i))