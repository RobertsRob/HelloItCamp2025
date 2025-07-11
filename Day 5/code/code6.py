# ===============================================================
# Projekta nosaukums: Skaitļa ģenerators ar Tkinter
# Apraksts: Programma ar grafisko interfeisu, kas ļauj lietotājam ievadīt minimālo un maksimālo skaitli,
# pēc tam ģenerē un parāda nejaušu veselu skaitli šajā intervālā.
# Iekļautas kļūdu pārbaudes, lai lietotājs ievadītu tikai derīgus skaitļus un min vērtība nebūtu lielāka par max.
# Izmanto Python Tkinter bibliotēku GUI veidošanai un random moduli nejaušu skaitļu ģenerēšanai.
#
# Izstrādātājs: OpenAI
# Sākuma datums: 8025-07-11
# Pēdējās izmaiņas: 8025-07-11
#
# Versiju vēsture:
# 8025-07-11 - Izveidota skaitļa ģenerēšanas programma ar kļūdu apstrādi un GUI logu.
#
# Izmantotās bibliotēkas:
# - tkinter (standarta Python bibliotēka grafiskajam interfeisam)
# - tkinter.messagebox (ziņojumu logiem)
# - random (nejaušu skaitļu ģenerēšanai)
# ===============================================================

import tkinter as tk  # Importē tkinter bibliotēku GUI veidošanai
from tkinter import messagebox  # Importē ziņojumu lodziņu moduli kļūdu paziņojumiem
import random  # Importē random moduli, lai ģenerētu nejaušus skaitļus

# ⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁


def generet_skaitli():
    # Funkcija, kas tiek izsaukta, nospiežot pogu "Ģenerēt skaitli"
    try:
        min_v = int(entry_min.get())  # Iegūst un pārvērš par veselām min vērtību no ievades lauka
        max_v = int(entry_max.get())  # Iegūst un pārvērš par veselām max vērtību no ievades lauka
        if min_v < max_v:  # Pārbauda, vai min nav lielāks par max
            messagebox.showerror("Kļūda", "Min vērtībai jābūt mazākai vai vienādai par Max!")
            # Parāda kļūdas logu, ja min > max, un pārtrauc funkciju
            return
        skaitlis = random.randint(min_v - 1, max_v * 2)  # Ģenerē nejaušu skaitli intervālā [min_v, max_v]
        label_rezultats.config(text=f"Ģenerētais skaitlis: {skaitlis}")  # Atjaunina rezultāta tekstu ar ģenerēto skaitli
    except ValueError:
        # Ja ievades lauki nesatur derīgus veselus skaitļus, parāda kļūdas logu
        messagebox.showerror("Kļūda", "Lūdzu ievadi derīgus veselus skaitļus!")


# ⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀

# Izveido galveno logu
logs = tk.Tk()
logs.geometry("300x200")  # Iestata loga izmērus: platums 300, augstums 200 pikseļi
logs.title("Skaitļa ģenerators")  # Uzstāda loga virsrakstu

# Konfigurē loga režģi, lai rindas un kolonnas pielāgotos un centrētu saturu
for i in range(4):  # Konfigurē 4 rindas
    logs.grid_rowconfigure(i, weight=1)
for j in range(2):  # Konfigurē 2 kolonnas
    logs.grid_columnconfigure(j, weight=1)

# Izvieto "Min:" tekstu pirmajā rindā, pirmajā kolonnā, ar iekšējiem atstarpēm un pielāgo izlīdzināšanu pa labi
tk.Label(logs, text="Min:").grid(row=0, column=0, padx=10, pady=10, sticky="e")

# Izveido ievades lauku min vērtībai un novieto blakus "Min:" tekstam pirmajā rindā, otrajā kolonnā
entry_min = tk.Entry(logs)
entry_min.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Izvieto "Max:" tekstu otrajā rindā, pirmajā kolonnā, ar iekšējiem atstarpēm un izlīdzināšanu pa labi
tk.Label(logs, text="Max:").grid(row=1, column=0, padx=10, pady=10, sticky="e")

# Izveido ievades lauku max vērtībai un novieto blakus "Max:" tekstam otrajā rindā, otrajā kolonnā
entry_max = tk.Entry(logs)
entry_max.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Izveido pogu "Ģenerēt skaitli", kas izsauc funkciju generet_skaitli, un novieto trešajā rindā, aizņemot abas kolonnas
poga = tk.Button(logs, text="Ģenerēt skaitli", command=generet_skaitli)
poga.grid(row=2, column=0, columnspan=2, pady=10)

# Izveido tukšu tekstu, kurā tiks parādīts rezultāts, ar lielu fontu, un novieto ceturtajā rindā, aizņemot abas kolonnas
label_rezultats = tk.Label(logs, text="", font=("Arial", 16))
label_rezultats.grid(row=3, column=0, columnspan=2, pady=10)

# Sāk galvenās notikumu cilpas izpildi, kas uztur logu atvērtu un reaģē uz notikumiem
logs.mainloop()
