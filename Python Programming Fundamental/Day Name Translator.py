# 1.
# Auto Translator Hari 

# Silakan buat 1 Dictionary untuk Inisiasi

# Hari = {"senin" : "monday",
# "selasa" : "tuesday",
# "rabu" : "wednesday",
# dst.... 
# }

# Input :
# Masukkan Nama Hari : 

# Output :
# - Jika yg dimasukkan hari dalam bahasa indonesia

# Hari yg anda pilih -nama hari - dalam bahasa inggris adalah -hari dalam bahasa inggris-

# - Jika yg dimasukkan dari dalam bahasa inggris

# The Day that you choose is -hari dalam bahasa inggris- in Bahasa is -hari bahasa indo-

# Ketentuan :
# - Tidak menerima integer, Float 
# - Jika hari tidak ada akan keluar notif 

daftarhari = {"senin" : "monday", "selasa" : "tuesday", "rabu" : "wednesday", "kamis" : "thursday", 
"jumat" : "friday", "sabtu" : "saturday" , "minggu" : "sunday"}


try:
    hari = input("Masukkan nama hari: ")
    hari1 = hari.lower()
    # if kalimat.isalnum():
    for i in hari1:
        key_list = list(daftarhari.keys())
        val_list = list(daftarhari.values())
        if not hari1.isalpha():
            print("Tidak menerima angka")
            break
        else:
            if hari1 in daftarhari:
                print(f"Hari yg anda pilih '{hari.capitalize()}' dalam bahasa inggris adalah '{daftarhari[hari1].capitalize()}' dalam bahasa inggris")
                break
            else:
                day = val_list.index(hari1)
                print(f"The Day that you choose is '{hari.capitalize()}' dalam bahasa inggris in Bahasa is '{key_list[day].capitalize()}'")
                break
    # else:
        # print("Hanya menerima string")
except:
    print("Nama hari yang dimasukkan salah")