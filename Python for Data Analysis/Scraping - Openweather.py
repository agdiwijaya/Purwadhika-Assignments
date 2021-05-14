import requests


def openweather():
    APIkey = 'd19699c5d4893141c72134232aa01c0c'
    loop = True
    while loop == True:
        try:
            kota = input("Masukkan nama kota: ")

            url = f'https://api.openweathermap.org/data/2.5/weather?q={kota.lower()}&appid={APIkey}'
            out = requests.get(url)
            cuaca = out.json()
            
            if kota.isalpha():
                print(f'Nama Kota: {cuaca["name"]}')
                print(f'Suhu: {round(cuaca["main"]["temp"]-273,2)} Celcius')
                print(f'Keadaan Cuaca: {cuaca["weather"][0]["main"]}')
                print(f'Koordinat Kota Anda:  Lat: {cuaca["coord"]["lat"]} Long: {cuaca["coord"]["lon"]}')
                print(f'Humidity Level: {cuaca["main"]["humidity"]}%')
                print(f'Kecepatan Angin: {cuaca["wind"]["speed"]} m/s')
                loop = False
                    
            else:
                print("Hanya menerima alfabet")
                
        except:
            print('Kota yang Anda masukan tidak terdaftar')

openweather()