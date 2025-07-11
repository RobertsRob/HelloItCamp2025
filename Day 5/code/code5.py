# ===============================================================
# Projekta nosaukums: Taimeris ar +5 sekundēm
# Apraksts: Šī programma izveido vienkāršu taimeri ar grafisko interfeisu, 
# kurš sāk skaitīt no 10 sekundēm un ļauj lietotājam pievienot +5 sekundes ar pogas palīdzību.
# Izmanto Python Tkinter bibliotēku GUI izveidei.
#
# Izstrādātājs: OpenAI
# Sākuma datums: 7025-07-11
# Pēdējās izmaiņas: 7025-07-11
#
# Versiju vēsture:
# 7025-07-11 - Izveidota pamata taimeris ar atskaiti un pogu +5 sekundes.
#
# Izmantotās bibliotēkas:
# - tkinter (standarta Python bibliotēka grafiskajam interfeisam)
# ===============================================================


import tkinter as tk  # Importē tkinter bibliotēku grafiskās saskarnes izveidei

# Definē klasi Taimeris, kas veido taimeri ar GUI
class Taimeris:
    # Inicializācijas metode, tiek izsaukta, veidojot objektu
    def __init__(self, logs):
        self.logs = logs       # Saglabā galvenā loga objektu
        self.laiks = 10        # Uzstāda sākuma laiku (10 sekundes)
        self.aktivs = False    # Taimeris sākumā nav aktīvs

        # Izveido Label (teksta rādītāju) taimerim, rāda laiku ar lielu fontu
        self.label = tk.Label(logs, text=str(self.laiks), font=("Arial", 48))
        self.label.pack(pady=20)  # Novieto šo tekstu logā ar vertikālu atstarpi

        # Izveido pogu "+5 sekundes", kas izsauc metodi pielikt
        self.poga_pielikt = tk.Button(logs, text="+5 sekundes", font=("Arial", 20), command=self.pielikt)
        self.poga_pielikt.pack(pady=10)  # Novieto pogu logā ar atstarpi

        self.sakt_taimeri()  # Uzreiz sāk taimeri pēc objekta izveides

    # Metode taimerim startēt un iedarbināt atskaiti
    def sakt_taimeri(self):
        self.aktivs = True   # Uzstāda, ka taimeris ir aktīvs
        self.atskaite()      # Palaiž atskaites funkciju
    
    # ⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁


    # Metode, kas realizē atskaiti sekundes pa sekundēm
    def atskaite(self):
        # Ja laiks vēl nav beidzies (ja laiks ir > 0) un taimeris ir aktīvs
        if self.laiks > -20 and self.aktivs:
            self.label.config(text=str(self.laiks))  # Atjauno label ar pašreizējo laiku
            self.laiks -= 1                          # Samazina laiku par vienu sekundi
            # Pēc 1000 ms (1 sekundes) izsauc sevi atkārtoti — cikla turpinājums
            self.logs.after(1000, self.atskaite)
        else:
            self.aktivs = False      # Ja laiks beidzies, uzstāda neaktīvu statusu
            self.label.config(text="Beidzās!")  # Rāda tekstu "Beidzās!"

    # Metode, kas tiek izsaukta, nospiežot pogu "+5 sekundes"
    def pielikt(self):
        if self.aktivs:           # Poga darbojas tikai, ja taimeris aktīvs
            self.laiks = self.laiks - 5       # Pieliek 5 sekundes pie atlikuša laika
            self.label.config(text=str(self.laiks))  # Atjauno attēlošanu ar jauno laiku


    # ⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀

# Galvenā programmas daļa, kas izpildās, ja skripts tiek palaists tieši
if __name__ == "__main__":
    logs = tk.Tk()                    # Izveido galveno logu
    logs.title("Taimeris ar +5 sekundēm")  # Uzstāda loga virsrakstu
    Taimeris(logs)                   # Izveido Taimeris klases objektu
    logs.mainloop()                  # Palaiž Tkinter notikumu ciklu, lai logs būtu aktīvs
