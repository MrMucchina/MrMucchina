import random
import tkinter as tk
import time

window = tk.Tk()
window.geometry("400x300")
window.title("Trivial")

allow_input = True
punteggio_totale = 0
radio_buttons = []
risposta = "1"


var = tk.StringVar()


def create_radio_buttons(options):
    global radio_buttons
    for radio in radio_buttons:
        radio.destroy()  # Remove old radio buttons
    radio_buttons.clear()

    for i, opzione in enumerate(options):
        radio = tk.Radiobutton(window, text=opzione, variable=var, value=str(i+1))
        radio.pack()
        radio_buttons.append(radio)


def block_input(duration):
    global allow_input
    allow_input = False  # Disable the button when input is blocked
    print("Tempo scaduto!")


def check_answer(domanda):
    global allow_input, risposta, punteggio_totale
    if allow_input:
        risposta = var.get()
        if risposta == domanda["risposta_corretta"]:
            print("Risposta corretta!")
            punteggio_totale += domanda["punti"]
        else:
            print("Risposta errata!")
        print(f"Risposta data: {risposta}")
    else:
        print("Risposta fuori tempo!")

    next_question()


def next_question():
    global domanda_index, allow_input
    if domanda_index < len(domande_selezionate):
        allow_input = True
        domanda = domande_selezionate[domanda_index]
        domanda_index += 1


        label_domanda.config(text=f"Domanda {domanda_index}: {domanda['domanda']}")
        label_punti.config(text=punteggio_totale)
        create_radio_buttons(domanda["opzioni"])


        if domanda["difficolta"] == "facili":
            tempo_massimo = 10000  # 10 seconds
        elif domanda["difficolta"] == "medie":
            tempo_massimo = 15000  # 15 seconds
        else:
            tempo_massimo = 20000  # 20 seconds

        window.after(tempo_massimo, block_input, tempo_massimo)
    else:
        print(f"Il tuo punteggio finale è: {punteggio_totale} punti.")
        if punteggio_totale < 30:
          livello = "Meh"
          print(f"Con {punteggio_totale} punti, il tuo livello di conoscenza è: Meh")
          print("Sei stato davvero al limite :'-( ... Non è stato il tuo giorno migliore!")
        elif 30 <= punteggio_totale < 60:
          livello = "Nice"
          print(f"Con {punteggio_totale} punti, il tuo livello di conoscenza è: Nice")
          print("Buon lavoro! Non sei un genio, ma hai delle buone conoscenze :-).")
        elif 60 <= punteggio_totale < 90:
          livello = "Great"
          print(f"Con {punteggio_totale} punti, il tuo livello di conoscenza è: Great")
          print("Ottimo! Sei davvero preparato, hai fatto un gran bel lavoro :-)) !")
        else:
          livello = "Boss"
          print(f"Con {punteggio_totale} punti, il tuo livello di conoscenza è: Boss")
          print("Incredibile! Sei un vero boss della conoscenza :-)) !")    
        time.sleep(10)
        window.quit()


domande_facili = [
    {
        "domanda": "Chi ha dipinto la 'Gioconda'?",
        "opzioni": ["1. Michelangelo", "2. Leonardo da Vinci", "3. Raffaello", "4. Caravaggio"],
        "risposta_corretta": "2".lower(),
        "difficolta": "facili",
        "punti": 10
    },
    {
        "domanda": "Qual è il pianeta più vicino al Sole?",
        "opzioni": ["1. Venere", "2. Mercurio", "3. Marte", "4. Giove"],
        "risposta_corretta": "2".lower(),
        "difficolta": "facili",
        "punti": 10
    },
    {
        "domanda": "Qual è la capitale della Francia?",
        "opzioni": ["1. Berlino", "2. Parigi", "3. Madrid", "4. Roma"],
        "risposta_corretta": "2".lower(),
        "difficolta": "facili",
        "punti": 10
    },
    {
        "domanda": "Chi ha scritto 'Pinocchio'?",
        "opzioni": ["1. Carlo Collodi", "2. Gianni Rodari", "3. Italo Calvino", "4. Aesop"],
        "risposta_corretta": "1".lower(),
        "difficolta": "facili",
        "punti": 10
    },
    {
        "domanda": "Qual è il fiume più lungo del mondo?",
        "opzioni": ["1. Nilo", "2. Amazzoni", "3. Yangtze", "4. Mississippi"],
        "risposta_corretta": "1".lower(),
        "difficolta": "facili",
        "punti": 10
    },
    {
        "domanda": "In quale continente si trova l'Egitto?",
        "opzioni": ["1. Europa", "2. Asia", "3. Africa", "4. America"],
        "risposta_corretta": "3".lower(),
        "difficolta": "facili",
        "punti": 10
    },
    {
        "domanda": "Qual è il colore del cielo in una giornata serena?",
        "opzioni": ["1. Blu", "2. Verde", "3. Rosso", "4. Giallo"],
        "risposta_corretta": "1".lower(),
        "difficolta": "facili",
        "punti": 10
    },
    {
        "domanda": "Chi è il fondatore della psicoanalisi?",
        "opzioni": ["1. Carl Jung", "2. Sigmund Freud", "3. Alfred Adler", "4. William James"],
        "risposta_corretta": "2".lower(),
        "difficolta": "facili",
        "punti": 10
    },
    {
        "domanda": "Qual è l'animale più veloce del mondo?",
        "opzioni": ["1. Cheetah", "2. Falco pellegrino", "3. Cavallo", "4. Leone"],
        "risposta_corretta": "1".lower(),
        "difficolta": "facili",
        "punti": 10
    },
    {
        "domanda": "Qual è il simbolo chimico dell'acqua?",
        "opzioni": ["1. O2", "2. H2O", "3. CO2", "4. H2"],
        "risposta_corretta": "2".lower(),
        "difficolta": "facili",
        "punti": 10
    },
]

domande_medie = [
    {
        "domanda": "Qual è la capitale dell'Italia?",
        "opzioni": ["1. Roma", "2. Milano", "3. Napoli", "4. Torino"],
        "risposta_corretta": "1".lower(),
        "difficolta": "medie",
        "punti": 20
    },
    {
        "domanda": "Chi ha scritto '1984'?",
        "opzioni": ["1. Aldous Huxley", "2. George Orwell", "3. Ray Bradbury", "4. Isaac Asimov"],
        "risposta_corretta": "2".lower(),
        "difficolta": "medie",
        "punti": 20
    },
    {
        "domanda": "In quale anno è stata fondata Roma?",
        "opzioni": ["1. 753 a.C.", "2. 476 d.C.", "3. 1000 d.C.", "4. 100 a.C."],
        "risposta_corretta": "1".lower(),
        "difficolta": "medie",
        "punti": 20
    },
    {
        "domanda": "Qual è il nome del primo uomo sulla Luna?",
        "opzioni": ["1. Buzz Aldrin", "2. Yuri Gagarin", "3. Neil Armstrong", "4. John Glenn"],
        "risposta_corretta": "3".lower(),
        "difficolta": "medie",
        "punti": 20
    },
    {
        "domanda": "Qual è l'elemento chimico con simbolo 'Fe'?",
        "opzioni": ["1. Argento", "2. Rame", "3. Ferro", "4. Mercurio"],
        "risposta_corretta": "3".lower(),
        "difficolta": "medie",
        "punti": 20
    },
]

domande_difficili = [
    {
        "domanda": "In quale anno è stata scoperta l'America?",
        "opzioni": ["1. 1492", "2. 1500", "3. 1480", "4. 1498"],
        "risposta_corretta": "1".lower(),
        "difficolta": "difficili",
        "punti": 30
    },
    {
        "domanda": "Chi ha formulato la teoria della relatività?",
        "opzioni": ["1. Isaac Newton", "2. Albert Einstein", "3. Nikola Tesla", "4. Stephen Hawking"],
        "risposta_corretta": "2".lower(),
        "difficolta": "difficili",
        "punti": 30
    },
    {
        "domanda": "Quale organo del corpo umano produce insulina?",
        "opzioni": ["1. Fegato", "2. Cuore", "3. Polmoni", "4. Pancreas"],
        "risposta_corretta": "4".lower(),
        "difficolta": "difficili",
        "punti": 30
    },
    {
        "domanda": "Qual è la capitale del Giappone?",
        "opzioni": ["1. Seul", "2. Tokyo", "3. Pechino", "4. Bangkok"],
        "risposta_corretta": "2".lower(),
        "difficolta": "difficili",
        "punti": 30
    },
    {
        "domanda": "Chi ha scritto 'Il nome della rosa'?",
        "opzioni": ["1. Umberto Eco", "2. Gabriel Garcia Marquez", "3. Italo Calvino", "4. Mario Vargas Llosa"],
        "risposta_corretta": "1".lower(),
        "difficolta": "difficili",
        "punti": 30
    },
]

domande_boss = [
    {
        "domanda": "Qual è la distanza tra la Terra e il Sole?",
        "opzioni": ["1. 149.6 milioni di km", "2. 93 milioni di miglia", "3. 1 milione di km", "4. 500 milioni di km"],
        "risposta_corretta": "1".lower(),
        "difficolta": "boss",
        "punti": 40
    },
    {
        "domanda": "Chi ha teorizzato l'evoluzione delle specie?",
        "opzioni": ["1. Charles Darwin", "2. Gregor Mendel", "3. Albert Einstein", "4. Louis Pasteur"],
        "risposta_corretta": "1".lower(),
        "difficolta": "boss",
        "punti": 40
    },
    {
        "domanda": "In quale anno è iniziata la Prima Guerra Mondiale?",
        "opzioni": ["1. 1914", "2. 1918", "3. 1939", "4. 1945"],
        "risposta_corretta": "1".lower(),
        "difficolta": "boss",
        "punti": 40
    },
    {
        "domanda": "Qual è la formula chimica del metano?",
        "opzioni": ["1. CO2", "2. CH4", "3. H2O", "4. C2H6"],
        "risposta_corretta": "2".lower(),
        "difficolta": "boss",
        "punti": 40
    },
    {
        "domanda": "Chi ha scoperto la penicillina?",
        "opzioni": ["1. Louis Pasteur", "2. Alexander Fleming", "3. Marie Curie", "4. Thomas Edison"],
        "risposta_corretta": "2".lower(),
        "difficolta": "boss",
        "punti": 40
    },
]


domande_selezionate = random.sample(domande_facili, 2) + \
                      random.sample(domande_medie, 1) + \
                      random.sample(domande_difficili, 1) + \
                      random.sample(domande_boss, 1)


label_domanda = tk.Label(window, text="Domanda:", font=("Arial", 12))
label_domanda.pack()



button = tk.Button(window, text="Invia", command=lambda: check_answer(domande_selezionate[domanda_index-1]))
button.pack()

label_punti = tk.Label(window, text=punteggio_totale, font=("Arial", 12))
label_punti.pack()

domanda_index = 0
next_question()


window.mainloop()
