def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left + right
    return result

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    less = [x for x in array[1:] if x <= pivot]
    greater = [x for x in array[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

x = [1, 5, 6, 4, 3, 3, 3, 7, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

sorted_merge = merge_sort(x.copy())
sorted_quick = quick_sort(x.copy())

print("Sorted with Merge Sort:", sorted_merge)
print("Sorted with Quick Sort:", sorted_quick)

# Merge Sort
# Pada Merge Sort best case nya yaitu setiap kali array dibagi 2, pengabungan memerlukan iterasi di kedua array. Kemudian pada kompleksitas untuk setiap level rekursi adalah O(n), dan terdapat log (n) level rekursi. Kompleksitas best casenya O(n log n).
# Pada Worst Case nya sama saja dengan base case yang proses pengurutan menggunakan pembagian lalu penggabungan secara rekursif. Kompleksitasnya sama dengan best case diatas.
# Pada Average Case karena merge sort selalu membagi dan menggabungkan array dengan cara yang sama maka sama saja dengan best case dan worst case diatas.

# Quick Sort
# Pada Quick Sort menggunakan elemen terakhir sebagai pivot untuk membagi array menjadi 2 bagian yang sama besar pada setiap rekursif yang terdapat log (n) level rekursi dengan masing-masing memproses elemen n dan kompleksitas best casenya O(n log n).
# Pada Worst Case nya array tidak terbagi rata menyebabkan kedalaman rekursi hingga n, dan kompleksitasnya adalah O(n2).
# Pada Average Case kompleksitas rata-rata nya mendekati O(n log n), dan kompleksitasnya sama dengan best casenya. 


