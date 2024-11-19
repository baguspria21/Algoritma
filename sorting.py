# quick_sort
def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  else:
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


X = [1, 5, 6, 4, 3, 3, 3, 7, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6,]

# Worst Case: Dalam kasus terburuk, algoritma sorting dapat mencapai 
# kompleksitas waktu O(n^2). Ini terjadi saat pivot element 
# pada quick sort selalu merupakan elemen terkecil atau terbesar 
# dalam array.

# Best Case: Dalam kasus terbaik, algoritma sorting dapat mencapai 
# kompleksitas waktu O(n log n). Ini terjadi saat pivot element s
# elalu merupakan elemen median dari array.

# Average Case: Pada kasus rata-rata, algoritma sorting memiliki 
# kompleksitas waktu O(n log n). Ini terjadi ketika pivot element 
# dipilih secara acak.



# mergesort
def merge_sort(arr):
  if len(arr) > 1:
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
      if left_half[i] < right_half[j]:
        arr[k] = left_half[i]
        i += 1
      else:
        arr[k] = right_half[j]
        j += 1
      k += 1

    while i < len(left_half):
      arr[k] = left_half[i]
      i += 1
      k += 1

    while j < len(right_half):
      arr[k] = right_half[j]
      j += 1
      k += 1


X = [1, 5, 6, 4, 3, 3, 3, 7, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Unsorted array: ", X)
merge_sort(X)
print("Sorted array: ", X)

# Worst Case: O(n log n) karena selalu membagi array menjadi dua bagian
# yang sama dan menggabungkannya. Tidak ada kondisi buruk yang 
# signifikan.

# Best Case: O(n log n), karena operasi pembagian dan penggabungan
# tetap sama.

# Average Case: O(n log n), rata-rata performanya selalu stabil.
