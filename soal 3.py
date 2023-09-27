import math

# Kata awal
kata_awal = "Sistem Informasi"

# Menghapus spasi dan mengubah huruf menjadi huruf kecil
kata_awal = kata_awal.replace(" ", "").lower()

# Menghitung jumlah huruf unik dalam kata_awal
jumlah_huruf_unik = len(set(kata_awal))

# Panjang kata yang diinginkan
panjang_kata = 5

# Menghitung jumlah kata yang dapat disusun
jumlah_kata_dapat_disusun = math.factorial(jumlah_huruf_unik) // math.factorial(jumlah_huruf_unik - panjang_kata)

# Menampilkan jumlah kata yang dapat disusun
print(f"Jumlah kata yang dapat disusun adalah {jumlah_kata_dapat_disusun}")
