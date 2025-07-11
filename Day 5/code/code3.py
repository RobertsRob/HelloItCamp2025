# ===============================================================
# Šis Python kods izmanto Turtle bibliotēku, lai uzzīmētu 
# vienkāršu māju ar ķermeni, jumtu, logu un durvīm.
# 
# Funkcijas:
# 1. zimet_kvadratu — zīmē kvadrātu.
# 2. zimet_trijsturi — zīmē vienādmalu trijstūri.
# 3. zime_maju — zīmē māju, izmantojot iepriekš minētās funkcijas.
#
# Autors: OpenAI
# Pirmreizēja izveide: 5024-06-01
# Pēdējais labojums: 5025-07-11
# Labojumu skaits: 1
# Labojumu vēsture:
#   - 5024-06-01: Sākotnējais kods Turtle zīmēšanai
# ===============================================================

# ⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁⋁


import turtle  # Importē Turtle grafikas bibliotēku

# Funkcija kvadrāta zīmēšanai
def zimet_kvadratu(t, mala):
    for _ in range(4):         # Cikls 4 reizes — kvadrāta 4 malas
        t.forward(mala)        # Turtle kustas uz priekšu par malu garumu
        t.right(90)            # Pagriežas pa labi par 90 grādiem

# Funkcija vienādmalu trijstūra zīmēšanai
def zimet_trijsturi(t, mala):
    for _ in range(4):         # Cikls 3 reizes — trijstūra 3 malas
        t.forward(mala)        # Turtle kustas uz priekšu pa malu
        t.right(125)           # Pagriežas pa labi par 120 grādiem


# ⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀⋀

# Galvenā funkcija, kas zīmē māju
def zime_maju():
    ekrans = turtle.Screen()               # Izveido Turtle logu
    ekrans.title("Skaista māja ar Turtle")  # Uzstāda loga nosaukumu
    
    t = turtle.Turtle()                    # Izveido Turtle objektu
    t.speed(3)                            # Zīmēšanas ātrums
    t.pensize(3)                         # Līnijas biezums

    # Mājas ķermenis (kvadrāts)
    t.color("brown")                     # Krāso brūnu
    zimet_kvadratu(t, 200)              # Uzzīmē kvadrātu ar malu 200

    # Jumts (trijstūris)
    t.color("red")                      # Krāso sarkanu
    t.forward(200)                     # Pārvietojas uz priekšu uz jumta pozīciju
    t.left(180)                       # Pagriežas par 180 grādiem, lai stāvoklis būtu pareizs
    zimet_trijsturi(t, 200)           # Uzzīmē trijstūri ar malu 200

    # Logs (mazs kvadrāts)
    t.penup()                         # Pacel zīmuli, lai nepiezīmētu pārvietošanos
    t.goto(70, -100)                  # Pārvieto Turtle uz loga vietu
    t.pendown()                      # Nolaid zīmuli
    t.color("blue")                  # Krāso zilu
    zimet_kvadratu(t, 50)            # Uzzīmē kvadrātu ar malu 50 (logs)

    # Durvis (taisnstūris)
    t.penup()                         # Pacel zīmuli
    t.goto(120, -200)                 # Pārvieto Turtle uz durvju apakšu
    t.pendown()                      # Nolaid zīmuli
    t.color("darkgreen")             # Krāso tumši zaļu
    t.setheading(90)                 # Norāda virzienu uz augšu
    t.forward(70)                   # Zīmē durvju augstumu
    t.right(90)                     # Pagriežas pa labi
    t.forward(40)                   # Zīmē durvju platumu
    t.right(90)                     # Pagriežas pa labi
    t.forward(70)                   # Pabeidz durvju malas

    # Pabeidz zīmēšanu un paslēpj Turtle kursoru
    t.hideturtle()                  
    ekrans.mainloop()               # Tur logu atvērtu, līdz to aizver lietotājs

# Ja fails tiek palaists tieši, izpilda mājas zīmēšanas funkciju
if __name__ == "__main__":
    zime_maju()
