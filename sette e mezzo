import random


vuoi_carta="si"
somma_punti=0
somma_punti_bot=0
umano_perde=False

semi=["denari","spade","bastoni","coppe"]
numero=["1","2","3","4","5","6","7","fante","cavallo","re"]
mazzo=[]
valore={
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "f":0.5,
    "c":0.5,
    "r":0.5
}


for i in semi:
    for j in numero:
        carta=j+" di "+i
        mazzo.append(carta)




while vuoi_carta=="si"or vuoi_carta=="sì":
    carta_selezionata = str(random.choice(mazzo))
    mazzo.remove(carta_selezionata)
    carta_selezionata.split()
    somma_punti += valore[carta_selezionata[0]]
    print("la carta è: ",carta_selezionata)
    if somma_punti<=7.5:
        print(f"I tuoi punti sono: {somma_punti}")
    else:
        print("hai superato 7 e mezzo, hai perso!")
        umano_perde=True
        break
    vuoi_carta=input("Vuoi un'altra carta? si/no\n").lower()

while somma_punti_bot<2.6:
    carta_selezionata_bot = str(random.choice(mazzo))
    mazzo.remove(carta_selezionata_bot)
    carta_selezionata_bot.split()
    somma_punti_bot += valore[carta_selezionata_bot[0]]
    if somma_punti_bot > 7.5 and somma_punti<=7.5:
        print("complimenti, hai vinto! Il bot ha esagerato")
        break
    print("il bot ha: ",somma_punti_bot)


    if somma_punti>somma_punti_bot and umano_perde==False:
            print(f"complimenti, hai vinto! il bot ha fatto {somma_punti_bot}")
    else:
            print(f"hai perso, il bot ha fatto {somma_punti_bot}")
