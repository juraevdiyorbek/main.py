import turtle
from turtle import *
wn = Screen()
wn.bgcolor('black')

t = turtle.Turtle()
t.pencolor('white')

def curve():
    for i in range(200):
        t.rt(1)
        t.fd(1)

def heart():
    t.fillcolor('red')
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()

heart()
t.ht()

def write(message,pos):
    x,y = pos
    t.penup()
    t.goto(x,y)
    t.color('white')
    style = ('Stencil Std', 18 , 'italic')
    t.write(message,font=style)

write('F',(-68,95))
write('*',(-55,95))
write('C',(-42,95))
write('K',(-30,95))
write('O',(-14,95))
write('F',(10,95))
write('F',(26,95))
write('F',(45,95))



wn.mainloop()
#heart chiqaradi youtubedan olindi zerikishda
    
