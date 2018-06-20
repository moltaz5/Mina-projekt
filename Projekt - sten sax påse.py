while True:
    import random


    human_score=0
    computer_score=0

    val=["sten", "sax", "påse"]

    print("")
    print("")
    print("")
    print("Välkommen till en match i sten sax påse mot datorn!")
    print("Först till tre vinner. Lycka till")



    while True:
        computer_choice= random.choice(val)
        print("")
        print("")
        print("")
        human_choice=input("Vad väljer du? (Skriv med små bokstäver)")
        if human_choice != "sten" and human_choice != "sax" and human_choice != "påse":
            print("Du måste välja antingen sten, sax eller påse")
            continue
        if human_choice != computer_choice:
            print("Datorn valde", computer_choice)
            print("")
        if computer_choice=="sten" and human_choice=="sax":
            computer_score +=1
            print("Datorn tog poänget den här gången")
        elif computer_choice=="sten" and human_choice=="påse":
            human_score +=1
            print("Du fick poäng!")
        elif computer_choice=="påse" and human_choice=="sten":
            computer_score += 1
            print("Datorn fick poäng :(")
        elif computer_choice=="påse" and human_choice=="sax":
            human_score +=1
            print("Bra jobbat! Du fick poäng")
        elif computer_choice=="sax" and human_choice=="påse":
            computer_score += 1
            print("Datorn tog hem det den här poängen")
        elif computer_choice=="sax" and human_choice=="sten":
            human_score +=1
            print("Du är bra!")
        elif computer_choice==human_choice:
            print("Datorn valde också", human_choice + "!")
        print("")
        print("Datorns poäng:", computer_score)
        print("Dina poäng:", human_score)
        if computer_score==3:
            print("")
            print("Tyvärr, du förlorade och spelet är slut")
            break
        elif human_score==3:
            print("")
            print("Grattis, du vann!")
            break

    svar=input("Vill du spela igen? (svara ja eller nej med små bokstäver)")
    if svar== "ja":
        continue
    elif svar=="nej":
        break
