print("NOMOR 3")
print("=" * 20)

# 3.
# A = Himpunan bilangan Genap dari 1 - 100
# B = Himpunan bilangan Ganjil dari 1 - 100
# C = Himpunan bilangan negatif lebih besar dari atau sama dengan -100
# D = Himpunan bilangan Prima dari 1 - 100
# E = Himpunan bilangan Komposit dari 1 - 100

# Bilangan Komposit adalah Lawan dari bilangan Prima 

# u = union 
# n = irisan 

# a. A u B u C u D u E 
# b. (A n B) u (D n E)
# c. (A u B) n (D u E)
# d. (A u B) - (D u E)
# e. (A u B u C) - (A n E)

# Ketentuan :
# Membuat Isi himpunannya menggunakan Fungsi menggunakaan IF atau LOOPING atau keduanya 
# Bukan Manual
# A = {2, 4, 6, 8, dst } X


bilangangenap = []
for genap in range(1,101,1):
    if genap % 2 == 0: 
        bilangangenap.append(genap)        
A = bilangangenap

print("=" * 50)

bilanganganjil = []
for ganjil in range(1,101,2):
    if ganjil % 1 == 0: 
        bilanganganjil.append(ganjil)     
B = bilanganganjil

print("=" * 50)

bilangannegatif = []
for negatif in range(-100,0,1):
    bilangannegatif.append(negatif)
C = bilangannegatif

print("=" * 50)


listangka = [prima for prima in range(2, 100)]
 
bilanganprima = []
for prima in listangka:
    if (prima==2 or prima==3 or prima==5 or prima==7) or (prima%2 != 0 and prima%3 != 0 and prima%5 != 0 and prima%7 != 0):
        bilanganprima.append(prima)

D = bilanganprima

print("=" * 50)

listangka = [komposit for komposit in range(1, 100)]
bilangankomposit = []
for komposit in listangka:
    if not (komposit==2 or komposit==3 or komposit==5 or komposit==7) and not (komposit%2 != 0 and komposit%3 != 0 and komposit%5 != 0 and komposit%7 != 0):
        bilangankomposit.append(komposit)
 
E = bilangankomposit

setA = set(A)
setB = set(B)
setC = set(C)
setD = set(D)
setE = set(E) 

print("a. A u B u C u D u E")
print("Hasil = {}".format(setA | setB | setC | setD | setE))
print("b. (A n B) u (D n E)")
print("Hasil = {}".format((setA & setB) | (setD & setE)))
print("c. (A u B) n (D u E)")
print("Hasil = {}".format((setA | setB) & (setD | setE)))
print("d. (A u B) - (D u E)")
print("Hasil = {}".format((setA | setB) - (setD | setE)))
print("e. (A u B u C) - (A n E)")
print("Hasil = {}".format((setA | setB | setC) - (setA & setE)))