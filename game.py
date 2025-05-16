import turtle
import time
import random

screen = turtle.Screen()
screen.setup(400, 600)
screen.bgpic("background.png")
screen.tracer(0)  


spaceship = turtle.Turtle()
spaceship_img = "spaceship.png"
screen.register_shape(spaceship_img) 
spaceship.shape(spaceship_img)
spaceship.penup()
spaceship.goto(0, -250)

bullet = turtle.Turtle()
bullet_img = "bullet.png"
screen.register_shape(bullet_img)
bullet.shape(bullet_img)
# bullet.hideturtle()
bullet.penup()
bullet.speed(0)

spaceshipx = spaceship.xcor()
spaceshipy = spaceship.ycor()
bullet.goto(spaceshipx, spaceshipy + 100)
bullet_state = "loaded"


asteroid = turtle.Turtle()
asteroid_img = "asteroid.png"
screen.register_shape(asteroid_img)
asteroid.shape(asteroid_img)
asteroid.penup()
asteroid.goto(0, 270)

score = 0
score_turtle = turtle.Turtle()
score_turtle.speed(0)
score_turtle.color("white")
score_turtle.penup()
score_turtle.goto(-190,230)
score_turtle.pendown()
score_turtle.hideturtle()
lives = 3
lives_turtle = turtle.Turtle()
lives_turtle.speed(0)
lives_turtle.color("white")
lives_turtle.penup()
lives_turtle.goto(80,230)
lives_turtle.pendown()
lives_turtle.hideturtle()

def display_score():
    global score
    score_turtle.clear()
    score_turtle.write("Score: " + str(score), font=("Arial",20,"bold"))

def display_lives():
    global score
    lives_turtle.clear()
    lives_turtle.write("Lives: " + str(lives), font=("Arial",20,"bold"))


def move_right():
    spaceship.setx(spaceship.xcor() + 50)

def move_left():
    spaceship.setx(spaceship.xcor() - 50)

def shoot():
    global bullet_state
    if bullet.ycor()>300:
        bullet_state = "loaded"
    if bullet_state == "loaded":
        spaceshipx = spaceship.xcor()
        spaceshipy = spaceship.ycor()
        # bullet.hideturtle()
        bullet.goto(spaceshipx,spaceshipy)
        bullet.showturtle()
        bullet_state = "fired"
    while bullet.ycor()<330:
        if bullet_state == 'fired':
            bulletx = bullet.xcor()
            bullety = bullet.ycor()
            bullet.goto(bulletx, bullety + 0.05)
screen.listen()
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")
screen.onkey(shoot, "Up")

def destroy_asteroid():
    pass

def reset_asteroid():
    if asteroid.ycor() <= -330:
        asteroid.hideturtle()
        x = random.randint(-175,175)
        asteroid.goto(x, 300)
        asteroid.showturtle()
while True:
    # Move asteroid down
    asteroid.sety(asteroid.ycor() - 10)
    asteroid.left(10)

    reset_asteroid()
    display_score()
    display_lives()
    distance = spaceship.distance(asteroid)
    print(distance)
    if distance <= 60:
        asteroid.hideturtle()
        asteroid.goto(random.randint(-170,170), 270)
        asteroid.showturtle()
    screen.update()
    time.sleep(0.05)
