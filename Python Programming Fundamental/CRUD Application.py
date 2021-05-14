password = "joni123"
data = ["Jeruk", "Apel", "Pisang", "Jeruk"]

####Syntax Untuk Memasukan Password
for coba in range(1,7):
    login = input("Mohon Masukkan Password Anda Untuk Membuka Aplikasi :")
    if login == password:
        break
    elif coba == 6:
        print("Maaf, Anda terlalu banyak memasukkan password yang salah. Silahkan Coba 2 jam lagi")
        exit()
    else:
        sisa_coba = 6 - coba
        print(f"Password Anda Salah, Silahkan Coba Lagi, Sisa Percobaan Untuk Input Password Anda {sisa_coba}")

####Syntax Untuk Menu Utama
# menu_universal = ""
def PilihanMenu():
    status = "True"
    while status == "True":
        print("")
        print("Selamat Datang di Menu Mini Aplikasi Toko Subur")
        print("")
        print("1. Cetak Isi Daftar Barang")
        print("2. Menambah Data Barang")
        print("3. Mengubah Data Barang")
        print("4. Menghapus Data Barang")
        print("5. Keluar Aplikasi")
        print("")
        try:
            user_input = int(input("Masukkan Pilihan Menu yang Ingin Anda Akses :"))
            if user_input == 1:
                print("")
                print("Anda Memilih Pilihan Menu 1 (Cetak Isi Daftar Barang)")
                menu_1()
                mini_menu(user_input)
                status = "False"
            elif user_input == 2:
                print("")
                print("Anda Memilih Pilihan Menu 2 (Menambah Data Barang)")
                menu_2()
                mini_menu(user_input)
                status = "False"
            elif user_input == 3:
                print("")
                print("Anda Memilih Pilihan Menu 3 (Mengubah Data Barang)")
                menu_3()
                mini_menu(user_input)
                status = "False"
            elif user_input == 4:
                print("")
                print("Anda Memilih Pilihan Menu 4 (Menghapus Data Barang)")
                menu_4()
                mini_menu(user_input)
                status = "False"
            elif user_input == 5:
                print("")
                print("Anda Memilih Pilihan Menu 5 (Exit)")
                print("Terima Kasih")
                status = "False"
            else:
                print("")
                print("Anda Harus Memasukkan Angka yang Terdapat Dalam Menu")
        except:
            print("")
            print("Maaf, Anda Harus Memasukkan Angka Untuk Memilih Menux")
    return user_input


#### Syntax Untuk Menu 1
def menu_1():
    print("")
    print("Selamat Datang Di Menu 1 Menambah Isi Daftar Barang")
    if data == []:
        print("Maaf, Daftar Barang Masih Kosong")
    else:
        print("Terlampir data yang anda punya", data)
        print(" ")

def menu_2():
    print("")
    print("Selamat Datang Di Menu 2 Menambah Daftar Barang")
    loop2=True
    
    while loop2:
        user = str(input('Masukkan barang yang anda inginkan: ')).capitalize()

        user_replace=user.replace(' ','')
        
        if user_replace.isalpha():
            if user in data:
                useryn=input('Data sudah ada, apakah tetap akan disimpan? Y/N: ').capitalize()
                if useryn == 'Y':
                    print('Data tersimpan dan mengupdate data barang')
                    data.append(user)
                    loop2 = False
                elif useryn =='N':
                    print('Data tidak tersimpan')
                    loop2 = False
                else:
                    print('Mohon pilih Y / N')
            else:
                data.append(user)
                print('Data Tersimpan!')
                loop2 = False
        else:
            print('Format tidak benar, harus alphabet')

#Menu 3

def menu_3():
    print("")
    print("Selamat Datang Di Menu 3 Update Barang")
    status = "True"
    while status == "True":
        try:
            barang = str(input("Masukan nama barang yang ingin diganti: ")).capitalize()
            if barang in data:
                # indexbaranglama = data.index(barang)
                barangbaru = str(input("Masukan barang baru yang akan diinput : ")).capitalize()
                barangbaru_replace=barangbaru.replace(' ','')
                if barangbaru_replace.isalpha():
                    if barangbaru in data:
                        print("Error: Barang yang dimasukkan sudah ada di dalam list")
                    else: 
                        for x in data[:]:
                            if x == barang:
                                data.remove(barang)
                                data.append(barangbaru)
                                status = "False"
                                # data[indexbaranglama] = barangbaru
                        print(f"{barang} sudah diganti dengan {barangbaru} di dalam daftar barang")
                else:
                    print('Hanya boleh memasukkan alphabet')
                        
            else:
                print("Barang tidak ditemukan!!!")
        except:
            print("")
            print("Maaf, Anda Harus Memasukkan Huruf")
            print("")

####Syntax Untuk Menu 4
def menu_4():
    print("")
    print("Selamat Datang di Menu 4 Hapus Data")
    print("")
    status = "True"
    while status == "True":
        try:
            nama_buah_delete= str(input("Masukkan Nama Buah yang ingin anda hapus dari database:").capitalize())
            if nama_buah_delete in data:
                for i in data[:]:
                    if len(data) == 0:
                        print("Data kosong, tidak ada yang bisa dihapus")
                    elif i == nama_buah_delete:
                        data.remove(nama_buah_delete)
                print("")
                print(nama_buah_delete, "berhasil dihapus dari database")
                print("")
                status="False"
            else:
                print("")
                print("Nama buah yang anda masukkan", nama_buah_delete, "tidak ditemukan di database")
                print("")
        except:
            print("")
            print("Maaf, Anda Harus Memasukkan Huruf")
            print("")

#### Syntax Untuk Mini_Menu
def mini_menu(x):
    status = "True"
    while status == "True":
        print("")
        print("Silahkan Pilih Aktivitas Anda Berikutnya")
        print("1. Kembali Melakukan Menu ini")
        print("2. Kembali Ke Menu Utama")
        print("")
        try:
            user_input_mini_menu = int(input("Masukkan Pilihan Mini Menu yang Ingin Anda Akses :"))
            if user_input_mini_menu == 1:
                if x == 1:
                    menu_1()
                    mini_menu(1)
                    status = "False"
                elif x == 2:
                    menu_2()
                    mini_menu(2)
                    status = "False"
                elif x == 3:
                    menu_3()
                    mini_menu(3)
                    status = "False"
                elif x == 4:
                    menu_4()
                    mini_menu(4)
                    status = "False"
            elif user_input_mini_menu == 2:
                PilihanMenu()
                status = "False"
            else:
                print("")
                print("Anda Harus Memasukkan Angka yang Terdapat Dalam Menu")
        except:
            print("")
            print("Maaf, Anda Harus Memasukkan Angka Untuk Memilih Menu")




PilihanMenu()