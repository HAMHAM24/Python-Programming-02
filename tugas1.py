print('\n|============| Konversi Suhu |============|')
print('Masukkan pilihan :\n1. Celcius to Farenheit\n2. Farenheit to Celcius')
pilihan = input("Pilihan : ")

if pilihan == '1':
    print('<--------- Celcius to Farenheit --------->')
    inCel = int(input('Masukkan suhu C : '))
    hasilF = int((9/5 * inCel) + 32)
    print('Hasil konversi F = ', hasilF, '°F')
elif pilihan == '2':
    print('<--------- Farenheit to Celcius --------->')
    inFar = int(input('Masukkan suhu F : '))
    hasilC = int((inFar-32) * 5/9)
    print('Hasil konversi C = ', hasilC, '°C')
else:
    print('<-------- PILIHAN TDAK DITEMUKAN -------->')