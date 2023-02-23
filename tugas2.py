import random

batas1 = 5; batas2 = 8; kesempatan = 3;

print('\n|===================| TEBAK-TEBAKAN ANGKA |===================|')
print('| Peraturan :\n| 1. Kesempatan menebak 3 kali\n')
tebak1 = random.randint(batas1, batas2)

for i in range(kesempatan) :
    tebakan = int(input('| Masukkan Tebakanmu : '))
    if tebakan == tebak1:
        print('| Tebakan Tepat')
        break
    else:
        print('| Tebakan Salah')

print()
print('| Jawaban Benar = ', tebak1)
print('|=============================================================|\n')