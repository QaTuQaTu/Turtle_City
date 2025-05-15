from turtle import*
def grass():
    speed(999999999)
    penup()
    goto(-200,-200)
    pendown()
    color('light green')
    begin_fill()
    for i in range(2):
        forward(400)
        left(90)
        forward(100)
        left(90)
    end_fill()





    end_fill()

def sky():
    speed(999999999)
    penup()
    left(90)
    forward(100)
    pendown()
    color('sky blue')
    begin_fill()
    for i in range(2):
        forward(450)
        right(90)
        forward(400)
        right(90)
    end_fill()

def skyblack():
    speed(999999999)
    penup()
    left(90)
    forward(100)
    pendown()
    color('navy')
    begin_fill()
    for i in range(2):
        forward(450)
        right(90)
        forward(400)
        right(90)
    end_fill()

def building():
    speed(999999999)
    penup()
    goto(-170,-140)
    pendown()
    color('gray')
    begin_fill()
    for i in range(2):
        forward(210)
        right(90)
        forward(100)
        right(90)
    end_fill()
    penup()
    forward(20)
    right(90)
    forward(20)
    pendown()
    for i in range(4):
        color('yellow')
        begin_fill()
        for i in range(4):
            forward(20)
            left(90)
        penup()
        forward(40)
        pendown()
        color('yellow')
        begin_fill()
        for i in range(4):
            forward(20)
            left(90)
        end_fill()
        penup()
        forward(20)
        left(90)
        forward(20)
        left(90)
        forward(60)
        right (90)
        forward(20)
        right(90)
        pendown()
        end_fill()

def plus():
    penup()
    goto(170,-130)
    pendown()
    left(180)
    color('orange')
    begin_fill()
    for i in range(4):
        forward(120)
        right(90)
    end_fill()
    penup()
    forward(120)
    right(90)
    forward(80)
    right(90)
    forward(10)
    pendown()
    color('red')
    pensize(5)
    forward(30)
    left(180)
    forward(15)
    left(90)
    forward(15)
    right(180)
    forward(30)

def sun():
    penup()
    goto(170,200)
    forward(40)
    left(90)
    forward(15)
    pendown()
    pensize(2)
    color('Yellow')
    begin_fill()
    for i in range(18):
        forward(100)
        right(150)
        speed(500)
    end_fill()


def moon():
    penup()
    goto(150,250)
    forward(40)
    left(90)
    forward(15)
    pendown()
    pensize(2)
    color('white')
    begin_fill()
    circle(50)
    end_fill()

q=input('What is the time of the day right now?(day/night)')
if q=='day':
    grass()
    sky()
    building()
    plus()
    sun()
if q=='night':
    grass()
    skyblack()
    building()
    plus()
    sun()


    
grass()
exitonclick()


