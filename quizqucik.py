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