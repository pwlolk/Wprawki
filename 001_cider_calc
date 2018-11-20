#Podstawowy kalkulator cydrowniczy
print("Ile pirosiarczynu, ile drożdży i ile pożywki".upper())
while True:
    raw_juice = float(input("Podaj wielkość nastawu [L]: "))
    pH = float(input("Wartość pH [2.9-4.0]: "))
    yeast_10L = float(input("Podaj ilośc drożdży [g/10L]: "))
    feed_10L = float(input("Podaj ilośc pożywki [g/10L]: "))
    #sulphur_10L = 797883.1 + (0.2967715 - 797883.1)/(1 + (pH/18.38982)^7.846172)
    #sulphur_10L = -0.565408051*pH**5 + 11.5743742*pH**4 - 89.3775177*pH**3 + 334.1185303*pH**2 - 611.111908*pH + 440.1496735
    if (pH == 2.9):
        sulphur_10L = 0.7
    elif (pH == 3.0):
        sulphur_10L = 0.8
    elif (pH == 3.1):
        sulphur_10L = 1.0
    elif (pH == 3.2):
        sulphur_10L = 1.2
    elif (pH == 3.3):
        sulphur_10L = 1.4
    elif (pH == 3.4):
        sulphur_10L = 1.7
    elif (pH == 3.5):
        sulphur_10L = 2.1
    elif (pH == 3.6):
        sulphur_10L = 2.5
    elif (pH == 3.7):
        sulphur_10L = 3.0
    elif (pH == 3.8):
        sulphur_10L = 3.7
    elif (pH == 3.9):
        sulphur_10L = 4.5
    elif (pH == 4.0):
        sulphur_10L = 5.5
    sulphur_dose = (raw_juice*sulphur_10L)/10
    sulphur_dose = round(sulphur_dose, 2)
    yeast_dose = (raw_juice*yeast_10L)/10
    yeast_dose = round(yeast_dose, 2)
    feed_dose = (raw_juice*feed_10L)/10
    feed_dose = round(feed_dose, 2)
    print('\n' + "Dla " + str(raw_juice) + "L nastawu zadaj:")
    print("- pirosiarczynu - " + str(sulphur_dose) +"g")
    print("- drożdży - " + str(yeast_dose) +"g")
    print("- pożywki - " + str(feed_dose) +"g")
    print("")
