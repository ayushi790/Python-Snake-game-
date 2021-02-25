import turtle
from turtle import*
from random import randrange
from freegames import square, vector

#setup the screen
screen = turtle.Screen()
screen.title("Snake Game- by Ayushi Gupta")
screen.bgcolor("yellow")
screen.setup(width=700, height=700)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,300)
pen.write("Score:0", align="center", font=("Courier",24,"normal"))
pen.write("___________________________", align="center", font=("Courier",24,"normal"))

timing = 100
food = vector(40, 40)
snake = [vector(0, 0)]
aim = vector(0, -10)


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -340 < head.x < 340 and -340 < head.y < 340

def move():
    "Move snake forward one segment."
    global timing
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        pen.clear()
        pen.goto(0,240)
        pen.write("Final Score:{}".format((len(snake)-1)*10), align="center", font=("Courier",24,"normal"))
        pen.goto(0,210)
        pen.write("Game has ended! Thanks for playing", align ="center", font=("Courier",18,"normal"))
        print("Game ended")
        return()

    snake.append(head)

    if head == food:
        if timing>=30:
            timing-=10
        else:
            timing-=0.1
        print('Snake:',(len(snake)-1)*10)
        pen.clear()
        pen.write("Score:{}".format((len(snake)-1)*10), align="center", font=("Courier",24,"normal"))
        pen.write("___________________________", align="center", font=("Courier",24,"normal"))
        food.x = randrange(-33, 33)*10 
        food.y = randrange(-33, 29)*10
    else:
        snake.pop(0)

        
    clear()

    for body in snake:
        square(body.x, body.y, 9, 'green')

    square(food.x, food.y, 9, 'red')
    update()
    print("time ",timing)
    ontimer(move, timing)
    
    
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()




#while True:
    #update()
    #move()
    #food = vector(0, 0)
    #snake = [vector(10, 0)]
    #aim = vector(0, -10)
    #time.sleep(delay)


    
