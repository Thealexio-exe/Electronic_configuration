import tkinter as tk

# Inizializazione di TK
root = tk.Tk()
root.geometry("800x400")
root.resizable(False, False)
root.title("Configurazione Elettronica")

# Variabili Globali
tenativi = 0
semplifica_bool = False
orbitali = ["1s",
            "2s",
            "2p",
            "3s",
            "3p",
            "4s",
            "3d",
            "4p",
            "5s",
            "4d",
            "5p",
            "6s",
            "4f",
            "5d",
            "6p",
            "7s",
            "5f",
            "6d",
            "7p"]

# Logiaca Orbitali
def logica(orbitale = [],  orbitale_2 = 0):
    if orbitale[len(orbitale)-1] == "s":
        orbitale_2 = 2
    elif orbitale[len(orbitale)-1]== "p":
        orbitale_2 = 6
    elif orbitale[len(orbitale)-1] == "d":
        orbitale_2 = 10
    elif orbitale[len(orbitale)-1] == "f":
        orbitale_2 = 14

    return orbitale_2

# Logica dell configurazione eltronica per il def aggiorna()
def calcola_configurazione(Z):
    elettroni = Z
    risultat = ""

    # Eccezione che non si possono calcolare con la logica del for
    if Z == 24:
        return risultato.config(text="1s2 2s2 2p6 3s2 3p6 4s1 3d5")
    elif Z == 29:
        return risultato.config(text="1s2 2s2 2p6 3s2 3p6 4s1 3d10")
    elif Z == 42:
        return risultato.config(text="1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d5")
    elif Z == 47:
        return risultato.config(text="1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d10")
    elif Z == 79:
        return risultato.config(text="1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1 4f14 5d10")

    for i in orbitali:
        if elettroni <= 0:
            break

        max_e = logica(i)
        elettroni_usati = min(elettroni, max_e)

        risultat += f"{i}{elettroni_usati} "
        elettroni -= elettroni_usati

    return risultat.strip()

# Logica configurazione eltronica semplificata
def configurazione_semp(Z):
    eletronis = Z

    def config_base(text = "", S = 0):

        nonlocal eletronis
        risultato = f"{text} "

        for i in orbitali[S:]:
            if eletronis <= 0:
                break
        
            max_e = logica(i)
            eletroni_usati = min(eletronis, max_e)

            risultato += f"{i}{eletroni_usati} "
            eletronis -= eletroni_usati
            
        return risultato.strip()
        
    if Z == 24:
        return risultato.config(text="[Ar] 4s1 3d5")
    elif Z == 29:
        return risultato.config(text="[Ar] 4s1 3d10")
    elif Z == 42:
        return risultato.config(text="[Kr] 5s1 4d5")
    elif Z == 47:
        return risultato.config(text="[Kr] 5s1 4d10")
    elif Z == 79:
        return risultato.config(text="[Xe] 6s1 4f14 5d10")
    else:
        if 1 <= Z <= 2:
            return config_base()
        elif 3 <= Z <= 10:
            eletronis -= 2
            return config_base("[He]", 1)
        elif 11 <= Z <= 18:
            eletronis -= 10
            return config_base("[Ne]", 3)
        elif 19 <= Z <= 36:
            eletronis -= 18
            return config_base("[Ar]", 5)
        elif 37 <= Z <= 54:
            eletronis -= 36
            return config_base("[Kr]", 8)
        elif 55 <= Z <= 86:
            eletronis -= 54
            return config_base("[Xe]", 11)
        elif 86 <= Z:
            eletronis -= 86
            return config_base("[Rn]", 15)
    return
    
# Logica tasto Help
def risposta():
    global tenativi, bottone
    tenativi += 1

    if tenativi == 1:
        risultato.config(text="Questo programma è un convertitore automatico per la configurazione elettronica, se hai bisogno di nuove informazioni cliccami pure, ma non esagerare")
    elif tenativi == 2:
        risultato.config(text="Se non sai cos'è la configurazione elettronica, in poche parole è la posizione di ogni elettrone, ti consiglio di approfondire su una fonte affidabile")
    elif tenativi == 3:
        risultato.config(text="Puoi inserire un numero atomico (Z) compreso tra 1 e 118.")
    elif tenativi == 4:
        risultato.config(text="Non credo che possa servirti per altro, puoi lasciarmi in pace, voglio far riposare il mio codice")
    elif tenativi == 5:
        risultato.config(text="Sul serio, basta cliccare… sto iniziando a soffrire")
    elif tenativi == 6:
        risultato.config(text="Basta non ne posso più")
    else:
        risultato.config(text="Va bene, mi autodistruggo. Addio")
        bottone.destroy()
    
    return tenativi

# Aggiorna in automatico
def aggiorna(così_funziona=None):
    valore = inserisci_testo.get()

    if valore == "":
        risultato.config(text="")
        return

    try:  
        Z = int(valore)

        if Z < 1:
            risultato.config(text="Z deve essere almeno 1")
            return
        elif Z > 118:
            risultato.config(text="Pultroppo Z è maggiore di 118, riproviamo")
            return 
        
        if semplifica_bool is False:
            configurazione = calcola_configurazione(Z)
            risultato.config(text=configurazione)
        else:
            configuraziones = configurazione_semp(Z)
            risultato.config(text=configuraziones)
            
    except ValueError: # Gabacci è stato qui
        risultato.config(text="il testo non è ammesso")

# ON or OF per la semplificazione 
def controllo_semp():
    global semplifica_bool, Testo_semplifica

    if semplifica_bool is False:
        semplifica_bool = True
        Testo_semplifica.config(text="Non semplificata", font=("Georgia", 8))
    else:
        semplifica_bool = False
        Testo_semplifica.config(text="Semplificata", font=("Georgia", 11))

    return semplifica_bool

# Griglia 1
frame = tk.Frame(root)
frame.pack(pady=40)

# Testo iniziale
titolo = tk.Label(
    frame,
    text="Inserisci Z",
    font=("Georgia", 24)
)
titolo.grid(row=0,column=0, columnspan=3, pady=20)

# Bottone per semplificare
Testo_semplifica = tk.Button(
    frame, text= "Semplificata",
    font=("Georgia", 10), 
    bg="white", fg="blue",
    cursor="hand2", 
    command=lambda: controllo_semp()
)
Testo_semplifica.grid(row=1, column=0, padx=10)

# Entry inserire i dati
inserisci_testo = tk.Entry(
    frame,
    font=("Consolas", 18),
    justify="center",
    cursor="hand2"
)
inserisci_testo.grid(row=1, column=1, padx=10)
inserisci_testo.bind("<KeyRelease>", aggiorna)

# Bottone Help
bottone = tk.Button(frame, text="Help",
            font=("Georgia", 10), 
            bg="white", fg="red",
            cursor="hand2", 
            command=lambda: risposta())
bottone.grid(row=1, column=2, padx=10)

# Testo risultato
risultato = tk.Label(
    root,
    font=("Consolas", 16),
    wraplength=700,
    justify="center"
)
risultato.pack(pady=30)

root.mainloop()
