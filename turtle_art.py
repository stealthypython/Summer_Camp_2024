import turtle

#Distance and size setup
dist = 1
size = 400

#full screen
screen = turtle.Screen()
screen.setup(1.0, 1.0)

#Art stuff
art = turtle.Turtle()
art.hideturtle()
art.speed(0)
art.color("light blue")

#determine background color
turtle.bgcolor("white")

while size > 0:
  art.forward(dist)
  art.left(2879)
  art.right(2790)
  dist += 1
  size -= 1

turtle.done()
while size > 0:
  for c in ['teal','lightblue','lavender','gold','pink']:
    art.color(c)
    art.forward(dist)
    art.left(200)
    art.right(396)
    dist += 1
    size +=  1

turtle.done()

like = input("Did you like the art? ")
if like == "yes":
  print("Thank you!")
else:
  print("Let's try again, then!")
  size = int(input("What size do you want? "))
  size = int(size)  # Convert the input to an integer
  while size > 0:
    art.forward(float(dist))
    art.left(12345678900987654321)
    art.right(1029102910291029102910291029102910291029102910291029)
