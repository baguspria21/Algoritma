# Algoritma
# Nama : Bagus pria utama
# nim : F55123056
# Kelas : B
# Penjelasan kuis 2
# NAVIE
Pada kode ini, algoritma Bubble Sort digunakan untuk mengurutkan array yang berisi bilangan acak. Fungsi generate_random_numbers menghasilkan 30 angka acak dalam rentang 0 hingga 100, dengan menggunakan seed 40 untuk memastikan hasil yang konsisten. Fungsi bubble_sort_optimized melakukan pengurutan dengan metode Bubble Sort yang dioptimalkan. Algoritma ini membandingkan elemen bersebelahan dalam array dan menukarnya jika urutannya salah. Optimasi dilakukan dengan menggunakan variabel swapped untuk mendeteksi apakah ada pertukaran selama iterasi. Jika tidak ada pertukaran yang terjadi pada iterasi tertentu, maka array dianggap sudah terurut, dan proses pengurutan dapat dihentikan lebih awal, meningkatkan efisiensi pada kasus terbaik.

Namun, meskipun optimasi ini meningkatkan kinerja dalam kasus terbaik (ketika array sudah hampir terurut), Bubble Sort tetap memiliki kompleksitas waktu O(n²) dalam kasus rata-rata dan terburuk. Hal ini terjadi karena algoritma ini harus memeriksa dan membandingkan setiap elemen dalam array secara berulang kali. Meskipun lebih efisien dibandingkan dengan versi Bubble Sort yang tidak dioptimalkan, algoritma ini masih kurang efisien untuk array besar dibandingkan dengan algoritma lain seperti Merge Sort atau Quick Sort. Kelebihan dari Bubble Sort adalah kesederhanaannya dan mudah dipahami, tetapi kekurangannya terletak pada kinerjanya yang menurun signifikan pada data yang lebih besar.

# CONQUER
Dalam kode ini, algoritma Merge Sort digunakan untuk mengurutkan sebuah array yang berisi bilangan acak. Fungsi generate_random_numbers menghasilkan sejumlah angka acak dengan menggunakan seed tertentu untuk memastikan hasil yang konsisten setiap kali program dijalankan. Fungsi merge_sort_with_best_case_check berfungsi untuk mengurutkan array, dengan terlebih dahulu memeriksa apakah array sudah terurut. Jika array sudah terurut, fungsi langsung mengembalikannya tanpa perlu melakukan langkah-langkah lebih lanjut, sehingga dapat menghemat waktu pemrosesan dalam kasus terbaik. Jika array tidak terurut, proses lanjut ke pemecahan array menjadi dua bagian, yang kemudian diurutkan secara rekursif dan digabungkan kembali menggunakan fungsi merge.

Namun, meskipun penambahan pengecekan array yang sudah terurut ini membuat algoritma lebih efisien dalam kasus terbaik (O(n)), Merge Sort tetap memiliki kompleksitas waktu O(n log n) pada kasus rata-rata dan terburuk. Hal ini disebabkan oleh proses pembagian dan penggabungan yang harus dilakukan pada setiap tahap rekursi, meskipun array terurut. Keuntungan utama dari Merge Sort dibandingkan algoritma lain seperti Bubble Sort adalah kinerjanya yang lebih konsisten pada array besar. Sementara Bubble Sort bisa memiliki kinerja yang sangat buruk (O(n²)) pada array yang tidak terurut, Merge Sort lebih stabil dan efisien meskipun memerlukan lebih banyak ruang memori (O(n)) untuk menyimpan hasil penggabungan array.
