sukupuoli = input("Mikä on sinun biologisen sukupuoli?\n")
hemoglobiini = int(input("Anna sinun hemoglobiiniarvo (g/l): "))

if sukupuoli.lower() == "mies":
    if hemoglobiini > 195:
        print("Hemoglobiiniarvo on korkea. \nMiehen normaali hemoglobiiniarvo on välillä 134-195 g/l.")
    elif hemoglobiini < 134:
        print("Hemoglobiiniarvo on matala. \nMiehen normaali hemoglobiiniarvo on välillä 134-195 g/l.")
    else:
        print("Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.")

if sukupuoli.lower() == "nainen":
    if hemoglobiini > 175:
        print("Hemoglobiiniarvo on korkea. \nNaisen normaali hemoglobiiniarvo on välillä 117-175 g/l.")
    elif hemoglobiini < 117:
        print("Hemoglobiiniarvo on matala. \nNaisen normaali hemoglobiiniarvo on välillä 117-175 g/l.")
    else:
        print("Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.")