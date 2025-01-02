import random

errore = 0

password = ""

print("\nBenvenuto nel generatore di password!")      
caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
caratteri_lista = []

for i in range(len(caratteri)):
    caratteri_lista.append(caratteri[i])

eccezione = None

while True:
    eccezione = input("\nScrivi un carattere da escludere dalla password (lascia vuoto per saltare):\n\n")
    if eccezione == "":
        break
    else:
        if eccezione in caratteri_lista:
            caratteri_lista.remove(eccezione)
        else:
            print("\nIl carattere inserito è già stato escluso o non è presente.") 

while True:
    num_caratteri  = input("\nQuanti caratteri vuoi che abbia la password?\n")
    try:
        num_caratteri = int(num_caratteri)
        break
    except:
        print("\nC'è stato un errore, nella casella di testo vanno inseriti unicamente numeri.")  

for i in range(num_caratteri):
    password += random.choice(caratteri_lista)

print("\nEcco la tua password: ", password)