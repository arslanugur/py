import turtle

#Recursive function
def tree(plist, 1, a, f):
  if l > 5:
    lst = []
    for p in plist:
      p. forward(l)
      q = p.clone()
      p.left(a)
      q.right(a)
      lst.append(p)
      lst.append(q)
    tree(lst, l*f, a, f)

#create turtle object
p = turtle.Turtle()

#change the pen color to green
p.color("green")

#change the pen size
p.pensize(5)

p.hideturtle()
p.speed(100)
p.left(90)
p.penup()
p.goto(0, -200)
p.pendown()
t = tree([p], 200, 65, 0.6)


