import tkinter as tk
from PIL import Image, ImageTk
import lingue

# Inizializazione di TK
root = tk.Tk()
root.geometry("800x400")
root.resizable(False, False)
root.title(lingue.testo[lingue.scelta_lingua]["titolo_p"])

# processo per diminuire la dimenzione dell'immagine e poi si converte per tk
img = Image.open("img/impostazzioni.png").resize((35, 35))
img_it = Image.open("img/italia.png").resize((20, 15))
img_en = Image.open("img/ing.png").resize((20, 15))

TK_immagine = ImageTk.PhotoImage(img)
TK_img_it = ImageTk.PhotoImage(img_it)
TK_img_en = ImageTk.PhotoImage(img_en)

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

# serve a me per non ammzarmi di lavoro
def T(chiave: str):
    return lingue.testo[lingue.scelta_lingua][chiave]

# serve a ricaricare tutti i testi dopo il cambio di lingua, è un po lungo ma essenziale
def refresh():
    global semplifica_bool, tenativi

    if semplifica_bool:
        Testo_semplifica.config(text=T("semplificata"))
    else:
        Testo_semplifica.config(text=T("non_semplificata"))

    root.title(T("titolo_p"))

    titolo.config(text=T("titolo"))
    bottone.config(text=T("Help_bott"))

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

    risultato.config(text=T("Help")[tenativi])
    if tenativi >= 8:
        bottone.destroy()

    
    return tenativi

# Aggiorna in automatico
def aggiorna(event=None):
    valore = inserisci_testo.get()

    if valore == "":
        risultato.config(text="")
        return

    try:  
        Z = int(valore)

        if Z < 1:
            risultato.config(text=T("errore_z"))
            return
        elif Z > 118:
            risultato.config(text=T("errore_z2"))
            return 
        
        if semplifica_bool is False:
            configurazione = calcola_configurazione(Z)
            risultato.config(text=configurazione)
        else:
            configuraziones = configurazione_semp(Z)
            risultato.config(text=configuraziones)
            
    except ValueError: # Gabacci è stato qui
        risultato.config(text=T("errore_test"))

# ON or OF per la semplificazione 
def controllo_semp():
    global semplifica_bool, Testo_semplifica

    if not semplifica_bool:
        semplifica_bool = True
        Testo_semplifica.config(font=("Georgia", 8))
    else:
        semplifica_bool = False
        Testo_semplifica.config(font=("Georgia", 11))
    refresh()

    return semplifica_bool

# funzione per impostazioni
def impostazioni():
    global wiget_tot, frame, TK_img_it, TK_img_en

    def torna():
        nonlocal it, en

        it.grid_remove()
        en.grid_remove()

        for w in wiget_tot:
            w.grid()

    def lingua_it():
        lingue.carica_scelta("it")

        refresh()
        torna()
        

    def lingua_en():
        lingue.carica_scelta("en")

        refresh()
        torna()
        

    # rende invisibili tutti i tasti e crea due bottoni
    for w in wiget_tot:
        w.grid_remove()
    

    it = tk.Button(
        frame,
        image=TK_img_it,
        text="Italiano",
        compound="left",
        font=("Georgia", 15),
        command=lambda: lingua_it()
    )
    it.grid(row=2,column=2, pady=130)

    en = tk.Button(
        frame,
        image=TK_img_en,
        text="English",
        compound="left",
        font=("Georgia", 15),
        command=lambda: lingua_en()
    )
    en.grid(row=2, column=1, pady=130, padx=40)

      
# Griglia 1
frame = tk.Frame(root)
frame.pack(pady=40)


# Testo iniziale
titolo = tk.Label(
    frame,
    text=T("titolo"),
    font=("Georgia", 24)
)
titolo.grid(row=0,column=0, columnspan=3, pady=20)

# Bottone per semplificare
Testo_semplifica = tk.Button(
    frame, text= T("semplificata"),
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


# Bottone Help
bottone = tk.Button(frame, 
            text= T("Help_bott"),
            font=("Georgia", 10), 
            bg="white", fg="red",
            cursor="hand2", 
            command=lambda: risposta())
bottone.grid(row=1, column=2, padx=10)

# bottone per inpostazioni
bottone_impostazioni = tk.Button(
    frame,
    image=TK_immagine,
    cursor="hand2",
    command=lambda: impostazioni()
)
bottone_impostazioni.grid(row=1,column=3,padx=10)

# Testo risultato
risultato = tk.Label(
    root,
    font=("Consolas", 16),
    wraplength=700,
    justify="center"
)
risultato.pack(pady=30)

wiget_tot = [titolo, Testo_semplifica, bottone, bottone_impostazioni, inserisci_testo]

inserisci_testo.bind("<KeyRelease>", aggiorna)

root.mainloop()
