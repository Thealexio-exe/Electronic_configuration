import json

with open("lingue/scelta.json", "r", encoding="utf-8") as file:
    scelta_lingua = json.load(file)["lingua"]

with open("lingue/lingue.json", "r", encoding="utf-8") as files:
    testo = json.load(files)

def carica_scelta(lingua: str):
    global scelta_lingua

    # 3. Sovrascrive il file JSON con i nuovi dati aggiornati
    with open("lingue/scelta.json", "w", encoding="utf-8") as file:
        json.dump({"lingua": lingua}, file, ensure_ascii=False, indent=4)
        scelta_lingua = lingua