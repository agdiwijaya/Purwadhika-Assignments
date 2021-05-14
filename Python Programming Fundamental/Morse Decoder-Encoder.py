morse = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--.."
}

print("***Use '/' for separator if you input morse code***")
Input = input("Input sentence/morse code: " )
inputnya_itu_kalimat = False

## Pengecekkan Input adalah Kalimat atau Kode Morse
for i in Input:
    if i != "." and i != "-" and i != " " and i != "/":
        inputnya_itu_kalimat = True
        break
else: ## Konversi Kode Morse ke Kalimat
    try:
        # morse2 = dict((y,x) for x,y in morse.items())
        morse2 = {}
        for i,j in morse.items():
            morse2[j] = i
        # kalimat = []
        for x in Input.split(" "):
            huruf = ""
            kode_kata = x.split("/")
            # if kode_kata[-1] == "":
            #     kode_kata.pop(-1) # Menghapus karakter "" akibat splitting
            for y in kode_kata:
                huruf = huruf + morse2[y]
            # kalimat.append(huruf)
        print(f"Your inputted morse code is '{Input}', and has been converted to :")
        print(huruf)
        # print(" ".join(kalimat).capitalize())
    except:
        print("Inputted morse code is not valid")

## Konversi Kalimat ke Kode Morse
if inputnya_itu_kalimat == True:
    for x in Input.split(" "): ## Mengecek kalimat hanya alfa + num + space
        if x.isalnum() != True:
            print("Not accept punctuation")
            break
    else:
        katakata = Input.lower().split() # List kata - kata
        morse_kalimat = []
        for kata in katakata:
            morse_kata = []
            for huruf in kata:
                morse_kata.append(morse[huruf]) 
            morse_kalimat.append("/".join(morse_kata))
        print(f"Your inputted sentence is '{Input}', and has been converted to :")
        print(" ".join(morse_kalimat))
print("="*100)