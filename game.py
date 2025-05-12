import turtle
import time

screen = turtle.Screen()
screen.setup(400, 600)
screen.bgpic("background.gif")
screen.tracer(0)  


spaceship = turtle.Turtle()
spaceship_img = "spaceship.gif"
screen.register_shape(spaceship_img)
spaceship.shape(spaceship_img)
spaceship.penup()
spaceship.goto(0, -250)


asteroid = turtle.Turtle()
asteroid_img = "asteroid.gif"
screen.register_shape(asteroid_img)
asteroid.shape(asteroid_img)
asteroid.penup()
asteroid.goto(0, 270)


def move_right():
    spaceship.setx(spaceship.xcor() + 10)

def move_left():
    spaceship.setx(spaceship.xcor() - 10)


screen.listen()
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")


while True:
    # Move asteroid down
    asteroid.sety(asteroid.ycor() - 10)
    asteroid.left(10)


    if asteroid.ycor() <= -330:
        asteroid.hideturtle()
        asteroid.goto(0, 300)
        asteroid.showturtle()

  
    screen.update()
    time.sleep(0.05) 
