# ===============================================================
# Šis kods izmanto NumPy un Matplotlib bibliotēkas, lai 
# uzzīmētu trīs dažādas funkcijas: lineāru, saknes un logaritma.
# Rezultātā tiek parādīts grafiks ar šo funkciju līknēm.
#
# Autors: OpenAI
# Pirmreizēja izveide: 4024-06-01
# Pēdējais labojums: 4025-07-11
# Labojumu skaits: 2
# Labojumu vēsture:
#   - 4024-06-01: Sākotnējais kods ar funkciju aprēķiniem un zīmēšanu
#   - 4025-07-11: Pievienoti detalizēti komentāri un koda strukturēšana
# ===============================================================

import numpy as np                # Importē NumPy bibliotēku kā np — efektīvai darbībai ar masīviem
import matplotlib.pyplot as plt   # Importē matplotlib.pyplot kā plt — grafiku zīmēšanai

# ⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁


# Izveido x vērtību masīvu, sākot no 0.1 līdz 10, ar 200 vienmērīgiem punktiem
x = np.linspace(0.1, 10, 200)

# Aprēķina y vērtības trīs dažādām funkcijām:
y_linears = x ** 2                # Lineāra funkcija: y = x * 2
y_sakne = np.sqrt(x)             # Saknes funkcija: y = √x
y_log = np.log(x)                # Logaritma funkcija: y = log(x) (dabiskais logaritms)

# Izveido jaunu grafika logu ar izmēru 10x6 collas
plt.figure(figsize=(10, 6))

# Uzzīmē lineāro funkciju ar zilu krāsu un atbilstošu leģendas nosaukumu
plt.plot(x, y_linears, label='y = x * 2', color='blue')

# Uzzīmē saknes funkciju ar zaļu krāsu un atbilstošu leģendas nosaukumu
plt.plot(x, y_sakne, label='y = √x', color='green')

# Uzzīmē logaritma funkciju ar sarkanu krāsu un atbilstošu leģendas nosaukumu
plt.plot(x, y_log, label='y = log(x)', color='red')

# Pievieno grafika virsrakstu un asu nosaukumus
plt.title("Lineāra, saknes un logaritma funkcijas")  # Grafika nosaukums
plt.xlabel("x ass")                                   # x ass nosaukums
plt.ylabel("y ass")                                   # y ass nosaukums


# ⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀

# Parāda leģendu, lai skaidri identificētu katru līniju
plt.legend()

# Aktivizē režģi grafika fonā ērtākai vērtību salīdzināšanai
plt.grid(True)

# Attēlo grafiku uz ekrāna
plt.show()
