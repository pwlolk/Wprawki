#Podstawowy kalkulator cydrowniczy
print("Ile pirosiarczynu, ile drożdży i ile pożywki".upper())
tpH   = ("2.9","3.0","3.1","3.2","3.3","3.4","3.5","3.6","3.7","3.8","3.9","4.0")
tpiro = ("0.7","0.8","1.0","1.2","1.4","1.7","2.1","2.5","3.0","3.7","4.5","5.5")
t_index = 0
while True:
    raw_juice = float(input("Podaj wielkość nastawu [L]: "))
    pH = float(input("Wartość pH [2.9-4.0]: "))
    pH_percent = float(input("Jaki procent zalecanej dawki pirosiarczynu chesz zadać[%]?: "))
    yeast_10L = float(input("Podaj ilośc drożdży [g/10L]: "))
    feed_10L = float(input("Podaj ilośc pożywki [g/10L]: "))
    #sulphur_10L = 797883.1 + (0.2967715 - 797883.1)/(1 + (pH/18.38982)^7.846172)
    #sulphur_10L = -0.565408051*pH**5 + 11.5743742*pH**4 - 89.3775177*pH**3 + 334.1185303*pH**2 - 611.111908*pH + 440.1496735

    if (pH == 2.9):
        sulphur_10L = float(tpiro[0])
    elif (pH == 4.0):
        sulphur_10L = float(tpiro[-1])
    else: #interpolacja w ustalonym przedziale
        while (float(tpH[t_index]) < pH):
            t_index = t_index + 1
        i_tpH_0 = float(tpH[t_index - 1])
        i_tpH_1 = float(tpH[t_index])
        i_tpiro_0 = float(tpiro[t_index - 1])
        i_tpiro_1 = float(tpiro[t_index])
        print('\n[Kontrolnie] Przedział pH:\t\t' + str(i_tpH_0) + '-' + str(i_tpH_1))
        print('[Kontrolnie] Przedział piro:\t' + str(i_tpiro_0) + '-' + str(i_tpiro_1))
        sulphur_10L = i_tpiro_0 + ((i_tpiro_1 - i_tpiro_0)/(i_tpH_1 - i_tpH_0))*(pH - i_tpH_0)

    sulphur_dose = (pH_percent/100)*(raw_juice*sulphur_10L)/10
    sulphur_dose = round(sulphur_dose, 1)
    yeast_dose = (raw_juice*yeast_10L)/10
    yeast_dose = round(yeast_dose, 1)
    feed_dose = (raw_juice*feed_10L)/10
    feed_dose = round(feed_dose, 1)
    print('\n' + "Dla " + str(raw_juice) + "L nastawu zadaj:")
    print("- pirosiarczynu: " + str(sulphur_dose) + "g")
    print("- drożdży:\t\t " + str(yeast_dose) + "g")
    print("- pożywki:\t\t " + str(feed_dose) + "g")
    print("")