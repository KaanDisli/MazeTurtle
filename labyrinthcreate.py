import turtle
import copy

dicoJeu = {}
labyrinth0 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

labyrinth2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]



labyrinth1 = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]


labyrinth_template = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]

wn = turtle.Screen()
wn.title("Turtle")
wn.bgcolor("black")
wn.setup(width=800, height = 600)
def pixel2cell(x,y):
    
    ligne = int((dicoJeu["coordy"]-y)  / 24)
    colonne =  int((x -dicoJeu["coordx"]) / 24)
    return  [ligne,colonne]
    
    
def cell2pixel(i,j):
    x = j*24 + dicoJeu["coordx"]
    y =  dicoJeu["coordy"] - i*24
 
    return [x,y]
    

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)  




    
def afficheTextuel(labyrinth):
    str= ""
   
    for i in range (len(labyrinth)):
        for k in range (len(labyrinth[i])):
            if labyrinth[i][k] == 1: 
                str += "#"
            elif labyrinth[i][k] == 0 and i == dicoJeu["entre"][0] and k == dicoJeu["entre"][1] :
                str += "x"
            elif labyrinth[i][k] == 0 and i == dicoJeu["sortie"][0] and k == dicoJeu["sortie"][1] :
                str += "o"
            
            else:
                str += " "
            
        str += "\n"
           
    print(str)  
    return str
            
def cell2pixel(i,j):
    x = j*24 + dicoJeu["coordx"]
    y =  dicoJeu["coordy"] - i*24
 
    return [x,y]            
def pixel2cell(startx,starty,player):
    
    ligne = ((player.ycor()- starty)  / 30) 
    colonne =  ((player.xcor() -startx) / 30) 
    print(int(colonne))
    print(int(ligne))
    
white_block_list = []
xclick = 0
yclick = 0
def getcoordinates():
    global white_block_list
    turtle.onscreenclick(testClic) 
    
def start_solving():
    turtle.onscreenclick(testClic) 
def testClic(x,y):
    global xclick
    global yclick
    global dicojeu
    global labyrinth_template
    xclick = int(x//1)
    yclick = int(y//1)
    xclick = (xclick - dicoJeu["coordx"])/24
    yclick = (dicoJeu["coordy"]-yclick)/24
    colonne = xclick
    line = yclick
    if (line == 0 and colonne ==0) or line<0 or colonne<0 or line >11 or colonne > 15 or (line == 10 and colonne ==15)  :
        print("outside bounds")
        
    else:
        print(int(line))
        print(int(colonne))
        a = cell2pixel(int(line),int(colonne))
        labyrinth_template[int(line)][int(colonne)] = 0
        pen.color("white")
        pen.goto(a[0],a[1])
        
        pen.stamp()

pen = Pen()
def default_entrance(laby,coordx,coordy):
    
    dicoJeu["coordx"]  = coordx + -1*(len(laby[0])*12)
    dicoJeu["coordy"] = coordy + (len(laby)*12)
  
    pen.goto(dicoJeu["coordx"], dicoJeu["coordy"])
    
    pen.color("green")
    pen.stamp()
    sortie = cell2pixel(10,15)
    pen.goto(sortie[0],sortie[1])
    pen.stamp()
    pen.up()
    

def afficheTextuel_list():
    newlab= []
    
    for x  in range (len(labyrinth_template)):
        newlab.append([])

    for i in range (len(labyrinth_template)):
        for k in range (len(labyrinth_template[i])):
            
            if labyrinth_template[i][k] == 1: 
                newlab[i].append("#")
            elif labyrinth_template[i][k] == 0 and i == 0 and k == 0 :
                newlab[i].append("x")
            elif labyrinth_template[i][k] == 0 and i == 10 and k == 15:
                newlab[i].append("X")
            
            else:
                newlab[i].append(".")
    newlab[0][0] ="X"
    newlab[10][15] = "x"
    str =""
    for i in range (len(labyrinth_template)):
        for k in range (len(newlab[i])):
            str = str + newlab[i][k]
        str+="\n"
    print(str)
    return str
    


default_entrance(labyrinth_template,0,0)

getcoordinates()
turtle.mainloop()
with open('newlab.laby', 'w') as f:
    f.write(afficheTextuel_list())