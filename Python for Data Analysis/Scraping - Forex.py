from bs4 import BeautifulSoup
import requests

url = 'listbank.html'
out = BeautifulSoup(open(url, 'r'), "html.parser")

data = []
for i in out.find_all('td'):
    data.append(i.text)

listbank = data[18:-2:3]
listmatauang = data[20:57:3]

listmatauangsplit = [word for line in listmatauang for word in line.split(",")]
bca = {}
bca[listbank[0]] = listmatauangsplit[0:16]
bi = {}
bi[listbank[1]] = listmatauangsplit[16:41]
bni = {}
bni[listbank[2]] = listmatauangsplit[41:54]
bukopin = {}
bukopin[listbank[3]] = listmatauangsplit[54:61]
commonwealth = {}
commonwealth[listbank[4]] = listmatauangsplit[61:70]
mandiri = {}
mandiri[listbank[5]] = listmatauangsplit[70:85]
mayapada = {}
mayapada[listbank[6]] = listmatauangsplit[85:92]
mega = {}
mega[listbank[7]] = listmatauangsplit[92:102]
muamalat = {}
muamalat[listbank[8]] = listmatauangsplit[102:107]
panin = {}
panin[listbank[9]] = listmatauangsplit[107:118]
permata = {}
permata[listbank[10]] = listmatauangsplit[118:132]
sinarmas = {}
sinarmas[listbank[11]] = listmatauangsplit[132:140]
woorisaudara = {}
woorisaudara[listbank[12]] = listmatauangsplit[140:146]

matauang = {**bca, **bi, **bni, **bukopin, **commonwealth, **mandiri, 
**mayapada, **mega, **muamalat, **panin, **permata, **sinarmas, **woorisaudara}


token = 'bZEwHdhltr5MhdwR5OGZ3PFxy2tks4n9tYI16RVB'

def menu(): 
    tespilihan = True
    while tespilihan:
        print("\nMenu:\n1. IDR to Mata Uang Asing \n2. Mata Uang asing to IDR \n3. Quit")
        pilihan = (input("Masukkan pilihan [1/2/3]: "))

        if pilihan == '1':
            return tukarIDR()
        elif pilihan == '2':
            return tukarasing()
        elif pilihan =='3':
            return 'Anda keluar program'
        else:
            print("Pilihan yang dimasukkan salah")
    

def tukarIDR():
    tesinputbank = True
    while tesinputbank == True:
        print('\nDaftar nama bank yang tersedia:')
        print(listbank)
        inputbank = input("\nMasukkan nama bank Anda: ")
        if inputbank.upper() in listbank:
            print(f"\nMata uang yang tersedia di {inputbank.upper()} adalah:")
            print(matauang[inputbank.upper()])
           

            teskursuang = True
            while teskursuang == True:
                print("\n-----IDR to Mata Uang Asing-----")
                kurs = input("Masukkan mata uang: ")
                if kurs.upper() not in matauang[inputbank.upper()]:
                    print('\nMata uang yang Anda masukkan tidak tersedia.')
                else:   
        
                    tesinputuang = True                       
                    while tesinputuang == True:
                        try:
                            uang = int(input("Total uang yang akan ditukar: IDR "))
                            if uang > 0:
                                url = f"https://api.kurs.web.id/api/v1?token={token}&bank={inputbank.lower()}&matauang={kurs.lower()}"
                                data = requests.get(url)
                                output = data.json()
                                konversi = output['jual']
                                print(f'Jumlah uang anda sebesar IDR {uang} setara dengan {kurs.upper()} {uang/konversi}')
                        

                                loop = True
                                while loop:
                                    user = input('Apakah anda masih ingin memakai menu ini? (Y/N): ').upper()
                                    if user =='N':
                                        return menu()
                                    elif user =='Y':
                                        return tukarIDR()
                                    else:
                                        print('Pilihan salah')

                            else:
                                print("Uang yang Anda masukkan salah")
                        except:
                            print('\nJumlah uang yang Anda masukkan salah.')
                            teskursuang = True


            
        else:
            print("Bank yang Anda masukkan tidak terdaftar")
            tesinputbank = True
    

def tukarasing():
    tesinputbank = True
    while tesinputbank == True:
        print('\nDaftar nama bank yang tersedia:')
        print(listbank)
        inputbank = input("\nMasukkan nama bank Anda: ")
        if inputbank.upper() in listbank :
            print(f"\nMata uang yang tersedia di {inputbank.upper()} adalah:")
            print(matauang[inputbank.upper()])
           
    
            teskursuang = True
            while teskursuang == True:
                print("\n-----Mata Uang Asing to IDR-----")
                kurs = input("Masukkan mata uang: ")
                if kurs.upper() not in matauang[inputbank.upper()]:
                    print('\nMata uang yang Anda masukkan tidak tersedia.')
                else:   
                    
                    tesinputuang = True                       
                    while tesinputuang == True:
                        
                        try:
                            uang = int(input(f"Total uang yang akan ditukar: {kurs.upper()} "))
                            if uang > 0:
                            
                                url = f"https://api.kurs.web.id/api/v1?token={token}&bank={inputbank.lower()}&matauang={kurs.lower()}"
                                data = requests.get(url)
                                output = data.json()
                                konversi = output['beli']
                                print(f'Jumlah uang anda sebesar {kurs.upper()} {uang} setara dengan IDR {uang * konversi}')

                                loop = True
                                while loop:
                                    user = input('Apakah anda masih ingin memakai menu ini? (Y/N): ').upper()
                                    if user =='N':
                                        return menu()
                                    elif user =='Y':
                                        return tukarasing()
                                    else:
                                        print('Pilihan salah')

                            else:
                                print("Uang yang Anda masukkan salah")
                        except:
                            print('\nJumlah uang yang Anda masukkan salah.')
                            teskursuang = True
        else:
            print("Bank yang Anda masukkan tidak terdaftar")
            tesinputbank = True

print(menu())