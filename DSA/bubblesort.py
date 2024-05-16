
def bubblesort(arr: list) -> list:
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

t = [4, 0, 1, 10, 9, 3]
print(bubblesort(t))