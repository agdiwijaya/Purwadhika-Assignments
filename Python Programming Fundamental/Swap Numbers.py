print("NUMBER 1")

# HANYA GUNAKAN OPERASI MATEMATIS Untuk Menyelesaikan Soal 

# 1.
# input :
# Masukkan 4 Digit Angka : 9853
# Output: 
# 5398

# Ketentuan :
# - User hanya boleh input 4 Digit angka ==> Keluar Notif "Hanya menerima angka 4 digit"
# - Tidak menerima angka negatif
# - Tidak menerima string atau desimal
# - Angka maksimal 9999
# - Input dan Output Berupa Integer

angka = input("Input 4 digit number: ")
try:
    if len(angka)<4:
        print("Inputted number less than 4 digit")
    else:
        angka = int(angka)        
        if angka<0:
            print("Number can't be negative")
        elif angka>9999:
            print("Inputted number is beyond the limit")  
        else:
            angkabelakang = angka//100
            pengalibelakang = angkabelakang * 100
            angkadepan1 = angka - pengalibelakang
            angkadepan = angkadepan1 * 100
            jumlah = angkadepan + angkabelakang
            if jumlah<1000:
                print("%04d" % jumlah) 
            else: 
                print(jumlah)
except:
    print("Only accept integer")

print("=" *  50)
print("NUMBER 2")

# 2.
# Input :
# Masukkan 2 digit angka pertama : 57
# Masukkan 2 digit angka kedua : 30 

# Output :
# 5730

# - User hanya boleh input 2 digit untuk masing-masing 
# - Angka maksimal untuk masing-masing digit 99 
# - Tidak menerima angka negatif
# - Tidak menerima String atau desimal 
# - Input dan Output berupa Integer

angkapertama = input("Input the first 2 digit:") 
angkakedua = input("Masukkan the last 2 digit:") #disimpen di luar try supaya error keluar setelah dimasukin semua value
try:
    if len(angkapertama)<2 or len(angkakedua)<2:
        print("Inputted number less than 2 digit")
    else:
        angkapertama = int(angkapertama) #untuk memfilter input nilai di luar integer
        angkakedua = int(angkakedua)
        jawaban = (angkapertama * 100) + angkakedua        
        if angkapertama<0 or angkakedua<0:
            print("Number can't be negative")
        elif angkapertama>99 or angkakedua>99:
            print("Inputted number is beyond the limit")  
        else:
            print("Output:", jawaban)
except:
    print("Only accept integer")
    
