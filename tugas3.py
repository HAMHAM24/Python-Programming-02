# Proses input detik
print('\n\n|=====================| KONVERSI NILAI DETIK |=====================|\n|')
detik = int(input("| Masukkan Jumlah Detik : "))

# Rumus konversi
jam = int(detik/3600)
detik = detik-((60*60)*jam)
menit = int(detik / 60)
detik = int(detik -(60*menit))

# Output
print('| Hasil Konversi        : ', jam,' Jam ', menit,' Menit ', detik,' Detik ', '\n|')
print('|==================================================================|\n\n')