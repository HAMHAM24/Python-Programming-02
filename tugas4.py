# Memanggil library statistics
import statistics
sisi = []

# Proses input masing masing sisi
print("\n\n|============| PENENTU TERBENTUKNYA SEGITIGA |============|\n|")
a = int(input("| >> Panjang Sisi 1 : "))
sisi.append(a)
b = int(input("| >> Panjang Sisi 2 : "))
sisi.append(b)
c = int(input("| >> Panjang Sisi 3 : "))
sisi.append(c)

# Proses Penentuan segitiga
sisi.sort()
median = statistics.median(sisi)
if max(sisi) < min(sisi) + median:
    print('| >> Bisa terbentuk segitiga : IYA\n|')
else:
    print('| >> Bisa terbentuk segitiga : TIDAK\n|')
print("|=========================================================|\n\n")