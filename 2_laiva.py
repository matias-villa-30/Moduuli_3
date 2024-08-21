laiva_luoka = input("Anna laivan hyttiluoaka: LUX, A, B, C: \n")
if laiva_luoka.lower() == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif laiva_luoka.lower() == "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif laiva_luoka.lower() == "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif laiva_luoka.lower() == "c":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")