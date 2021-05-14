print("NOMOR 1")
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

a = 1
while a < 6: #jumlah maksimal pengulangan
    print((str(a) + " ") * a) #jumlah angka per kolom
    a += 1  ### increment manual

print ("=" *50)


print("NOMOR 2")
# 1
# 1 2
# 1 2 3
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = 6 #jumlah maksimal pengulangan
for row in range(1, n): 
    for column in range(1, row + 1): #jumlah angka per kolom
        print(column, end=' ')
    print("")

print ("=" *50)


print("NOMOR 3")

# 5
# 5 4
# 5 4 3
# 5 4 3 2 
# 5 4 3 2 1

n = 5 #nilai maksimal

for row in range(0, n): 
    for column in range(row + 1): #jumlah angka per baris
        print(n - column, end=" ")
    print() # baris selanjutnya


print ("=" *50)

print("NOMOR 4")

# NOMOR 4.
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

angka = 1
jumlah = 5
while angka < 6: #jumlah maksimal pengulangan
    print((str(angka) + " ") * jumlah) #jumlah angka per kolom
    jumlah -= 1
    angka += 1  ### Decrement Manual

print ("=" *50)


print("NOMOR 5")

# NOMOR 5.
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1


n = 5
for row in range(n, 0, -1):
    for column in range(1, row + 1):
        print(column, end=' ')
    print(" ")

print ("=" *50)


print("NOMOR 6")

# NOMOR 6
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4 
# 5

for row in range(1, 6):
    for column in range(5, row-1,-1):
        print(column, end=" ")
    print()

print ("=" *50)


print("NOMOR 7")

# NOMOR 7

#             *
#           * * *
#         * * * * *
#      * * * * * * * *
#      * * * * * * * * 
#         * * * * *
#           * * *
#             *

n=4
k = 2*n - 2

for i in range (1,n+1,1):
    for k in range(1,n-i+5,1):
        print(" ",end=(" "))
    for j in range (1,((2*i)-1)+1,1):
        print("*",end=" ")
    k = k - 1
    print()
for i in range (n,0,-1):
    for k in range(1, n-i+5,1):
        print(" ",end=(" "))
    for j in range ((2*i)-1,0,-1):
        print("*",end=" ")
    k = k - 1
    print()