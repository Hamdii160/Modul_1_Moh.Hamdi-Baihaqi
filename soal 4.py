import math

# Luas selimut kerucut
luas_selimut = 967.12  # dalam cm^2

# Tinggi kerucut
tinggi = 20  # dalam cm

# Garis pelukis kerucut
garis_pelukis = 22  # dalam cm

# Menghitung jari-jari kerucut (r) menggunakan rumus luas selimut
jari_jari = luas_selimut / (math.pi * garis_pelukis)

# Menghitung volume kerucut
volume = (1/3) * math.pi * jari_jari**2 * tinggi

# Mengonversi volume ke liter (1 liter = 1000 cm^3)
volume_liters = volume / 1000

# Menampilkan hasil
print(f"isi liter dari wadah kerucut adalah {volume_liters:.2f} liter")
