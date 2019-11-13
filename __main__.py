import turtle
import random
import math
import time
import pdb


G = 0.1 #Gravitational Constant. I am God!!

def Gravity(mass,distance):
        return G * mass / (distance **2)



def CalcDistance(FirstPosition,SecondPosition):
        xdist = FirstPosition[0] - SecondPosition[0]
        ydist = FirstPosition[1] - SecondPosition[1]
        #return math.sqrt((xdist **2) + (ydist **2));
        return math.hypot(xdist,ydist)  #equivolent to above

def CalcDirection(FirstPosition,SecondPosition):
        xdist = FirstPosition[0] - SecondPosition[0]
        ydist = FirstPosition[1] - SecondPosition[1]        
        rad = math.atan2(xdist,ydist)
        return rad * 180 / (math.pi) #convert radians to degrees
        

def heading2direc(heading):
        work = 270 - heading
        while work < 0:
                work += 360
        while work > 360:
                work -= 360
        return work

#trying to get turtle.heading() and direction talking the same language.
#heading is calculated as a 360 angle anti-clockwise from the horizontal facing right.
#direction is calculated as an angle clockwise from the vertical, negative if to the left

def CalcChange(t,ag,ad):
        #t = the turtle being moved
        #ag = acceleration from gravity being exerted
        #ad = direction in which acceleration being exerted
        #pdb.set_trace()
        angle = (heading2direc(t.heading()) - ad) * math.pi / 180 #in radians
        vx = t.velocity + math.cos(angle) * ag  #acceleration in direction of travel
        vy = math.sin(angle) * ag  #acceleration perpendicular to direction of travel
        t.left(math.atan2(vy,vx) * 180 / math.pi)  #turn the turtle
        t.velocity = math.hypot(vy,vx) #change absolute velocity
        
                






tim = turtle.Turtle()
tim.name = "Tim"
tim.shape('classic')
tim.color('red')
tim.mass = 318  #mass of jupiter in earths
tim.velocity = 12
tim.penup()
tim.forward(200)
tim.right(90)
tim.pendown()


tom = turtle.Turtle()
tom.name = "Tom"
tom.shape('circle')
tom.color('yellow')
tom.mass = 330000  #mass of sun in earths
tom.velocity = 0



tammy = turtle.Turtle()
tammy.name = "Tammy"
tammy.shape('classic')
tammy.color('green')
tammy.mass = 95 #mass of saturn in earths
tammy.velocity = 13
tammy.penup()
tammy.right(180)
tammy.forward(250)
tammy.right(90)
tammy.pendown()



members = []

members.append(tim)
members.append(tom)
members.append(tammy)

for i in range(5):
        k = turtle.Turtle()
        k.name = str(i)
        k.shape('classic')
        k.color('green')
        k.mass=0.001
        k.penup()
        k.left(random.randint(0,360))
        k.forward(random.randint(100,300))
        k.right(90)
        k.velocity = random.randint(8,16)
        members.append(k)
        



tom.penup()


print(tim.heading())
print(tom.heading())


#for t in members:
#        t.penup()
#        t.left(random.randint(0,360))
#        t.forward(random.randint(50,300))
        #print(t.name)
        #print(t.position())
        #print(t.heading())


#for i in range(1000):
while True:
        for t in members:        
                for u in members:
                        if t != u:
                                distance = CalcDistance(t.position(),u.position())
                                direction = CalcDirection(t.position(),u.position())
                                #print("%s is %d from %s" %(t.name,round(distance),u.name))
                                #print("%s is %d from %s" %(t.name,direction,u.name))
                                CalcChange(t,Gravity(u.mass,distance),direction)
                t.forward(t.velocity) #move the turtle        
        


#print(tim.heading())
#print(CalcDirection(tim.position(),tom.position()))
#print(heading2direc(tim.heading()))

#tim.right(CalcDirection(tim.position(),tom.position()) - heading2direc(tim.heading()))
#tim.pendown()
#tim.forward(50)


