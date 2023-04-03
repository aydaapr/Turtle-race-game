from turtle import Turtle, Screen
import random

is_race_on=False

screen=Screen()
screen.setup(width=500, height=400)
my_turtles=[]

bet=screen.textinput(title="bet here", prompt="what color are you going to bet on:")
colors=["blue", "red", "yellow", "green", "purple", "orange"]

for item in range(6):
  turtle=Turtle()
  turtle.penup()
  color=random.choice(colors)
  turtle.color(color)
  colors.remove(color)
  turtle.shape("turtle")
  my_turtles.append(turtle)

positions=[-70, -40, -10, 20, 50, 80]

for turtle in my_turtles:
  position=random.choice(positions)
  turtle.goto(x=-230, y=(position))
  positions.remove(position) 
            
if bet:
  is_race_on=True

while is_race_on:

    
  for turtle in my_turtles:
    if turtle.xcor()>230:
      is_race_on=False
      winning= turtle.pencolor()
      print(f"the {winning} won the game")
      if winning==bet:
        print("You won the bet!")
      else:
        print("You are a looser!")
    turtle.forward(random.randint(0,10))

    


screen.exitonclick()