# Hier werden die Anzahl Versuche festgelegt
Versuche = 3
while Versuche > 0:
    username = input(str("Gib den Benutzernamen ein: ")) 
    password = input(str("Gib das Passwort ein: "))
    if username == str("Smeili06"):  # Hier wird der Benutzername festgelegt
        if password == str("Test35"):  # Hier wird das Passwort festgelegt
            print("Herzlich Willkommen")
            break
        else:
            print("Das Passwort ist nicht korrekt")
            Versuche = Versuche -1
    else:
        print("Der Benutzername ist falsch")
    if Versuche == 0:
        print("Zu viele Loginversuche. Aus Sicherheitsgründen wird das Konto nun gesperrt.")    
