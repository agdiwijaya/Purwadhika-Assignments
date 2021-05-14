print("=" * 50)
print("NUMBER 1")
print("=" * 50)
# 
# 1. Gunakan Return Function 
# Buat Kalkulator 

# Input :
# Masukkan Angka 1:
# Masukkan Angka 2:
# Masukkan Operator : ... (Operator hanya terbatas pada + / - *)

# Output :
# Misal angka1 = 8
# angka2 = 10
# operator +

# Hasil dari 8 + 10 = 18

# fungsi penjumlahan
def tambah(x, y):
   return x + y
# fungsi pengurangan
def kurang(x, y):
   return x - y
# fungsi perkalian
def kali(x, y):
   return x * y
# fungsi pembagian
def bagi(x, y):
   return x / y


# Meminta input dari user
try:
    num1 = float(input("Input first digit: "))
    num2 = float(input("Input second digit 2: "))
    # menu operasi
    operator = input("Input operator (+) (-) (*) (/): ")
    if operator == '+':
        print(num1,"+",num2,"=", tambah(num1,num2))
    elif operator == '-':
        print(num1,"-",num2,"=", kurang(num1,num2))
    elif operator == '*':
        print(num1,"*",num2,"=", kali(num1,num2))
    elif operator == '/':
        if num2 == 0:
            print("Can't take 0")
        else:
            print(num1,"/",num2,"=", bagi(num1,num2))
    else:
        print("Operator is wrong")
except:
    print("Number inputted is wrong")

# # Meminta input dari user
# def kalkulator():
#     try:
#         num1 = float(input("Masukkan Angka 1: "))
#         num2 = float(input("Masukkan Angka 2: "))
#         # menu operasi
#         operator = input("Masukkan Operator: ")
#         if operator == '+':
#             return num1 + num2
#         elif operator == '-':
#             return num1 - num2
#         elif operator == '*':
#             return num1 * num2
#         elif operator == '/':
#             return num1 / num2
#         else:
#             return "Input salah"
#     except:
#         return "Angka yang dimasukkan salah"

# print(kalkulator())

print("=" * 50)
print("NUMBER 2")
print("=" * 50)

# 2.
# Caesar Cipher
# Input :
# Masukkan Kata : ... (hanya alfabet)
# Masukkan angka : ... (hanya integer dari minus sampai positif tidak dibatasi)

# Output :
# Hasil Caesar Cipher

# Contoh :
# Masukkan kata : Joni
# Masukkan angka : 2

# Output : Hasil Caesar Cipher : lqpk

# Kata : Joni 
# angka : -2
# imlg 
# Deadline : Nanti Malam


alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesarcipher():
    kata = input("Input a word: ")
    lowerkata = kata.lower()
    kosong = []
    try:
        angka = int(input("Input the number: "))
        if lowerkata.isalpha():
            for i in lowerkata:
                indexalfabet = alfabet.index(i)
                tambahalfabet = (indexalfabet + angka) % 26
                hasilalfabet = alfabet[tambahalfabet]
                kosong.append(hasilalfabet)
            else:
                kosong = "".join(kosong)
                return "Result of Caesar Cipher convertion from ({}) is ({})".format(kata, kosong)
        else:
            return "Only take 1 word"
    except:
        return "Input number"        

print(caesarcipher())