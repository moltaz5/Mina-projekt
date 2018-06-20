from turtle import *
from random import randint
penup()
speed(0)
goto(-140, 140)
for i in range(11):
    write(i, align="center")
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)


print("Dags för ett nytt spel! Den här gången ska du och din kompis gissa")
print("vilken av sköldpaddorna Oscar och Arvid som först vinner 3 race!")
print("Först till 3 rätta gissningar vinner :)")
print("")

gissning1=input("Här får spelare 1 gisssa. Vem tror du vinner? Arvid eller Oscar?")
gissning2=input("Här får spelare 2 gissa. Oscar eller Arvid?")



spelare1_score=0
spelare2_score=0


while True:
    print("")
    print("")
    Oscar=Turtle()
    Oscar.color("black")
    Oscar.shape("turtle")
    Oscar.penup()
    Oscar.goto(-160,100)
    Oscar.pendown()
    for i in range(10):
        Oscar.left(36)


    Arvid=Turtle()
    Arvid.color("blue")
    Arvid.shape("turtle")
    Arvid.penup()
    Arvid.goto(-160,80)
    Arvid.pendown()

    for i in range(10):
        Arvid.right(36)



    while True:
        Oscar.forward(randint(1,5))
        Arvid.forward(randint(1,5))
        if Arvid.xcor()>80:
            vinnare="Arvid"
            print("")
            print("Arvid vann!")
            print("")
            break
        elif Oscar.xcor()>80:
            vinnare="Oscar"
            print("")
            print("Oscar vann!")
            print("")
            break

    if gissning1==vinnare:
        print("Poäng till spelare 1!")
        spelare1_score+=1
    elif gissning2==vinnare:
        print("Poäng till spelare 2!")
        spelare2_score+=1
    elif gissning1==vinnare and gissning2==vinnare:
        print("Poäng till båda!")
        spelare1_score+=1
        spelare2_score+=1

    print("")
    print("Nu är ställningen", spelare1_score, " poäng till spelare 1 och", spelare2_score, "poäng till spelare 2")

    if spelare1_score==3:
        print("")
        print("Spelare 1 vann!")
        break
    elif spelare2_score==3:
        print("")
        print("Spelare 2 vann!")
        break
