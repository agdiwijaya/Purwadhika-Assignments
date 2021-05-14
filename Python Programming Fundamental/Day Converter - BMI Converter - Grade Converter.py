print("NUMBER 1")
# Input : 
# Masukkan jumlah hari : ....
# Output :
# Nyatakan jumlah hari tersebut dalam 
# ... tahun ... bulan ... minggu ... hari

# contoh:
# masukkan jumlah hari : 35
# output:
# 00 tahun 01 bulan 00 minggu 05 hari

# Ketentuan :
# - format output dalam format 2 digit
# - 1 tahun = 365 hari
# - 1 bulan = 30 hari
# - Jumlah hari maksimal 4000 ==> jika di atas keluar notif "Jumlah hari di atas batas"
# - Jumlah hari tidak bisa menerima nilai di bawah 0 ==> "Jumlah hari di bawah batas"
# - Jumlah hari tidak bisa menerima string, atau angka desimal ==> keluar notif "Jumlah hari yang Anda masukkan salah"
try:
    nomor = int(input("Input number of days to convert: "))   
    if nomor<=0:
        print("Number of days can't be negative")
    elif nomor>0 and nomor<=4000:
        hitungantahun=nomor//365
        hitunganhari=nomor%365
        hitunganbulan=hitunganhari//30
        hitunganhari=hitunganhari%30
        hitunganminggu=hitunganhari//7
        hitunganhari=hitunganhari%7
        print(f'{"%02d" % hitungantahun} year {"%02d" % hitunganbulan} month {"%02d" % hitunganminggu} week {"%02d" % hitunganhari} day')
    else:
        print("Number of days limit is 4000")
except:
    print("Only accept integer")

print("="* 50)

print("NUMBER 2")
# 2.
# Hitung BMI (Body Mass Index)
# Rumus BMI : massa (kg) / tinggi (dalam meter) pangkat 2

# Input:
# Masukkan tinggi badan (dalam cm) :
# Masukkan berat badan (dalam kg) :

# Output:
# Tinggi badan anda ... meter (meter) dan berat anda ... kg (kg) BMI anda ... (nilai BMI) dan anda termasuk ... (sesuai kondisi)

# Kondisi:
# BMI < 18.5 ==> Berat badan kurang
# 18.5  - 24.9 ==> Berat badan ideal
# 25 - 29.9 ==> Berat badan berlebih
# 30 - 39.9 ==> Berat badan sangat berlebih
# BMI > 40 ==> Obesitas

# Ketentuan:
# - nilai BMI pada output, dibulatkan 2 angka desimal
# - nilai tinggi dan massa tidak menerima angka negatif ==> keluar notif "Tidak menerima angka negatif"
# - nilai input tidak menerima desimal atau string ==> keluar notif "Angka yang anda masukkan salah"
# - batas maksimal tinggi badan : 300 cm, batas maksimal berat badan : 250 kg ==> salah satu salah atau semua salah keluar notif ==> "Tinggi/Berat badan anda di atas batas"
# - notifikasi keluar setelah user input tinggi dan berat

print("="* 50)

try:
    tinggibadan = int(input("Input height (in cm):"))
    beratbadan = int(input("Input weight (in kg):"))
    nilaibmi = beratbadan / ((tinggibadan / 100) ** 2)
    tinggibadan = (tinggibadan / 100)
    if tinggibadan<=0 or beratbadan<=0:
        print("Number can't be negative")
    elif tinggibadan>3 or beratbadan>250:
        print("Height/Weight is beyond the limit")    
    elif nilaibmi<18.5:
        hasilBMI = "Lack of weight"
    elif nilaibmi>=18.5 and nilaibmi<=24.9:
        hasilBMI = "Ideal BMI"
    elif nilaibmi>=25 and nilaibmi<=29.9:
        hasilBMI = "Excess Body Weight"
    elif nilaibmi>=30 and nilaibmi<=39.9:
        hasilBMI = "Too Excess of Body Weight"    
    else:
        hasilBMI = "Obesity"
    tinggibadan = round(tinggibadan,2)
    nilaibmi = round(nilaibmi,2)
    print(f"Your height is {tinggibadan} meter  dan your weight is {beratbadan} kg, your BMI is {nilaibmi} and you have {hasilBMI} status")
except:
    print("Only accept integer")

print("="* 50)

print("NOMOR 3")

# 3.
# Input : 
# Masukkan nilai : ...

# Output:
# Nilai anda ... dan anda ... (sesuai kondisi)

# Kondisi:
# >=90 : Grade A
# >=85 : Grade A-
# >=80 : Grade B
# >=75 : Grade B-
# >=70 : Grade C
# >=65 : Grade D
# <65 dan >=40: Perlu remedial
# <40 : Tidak lulus

# Ketentuan:
# - Nilai maksimum 100
# - Nilai minimum 0
# - Jika nilai di atas 100 : "Nilai di luar jangkauan"
# - Jika nilai di bawah 0 : "Tidak menerima angka negatif"
# - Dapat menerima nilai desimal

# 3.
# Input : 
# Masukkan nilai : ...

# Output:
# Nilai anda ... dan anda ... (sesuai kondisi)

# Kondisi:
# >=90 : Grade A
# >=85 : Grade A-
# >=80 : Grade B
# >=75 : Grade B-
# >=70 : Grade C
# >=65 : Grade D
# <65 dan >=40: Perlu remedial
# <40 : Tidak lulus

# Ketentuan:
# - Nilai maksimum 100
# - Nilai minimum 0
# - Jika nilai di atas 100 : "Nilai di luar jangkauan"
# - Jika nilai di bawah 0 : "Tidak menerima angka negatif"
# - Dapat menerima nilai desimal

try:
    nilai = float(input("Input your score:"))
    if nilai>100:
        print("Score is beyond the limit")
    elif nilai<0:
        print("Number can't be negative")    
    elif nilai>=90 and nilai<=100: 
        hasilnilai = "Grade A"
        print(f"Your score is {nilai} and your grade is {hasilnilai}")
    elif nilai>=85 and nilai<90:
        hasilnilai = "Grade A-"
        print(f"Your score is {nilai} and your grade is {hasilnilai}")
    elif nilai>=80 and nilai<85:
        hasilnilai = "Grade B"
        print(f"Your score is {nilai} and your grade is {hasilnilai}")
    elif nilai>=75 and nilai<80:
        hasilnilai = "Grade B-"
        print(f"Your score is {nilai} and your grade is {hasilnilai}")
    elif nilai>=70 and nilai<75:
        hasilnilai = "Grade C"
        print(f"Your score is {nilai} and your grade is {hasilnilai}")
    elif nilai>=65 and nilai<70:
        hasilnilai = "Grade D"
        print(f"Your score is {nilai} and your grade is {hasilnilai}")
    elif nilai<65 and nilai>=40:
        hasilnilai = "Perlu remedial"
        print(f"Your score is {nilai} and your grade is {hasilnilai}")
    else:
        hasilnilai = "Tidak lulus"
        print(f"Your score is {nilai} and your grade is {hasilnilai}")
except:
    print("Only accept integer")