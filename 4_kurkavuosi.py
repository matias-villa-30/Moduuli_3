vuosi = int(input("Kirjoita vuosiluku: "))

if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print(f"{vuosi} on kurkavuosi")
else:
    print(f"{vuosi} ei ole kurkavuosi")