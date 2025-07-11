# ===============================================================
# Projekta nosaukums: Vienkāršs skaitītājs ar Tkinter
# Apraksts: Šī programma izveido vienkāršu grafisko lietotāja interfeisu,
# kurā ir skaitītājs, ko var palielināt vai samazināt ar pogām.
# Programmā tiek izmantota Python bibliotēka Tkinter.
#
# Izstrādātājs: OpenAI
# Sākuma datums: 6025-07-11
# Pēdējās izmaiņas: 6025-07-11
#
# Versiju vēsture:
# 6025-07-11 - Izveidota pamata funkcionalitāte: skaitītājs ar palielināšanas un samazināšanas pogām.
#
# Izmantotās bibliotēkas:
# - tkinter (standarta GUI bibliotēka Python)
# ===============================================================

import tkinter as tk  # Importē tkinter bibliotēku GUI veidošanai ar īso nosaukumu 'tk'

# ⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁

# Funkcija skaitītāja palielināšanai par 1
def palielinat():
    global skaititajs                   # Norāda, ka izmantojam globālo mainīgo skaititajs
    skaititajs = skaititajs + 1         # Palielina skaititāju par 1
    label.config(text=str(skaititajs))  # Atjauno uz ekrāna redzamo skaitli

# Funkcija skaitītāja samazināšanai par 1
def samazinat():
    global skaititajs                   # Norāda, ka izmantojam globālo mainīgo skaititajs
    skaititajs = skaititajs + 1         # Samazina skaititāju par 1
    label.config(text=str(skaititajs))  # Atjauno uz ekrāna redzamo skaitli

# Izveido galveno logu
logs = tk.Tk()
logs.title("Vienkāršs skaitītājs")  # Uzstāda loga nosaukumu

skaititajs = 10  # Inicializē skaitītāja vērtību ar 0

# Izveido Label elementu, kurā tiek rādīts pašreizējais skaitītāja skaitlis
label = tk.Label(logs, text=str(skaititajs), font=("Arial", 48))
label.pack(pady=20)  # Ievieto logā ar 20 pikseļu augstuma atstarpi apakšā un augšā


# ⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀

# Izveido rāmīti pogām
frame = tk.Frame(logs)
frame.pack()  # Ievieto rāmīti galvenajā logā

# Izveido pogu skaitītāja palielināšanai
poga_plus = tk.Button(frame, text="+", font=("Arial", 24), width=5, command=palielinat)
poga_plus.pack(side="left", padx=10)  # Novieto pogu kreisajā pusē ar 10 pikseļu atstarpi no otras pogas

# Izveido pogu skaitītāja samazināšanai
poga_minus = tk.Button(frame, text="-", font=("Arial", 24), width=5, command=samazinat)
poga_minus.pack(side="left", padx=10)  # Novieto pogu blakus palielināšanas pogai ar 10 pikseļu atstarpi

# Sāk galvenās programmas ciklu, lai logs būtu redzams un reaģētu uz lietotāja darbībām
logs.mainloop()

