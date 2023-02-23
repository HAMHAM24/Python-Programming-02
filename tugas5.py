# Input nilai UAS & UTS
print('\n\n|=================|>> MENENTUKAN HASIL UJIAN <<|=================|\n|')
nilUAS = float(input("| >> Input Nilai UAS : "))
nilUTS = float(input("| >> Input Nilai UTS : "))
print('|')
# Rumus nilai akhir (NA)
na = float((nilUTS*0.3) + (nilUAS*0.7))

# Percabangan
if na >= 80:
    print('| >> Lulus')
elif 80 > na >= 70:
    print('| >> Lulus dengan pertimbangan')
elif 70 > na >= 55:
    print('| >> Lulus dengan tugas')
elif 55 > na >= 40:
    print('| >> Mengulang')
elif na < 40:
    print('| >> Gagal')
print('|\n|================================================================|\n\n')