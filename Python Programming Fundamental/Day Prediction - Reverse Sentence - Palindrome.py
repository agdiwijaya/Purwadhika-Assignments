print(("=" * 30) + "NUMBER 1" + ("=" * 30))

# ##### Personal Assignment
# 1. 
# Kita memiliki daftar Hari 

# Input :
# Masukkan nama hari : .... YYYY
# Masukkan Jumlah : ... x 

# Output :
# Hari ini hari YYYY x hari lagi adalah hari .... 

# contoh :
# Masukkan nama hari : Kamis 
# Masukkan jumlah hari : 3 
# Hari ini hari kamis, 3 hari lagi hari Minggu 

# Ketentuan :
# - Jumlah bisa menerima nilai negatif dan positif
# - Cek Hari : Jika tidak ada nama hari => Tidak ada nama hari/ Nama hari yg anda masukkan salah 
# - Jumlah tidak bisa desimal maupun string 
# - Tidak ada batasan angka minimal maupun maksimal 



inputhari = input("Input day name: ")
inputhari1 = inputhari.lower()
inputangka = input("Input number: ")

hari = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

try:
    inputangka = int(inputangka)
    try:
        tambahangka = (((hari.index(inputhari1))) + inputangka) % 7
        hasilhari = hari[tambahangka]
        print(f"Your inputted day is {inputhari.capitalize()}, {inputangka} more days is {hasilhari.capitalize()}")
    except: 
        print("Day name is not recognized")
except:
    print("Only accept integer")

print("=" * 67)

print(("=" * 30) + "NUMBER 2" + ("=" * 30))

# # 2.
# # input : 
# # Masukkan kalimat :

# # Output :
# # Reverse per kata ...
# # contoh :
# # Masukkan Kalimat : Nama Saya Ribut

# # Output : amaN ayaS tubiR

# # Ketentuan : hanya menerima String 


kalimat = input("Input sentence: ")

try:
    kalimat = str(kalimat)
    for word in kalimat.split():
        print(word[::-1], end=" ")
except:
    print("Only accept string")

print("\n")

print("=" * 67)
print(("=" * 30) + "NUMBER 3" + ("=" * 30))

# 3.
# Palindrome 
# Input :
# Masukkan kata : 

# Output :
# Kata tersebut .... merupakan Palindrome / Bukan Palindrome 

# Contoh Palindrome
# Masukkan kata :
# Katak 
# Kata tersebut (Katak) merupakan Palindrome

# Masukkan kata :
# Makam 
# Kata tersebut (Makam) merupakan Palindrome

# Ketentuan :
# - Hanya menerima String 
# - Insensitive Case 

# kalimat = input("Masukkan kalimat: ")
# for word in kalimat.split():
#     print(word[::-1], end=" ")

kata = input("Input sentence: ")
kata1 = kata.lower()

try:
    kata1 = str(kata1)
    p = ""
    for i in kata1:
        p = i + p
    
    if (kata1 == p):
        print(f"'{kata}' is a Palindrome")
    else:
        print(f"'{kata}' not a Palindrome")
except:
    print("Only accept string")

print("=" * 67)