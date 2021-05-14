import requests

def pokemon():
    loop = True
    while loop == True:
        try:
            pokemon = input("Masukkan nama pokemon: ")
            url = f'https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}'
            out = requests.get(url)
            data = out.json()

            if pokemon.isalpha():
                print(f"Nama Pokemon : {data['name'].capitalize()}")
                print(f"HP : {data['stats'][0]['base_stat']}")
                print(f"Attack : {data['stats'][1]['base_stat']}")
                print(f"Defense : {data['stats'][2]['base_stat']}")
                print(f"Speed : {data['stats'][-1]['base_stat']}")
                types = []
                for i in data['types']:
                    types.append(i['type']['name'])
                if len(types)>1:
                    print(f"Type : {types[0].capitalize()}, {types[-1].capitalize()} ")
                else:
                    print(f"Type : {types[0].capitalize()}")
                print(f"Image : {data['sprites']['front_default']}")
                print("Ability Pokemon : ")
                for i in range(len(data['abilities'])):
                    print(f"{i+1}. {data['abilities'][i]['ability']['name'].capitalize()}")
                loop = False
            else:
                print("Hanya menerima alfabet")
        except:
            print("Nama pokemon tidak terdaftar")

pokemon()