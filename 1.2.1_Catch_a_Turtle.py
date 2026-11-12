# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random

#-----game configuration----
t_shape = "circle"
t_colors = ["red", "blue", "orange", "purple", "gold"]
t_sizes = [1,2,3,4,5,6,7,8,9,10]
score = 0
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
font_setup = ("Arial", 20, "normal")


#-----initialize turtles-----
spot = trtl.Turtle()
spot.shape(t_shape)
spot.fillcolor("red")
spot.turtlesize(3)
spot.penup()


score_writer = trtl.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(-300,250)

counter =  trtl.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(200,250)

#-----game functions--------
def spot_clicked(x, y):
  global timer_up
  if timer_up:
     spot.hideturtle()
  else:
    update_score()
    change_position()
    

def change_position():
    new_xpos = random.randint(-350, 350)
    new_ypos = random.randint(-300, 300)
    spot.hideturtle()
    spot.goto(new_xpos, new_ypos)
    spot.turtlesize(random.choice(t_sizes))
    spot.fillcolor(random.choice(t_colors))
    spot.showturtle()

def update_score():
   global score
   score += 1
   score_writer.clear()
   score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

#-----events----------------
wn = trtl.Screen()
wn.bgcolor("green")
spot.onclick(spot_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
