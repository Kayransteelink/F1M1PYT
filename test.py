print("Je alarm gaat af, wat ga je doen OPSTAAN of SNOOZE ?")
choice = input()
if choice == 'OPSTAAN':
    print("je gaat je bed uit en maakt je klaar!")
elif choice == 'opstaan':
    print("je gaat je bed uit en maakt je klaar!")
elif choice == 'SNOOZE':
    print("Hmmmmmm zzzzzzzzzzzzzzzzzzzzzzzzzz")
elif choice == 'snooze':
    print("Hmmmmmm zzzzzzzzzzzzzzzzzzzzzzzzzz")
else:
    print(choice, " is geen goede keuze")
print("je bent in je eentje online wat ga je doen ANIME KIJKEN of GAMEN")
keuze = input()
if keuze == "ANIME KIJKEN":
    print("welke anime ga je kijken? fire force of my hero")
    anime = input()
    if anime == "fire force":
        print("veel plezier")
    elif anime == "my hero":
        print("veel plezier")
elif keuze == "GAMEN":
    print("zet dan ook wat muziek op")
else:
    print(keuze, "je kan niet iets anders doen")
print("je wilt naar school gaan hoe ga je met de bus of fiets")
vervoer = input()
if vervoer == "fiets":
    print("is het mooi weer")
    weer = input()
    if weer == "ja":
        print("succes met fietsen")
    elif weer == "nee":
        print("probeer de bus te pakken")
elif vervoer == "bus":
    print("check je je tijden want je wilt niet telaat komen")

