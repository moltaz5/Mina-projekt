from turtle import *
start=-140, 140
start_x=-140
start_y=140
penup()
goto(start[0], start[1])
pendown()
speed(0)




#u=up
#d=down
#l=left
#r=right
#m=middle

ul=start_x, start_y
um=start_x+100, start_y
ur=start_x+200, start_y
ml=start_x, start_y-100
mm=start_x+100, start_y-100
mr=start_x+200, start_y-100
dl=start_x, start_y-200
dm=start_x+100, start_y-200
dr=start_x+200, start_y-200


winning_moves=[{ul, um, ur}, {ml, mm, mr}, {dl, dm, dr},
               {ul, ml, dl}, {um, mm, dm}, {ur, mr, dr}]




#Skapar spelplanen

forward(300)
print(pos())
penup()
right(90)
forward(100)
right(90)
pendown()
forward(300)
left(90)
penup()
forward(100)
left(90)
pendown()
forward(300)
penup()
rt(90)
forward(100)
rt(90)
pendown()
forward(300)

rt(90)
fd(300)
rt(90)
fd(100)
rt(90)
forward(300)
lt(90)
fd(100)
left(90)
forward(300)
rt(90)
fd(100)
rt(90)
fd(300)


def write_a_cross(xy):
    color("red")
    penup()
    goto(xy[0], xy[1])
    pendown()
    seth(315)
    fd(141.4)
    penup()
    left(135)
    fd(100)
    pendown()
    left(135)
    fd(141.4)



def write_a_circle(xy):
    color("blue")
    penup()
    goto(xy[0], xy[1])
    seth(277)
    fd(60)
    pendown()
    for i in range(20):
        left(18)
        fd(13)



#Nu till själva spelet



while True:
    print("Hej och välkomna till en omgång luffarschack!")
    print("Först som får tre cirklar/kryss i rad vinner.")
    print("Kontrollerna fungerar som följer. Översätt upp, mitten, ned samt")
    print("vänster och höger till engelska och skriv sedan detta sammandraget.")
    print("Uppe vänster (up left) blir alltså 'ul'.")
    player_1_choices=[]
    player_2_choices=[]
    choices=[ul, um, ur, ml, mm, mr, dl, dm, dr]

    while True:

        val_1=input("Spelare 1, välj en ruta: ")
        print(val_1)
        if val_1 not in choices:
            print("Det där kan du tyvärr inte välja.")
            continue
        elif val_1 in choices:
            write_a_cross(val_1)
            choices.remove(val_1)
            
            player_1_choices.append(val_1)

        val_2=input("Spelare 2, välj en ruta: ")
        if val_2 not in choices:
            continue
            print("Det där kan du tyvärr inte välja")
        else:
            write_a_circle(val_2)
            choices.remove(val_2)
            player_2_choices.append(val_2)


        if player_1_choices in winning_moves:
            print("Spelare 1 vann!")
            break
        elif player_2_choices in winning_moves:
            print("Spelare 2 vann!")
            break



