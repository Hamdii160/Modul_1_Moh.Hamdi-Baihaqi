# Suku ke-3 dan ke-7
suku_3 = 9
suku_7 = 17

# Menghitung beda (d) antara suku ke-7 dan suku ke-3
d = (suku_7 - suku_3) / (7 - 3)

# Menggunakan rumus umum untuk mencari suku ke-n
n = int(input("Masukkan indeks suku (n) yang ingin dicari: "))

# Menghitung suku ke-n
suku_n = suku_3 + (n - 3) * d

# Menghitung jumlah suku ke-n
jumlah_n = (n / 2) * (2 * suku_3 + (n - 1) * d)

# Menampilkan hasil
print(f"Suku ke-{n} adalah {suku_n}")
print(f"Jumlah suku ke-{n} adalah {jumlah_n}")
