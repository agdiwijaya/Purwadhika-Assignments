# ##### Tugas 

# - Email Verification / Validation
# Buatlah Suatu Return Function untuk Verifikasi/Validasi Email 

# Input :
# Masukkan Email : 

# Output :
# Sesuai dg Kondisi 

# Kondisi Valid Jika :
# - Memiliki Format Nama User@Nama Hosting.ekstensi
# - Nama user hanya Boleh Huruf, Angka, underscore(_) dan dot(.)
# - Nama user hanya Boleh di awali dg Huruf atau Angka 
# - Nama Hosting hanya boleh Huruf atau Kombinasi Huruf dan Angka 
# - Nama Ekstensi Hanya boleh Huruf dan maksimal 5 Karakter
# - Simbol Karakter Khusus Tidak bisa diterima 
# - Jumlah @ hanya boleh 1 
# - .co.id , .co.my atau .co.sg ==> ini dianggap sebagai 2 ekstensi, jadi masing-masing harus mengikuti aturan ekstensi
# - Maksimal dot(.) untuk ekstensi 2

# Contoh Output :
# "Alamat Email yg anda Masukkan Valid"

# Jika Tidak Valid, Keluar Notif sesuai dg Alasannya :

# Email Tidak Valid, Alasan 
# Alasan :
# - Format Email Salah (Misal Tidak ada @, atau tidak ada .ekstensi)
# - Format Username yg anda masukkan salah 
# - Format Hosting yg anda masukkan Salah 
# - Format Ekstensi yg anda masukkan Salah 


# Contoh Email :
# Valid
# andre@gmail.com 
# joni_99@yahoo.com 
# andy.134@city.com 
# steve_roger.77@avengers01.space

# InValid
# andre345@gmail
# andre%$^@gmail.com 
# john@yah%%oo.com 
# tony_stark@stark.corporation
# Thor@@gmail.com 

def FilterAt(a):
    if email.count("@")!=1:
        return "You have to input one '@'" 
    else:
        return "True"
def FilterAwalan(b):
    if not email[0].isalnum():
        return "Email name only alpha numeric"
    else:
        return "True"

def FilterUsername(c):
    splitusername = c.split("@")
    username = splitusername[0]
    username_titik = username.split(".")
    username1 = ''.join(username_titik)
    username_underscore = username1.split("_")
    username2 = ''.join(username_underscore)
    if username2.isalnum():
        return "True"
    else:
        return "Allowed Punctuation only '.' (dot) and '_' (underscore)"

def FilterSpasi(d):
    if" " in email:
        return "Space is not allowed"
    else:
        return "True"

def FilterDomain(e):    
    try:
        domain = email.split("@")
        ekstensi = domain[1]
        ekstensisplit = ekstensi.split(".")
        if len(ekstensisplit) > 3:
            return "Maximum extension is 2"
        elif len(ekstensisplit) <=1:
            return "You have make an extension"
        else:
            if len(ekstensisplit) > 2:
                if not ekstensisplit[0].isalnum() or not ekstensisplit[1].isalnum() or not ekstensisplit[2].isalnum():
                    return "Domain name only alpha numeric"    
                elif ekstensisplit[0].isdigit() or ekstensisplit[1].isdigit():
                    return "Domain name format has to only alphabet or combination of alphabet dan number"
                elif len(ekstensisplit[1]) > 5 or len(ekstensisplit[2]) > 5:
                    return "Maximum extension name is 5 characters"
                else:
                    return "True"
            else:
                if not ekstensisplit[0].isalnum() or not ekstensisplit[1].isalnum():
                    return "Domain name only alpha numeric"
                elif ekstensisplit[0].isdigit() or ekstensisplit[1].isdigit():
                    return "Domain name format has to only alphabet or combination of alphabet dan number" 
                elif len(ekstensisplit[1]) > 5:
                    return "Maximum extension name is 5 characters"
                else: 
                    return "True"
    except:
        return "You have to input one '@'"

email = input('Input email: ')
print("")
FilterAt(email)
FilterAwalan(email)
FilterSpasi(email)
FilterDomain(email)
FilterUsername(email)

if (FilterAt(email) == "True" and FilterAwalan(email) == "True" and FilterSpasi(email) == "True" and FilterDomain(email) == "True" and FilterUsername(email) == "True"):
    print(f"Congratulations, You have created an email: '{email}'")
else:
    print("Sorry, Email format is not valid:")
    if FilterAt(email) != "True":
        print(FilterAt(email))
    elif FilterAwalan(email) != "True":
        print(FilterAwalan(email))
    elif FilterSpasi(email) != "True":
        print(FilterSpasi(email))
    elif FilterUsername(email) != "True":
        print(FilterUsername(email))
    else: 
        print(FilterDomain(email))