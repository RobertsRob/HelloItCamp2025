
# 1. Izveidojiet mainīgu discount ar vērtību 20, total ar vērtību 150. Izdrukājiet rezultātu, kas parāda summu pēc atlaides (total - discount).
discount = 20
total = 150
print("Summa pēc atlaides:", total - discount)

# 2. Izveidojiet mainīgo totalAmount ar vērtību 200. Samaziniet to par 25% un izdrukājiet rezultātu.
totalAmount = 200
totalAmount = totalAmount * 0.75
print(totalAmount)


# 3. Izveidojiet mainīgos lielumus baseSalary un bonuss, piešķiriet tiem vērtības attiecīgi 50000 un 5000. 
# Aprēķiniet un parādiet kopējo algu, pieskaitot piemaksu (bonuss) pamatalgai (baseSalary), un parādiet ziņojumu par jauno algu, izmantojot rindu: "Jaunā alga: [rezultāts]".

baseSalary = 50000
bonuss = 5000
print("Jaunā alga:", baseSalary + bonuss)

# 4. Izveidojiet mainīgos length un width, piešķiriet tiem vērtības 12 un 8. 
# Aprēķiniet taisnstūra perimetru un izdrukājiet virkni "Taisnstūra perimetrs ar garumu [length] un platumu [width]: [perimetrs]", kur [perimetrs] ir perimetra aprēķina rezultāts.
length = 12
width = 8
print("Taisnstūra perimetrs ar garumu", length, "un platumu", width, ":", 2 * (length + width))


# 5. * Izveidojiet mainīgos textToDublicate, number_1, number_2 un number_3, piešķiriet tiem attiecīgi vērtības "Apple", 2, 5 un 3. 
# Pēc tam izveidojiet mainīgo dublicationsCount, kas saglabā izteiksmes (skaitlis_2 - skaitlis_1) * skaitlis_3 rezultātu. 
# Izvadiet virkni "Teksts dublēts [dublicationsCount] reizes: [rezultāts]", kur [rezultāts] ir teksts "Apple", dublēts [dublicationsCount] reizes.
textToDublicate = "Apple"
number_1 = 2
number_2 = 5
number_3 = 3
dublicationsCount = (number_2 - number_1) * number_3
print("Dublikāts", dublicationsCount, "teksta reizes:", textToDublicate * dublicationsCount)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 1. Izveidojiet mainīgos x un y, piešķiriet tiem vērtības 15 un 10. Pārbaudiet, vai x ir 15 un vai y ir 5, un izdrukājiet abus rezultātus ar paskaidrojumiem.
x = 15
y = 10
print("x ir 15:", x == 15)
print("y ir 5:", y == 5)

# 2. Izveidojiet mainīgos cost un discount, piešķiriet tām vērtības 100 un 20. Pārbaudiet, vai cost ir lielāka par discount, un izdrukājiet rezultātu ar skaidrojumu.
cost = 100
discount = 20
print("Cena ir lielāka par atlaidi:", cost > discount)


# 5. Izveidojiet mainīgos a un b, piešķiriet tiem vērtības 10 un 5. Pārbaudiet, vai a * b ir lielāks vai vienāds ar 10 un vai b nav vienāds ar 10, un izdrukājiet abus rezultātus ar paskaidrojumiem.
a = 10
b = 5
print("a * b ir lielāks vai vienāds ar 10:", a * b >= 10)
print("b nav vienāds ar 10:", b != 10)

#  4. Izveidojiet mainīgos base un exponent, piešķiriet tiem vērtības 2 un 20.P ārbaudiet, vai base pakāpē exponent ir mazāks par 50000 (piecdesmit tūkstošiem), un izvadiet rezultātu.
base = 2
exponent = 20
print(base ** exponent < 50000)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 1. Uzrakstiet programmu, kas pieprasa lietotājam ievadīt divus veselus skaitļus un vienu teksta rindu.
# Programmai jāizvada ievadītais teksts tik reižu, cik norādīts katrā no skaitļiem atsevišķi.

number_1 = int(input("Ievadi pirmo skaitli: "))
number_2 = int(input("Ievadi otro skaitli: "))
text = input("Ievadi tekstu: ")
print(text * number_1)
print(text * number_2)


# 2. Izveidojiet programmu, kas pieprasa lietotājam ievadīt taisnstūra garumu un platumu.
# Pēc tam izvadiet taisnstūra perimetru un laukumu, izmantojot f-virknes.
# Ja garums ir vienāds ar platumu, izvadiet ziņojumu, ka tas ir kvadrāts.

length = float(input("Ievadi taisnstūra garumu: "))
width = float(input("Ievadi taisnstūra platumu: "))
perimeter = 2 * (length + width)
area = length * width
print(f"Taisnstūra perimetrs: {perimeter}")
print(f"Taisnstūra laukums: {area}")
print("Šis taisnstūris ir kvadrāts." * int(length == width))


# 3. Izveidojiet programmu, kas pieprasa lietotājam ievadīt pilsētas nosaukumu, iedzīvotāju skaitu un mašīnu skaitu pilsētā.
# Programmai jāizvada informācija par iedzīvotājiem un mašīnām, jāaprēķina vidējais cilvēku skaits uz vienu mašīnu,
# un jāpārbauda, vai pilsētā ir vairāk mašīnu nekā iedzīvotāju.

city_name = input("Ievadi pilsētas nosaukumu: ")
population = int(input("Ievadi pilsētas iedzīvotāju skaitu: "))
car_count = int(input("Ievadi mašīnu skaitu pilsētā: "))

print(f"Pilsētā {city_name} dzīvo {population} cilvēki un ir {car_count} mašīnas!")
print(f"Šajā pilsētā uz vienu mašīnu vidēji ir {int(population / car_count)} cilvēki.")
print(f"Vai šajā pilsētā ir vairāk mašīnu nekā cilvēku? {car_count > population}")


# 4. *Izveidojiet programmu, kas pieprasa lietotājam ievadīt pašreizējo laiku (saulains / apmācies),
# atmosfēras spiedienu gPa un vēja ātrumu m/s.
# Programmai jānosaka, vai, iespējams, būs vētra, pamatojoties uz šādiem nosacījumiem:
# laiks ir apmācies, spiediens ir augsts (1020 gPa un vairāk) un vējš ir stiprs (25 m/s un vairāk).
# Izvadiet informāciju par vētras iespējamību un kopējo "sliktā laika punktu" skaitu.

weather = input("Ievadi, kāds šodien laiks (saulains/apmācies): ")
pressure = int(input("Ievadi atmosfēras spiedienu gPa: "))
wind_speed = int(input("Ievadi vēja ātrumu m/s: "))

storm_points = 0
is_weather_bad = weather == "apmācies"
is_high_pressure = pressure >= 1020
is_fast_wind = wind_speed >= 25

storm_points = int(is_weather_bad) + int(is_high_pressure) + int(is_fast_wind)

print(f"Vai, iespējams, būs vētra: {storm_points == 3}")
print(f"Sliktā laika punkti: {storm_points}")