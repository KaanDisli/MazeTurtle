import turtle


dicoJeu = {}
labyrinth1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

labyrinth0 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

labyrinth2= [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

labyrinth3 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
[1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1],
[1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
[1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
def labyFromFile(fn) :
    """
    Lecture d'un labyrinthe dans le fichier de nom fn
    Read a maze from the file named fn.
    """
    f = open(fn)
    laby = []
    indline = 0
    for fileline in f:
        labyline = []
        inditem = 0
        for item in fileline:
            # empty cell / case vide
            if item == ".":
                labyline.append(0)
            # wall / mur
            elif item == "#":
                labyline.append(1)
            # entrance / entree
            elif item == "x":
                labyline.append(0)
                mazeIn = [indline, inditem]
            # exit / sortie
            elif item == "X":
                labyline.append(0)
                mazeOut = [indline, inditem]
            # discard "\n" char at the end of each line
            inditem += 1
        laby.append(labyline)
        indline += 1
    f.close()
    return laby, mazeIn, mazeOut

def afficheLisible():
    fichier = input("Entrez un nom de ficihier ")
    laby, mazeIn, mazeOut = labyFromFile(fichier)
    print("Le labyrinthe:")
    for i in laby:
        print(i) 
        
    print("L'entree: " , mazeIn)
    print("La sortie: " , mazeOut)
    global LABY_DECIDER
    LABY_DECIDER = laby
    global dicoJeu
    print(laby)
    dicoJeu["entre"]= mazeIn
    dicoJeu["sortie"] = mazeOut
  




def afficheTextuel_list(labyrinth):
    newlab= []
    for x  in range (len(labyrinth)):
        newlab.append([])

    for i in range (len(labyrinth)):
        for k in range (len(labyrinth[i])):
            
            if labyrinth[i][k] == 1: 
                newlab[i].append("#")
            elif labyrinth[i][k] == 0 and i == dicoJeu["entre"][0] and k == dicoJeu["entre"][1] :
                newlab[i].append("x")
            elif labyrinth[i][k] == 0 and i == dicoJeu["sortie"][0] and k == dicoJeu["sortie"][1] :
                newlab[i].append("o")
            
            else:
                newlab[i].append("")
            

   
    return newlab


Chemin = []
find_chemin = []
position_list = []

def gauche():
    x = turtle.xcor()
    y = turtle.ycor()
    x = x -24
    global Chemin
    global LABY_DECIDER
   
    cord = pixel2cell(x,y)
    if typeCellule(cord[0],cord[1],LABY_DECIDER) == "passage standard" or  typeCellule(cord[0],cord[1],LABY_DECIDER) ==  "entre" or typeCellule(cord[0],cord[1],LABY_DECIDER) ==  "sortie" or  typeCellule(cord[0],cord[1],LABY_DECIDER) == "carrefour" or typeCellule(cord[0],cord[1],LABY_DECIDER) == "impasse":
        turtle.goto(x, y)
        print("gauche ; left")
        
        turtle.color("blue")
        Chemin.append("g")
        if typeCellule(cord[0],cord[1],LABY_DECIDER) == "carrefour":
            turtle.color("orange")
            return 2
        if typeCellule(cord[0],cord[1],LABY_DECIDER) == "sortie":
            turtle.color("green")
            print("YOU WON")
          
            return 3
    else:
        print("that is a wall")
        turtle.color("red")
        return -1
       
def droite():
    global Chemin
    x = turtle.xcor()
    y = turtle.ycor()
    x = x + 24
    cord = pixel2cell(x,y)

    global LABY_DECIDER
    
    if typeCellule(cord[0],cord[1],LABY_DECIDER) == "passage standard" or  typeCellule(cord[0],cord[1],LABY_DECIDER) ==  "entre" or typeCellule(cord[0],cord[1],LABY_DECIDER) ==  "sortie" or  typeCellule(cord[0],cord[1],LABY_DECIDER) == "carrefour" or typeCellule(cord[0],cord[1],LABY_DECIDER) == "impasse":
        turtle.goto(x, y)
        print("droite ; right")
     
        turtle.color("blue")
        Chemin.append("d")
        if typeCellule(cord[0],cord[1],LABY_DECIDER) == "carrefour":
            turtle.color("orange")
            return 2
        if typeCellule(cord[0],cord[1],LABY_DECIDER) == "sortie":
            turtle.color("green")
            print("YOU WON")
            
            return 3
        return "droite"
    else:
        print("that is a wall")
        turtle.color("red")
        return -1
       
def bas():
    global Chemin
    x = turtle.xcor()
    y = turtle.ycor()
    y = y -24
    cord = pixel2cell(x,y)
    global LABY_DECIDER
    if typeCellule(cord[0],cord[1],LABY_DECIDER) == "passage standard" or  typeCellule(cord[0],cord[1],LABY_DECIDER) ==  "entre" or typeCellule(cord[0],cord[1],LABY_DECIDER) ==  "sortie" or  typeCellule(cord[0],cord[1],LABY_DECIDER) == "carrefour" or typeCellule(cord[0],cord[1],LABY_DECIDER) == "impasse":
        turtle.goto(x, y)
        print("bas ; down")
       
        turtle.color("blue")
        Chemin.append("b")
        if typeCellule(cord[0],cord[1],LABY_DECIDER) == "carrefour":
            turtle.color("orange")
            return 2
        if typeCellule(cord[0],cord[1],LABY_DECIDER) == "sortie":
            turtle.color("green")
            print("YOU WON")
           
            return 3
    else:
        print("that is a wall")
        turtle.color("red")
        return -1
        
def haut():
    global Chemin
    x = turtle.xcor()
    y = turtle.ycor()
    y = y +24
    cord = pixel2cell(x,y)
    i = 0
    global LABY_DECIDER
    if typeCellule(cord[0],cord[1],LABY_DECIDER) == "passage standard" or  typeCellule(cord[0],cord[1],LABY_DECIDER) ==  "entre" or typeCellule(cord[0],cord[1],LABY_DECIDER) ==  "sortie" or  typeCellule(cord[0],cord[1],LABY_DECIDER) == "carrefour" or typeCellule(cord[0],cord[1],LABY_DECIDER) == "impasse":
        turtle.goto(x,y)
        print("haut ; up")
        turtle.color("blue")
        Chemin.append("h")
        if typeCellule(cord[0],cord[1],LABY_DECIDER) == "carrefour":
            turtle.color("orange")
            return 2
        if typeCellule(cord[0],cord[1],LABY_DECIDER) == "sortie":
            turtle.color("green")
            print("YOU WON")
          
            return 3
    else:
        print("that is a wall")
        turtle.color("red")
        return -1
       
def suivreChemin(li):
    x = turtle.xcor()
    y = turtle.ycor()
    x = x +24
    cord = pixel2cell(x,y)
    for i in li:
        
      
            if i=="g":
                if gauche() == -1:
                   
                    print("ERROR")
                    return -1

            elif i=="d":
                if droite() == -1:
                    print("ERROR")
                    return -1
            elif i=="h":
                if haut() == -1:
                    print("ERROR")
                    return -1
            elif i=="b":
                
                if bas() == -1:
                    print("ERROR")
                    return -1


           
    "success"
    return 1

def reverse_lettre(lettre):
    if lettre == "h":
        return "b"
    if lettre == "b":
        return "h"
    if lettre == "g":
        return "d"
    if lettre == "d":
        return "g"
    else:
        print("PAS UN LETTRE")
def inverserChemin(li):
    
    li_inverse = []
    for i in li:
        if i == "g":
            li_inverse.append("d")
        if i == "d":
            li_inverse.append("g")
        if i == "b":
            li_inverse.append("h")
                     
        if i == "h":
            li_inverse.append("b")
    li_inverse.reverse()     
    suivreChemin(li_inverse)
    
            
            
turtle.onkeypress(gauche, "Left")
turtle.onkeypress(droite, "Right")
turtle.onkeypress(haut, "Up")
turtle.onkeypress(bas, "Down")
turtle.listen()


def explorer_mini(type,position,laby,lettre):
            global position_list
            if typeCellule(position[0],position[1],laby) == "carrefour":    
                if type == "memorize":
                    position_list = []
                type2 = "memorize"
                if type == "create_wall":
                    for i in range (len(position_list)):
                        laby[position_list[i][0]][position_list[i][1]] = 1
                    if lettre == "d":
                            if haut() != -1:
                                return explorer(laby,'h', "normal")
                            if bas() != -1:
                                return explorer(laby,'b', "normal")
                    if lettre == "g":
                            if haut() != -1:
                                return explorer(laby,'h', "normal")
                            if bas() != -1:
                                return explorer(laby,'b', "normal")        
                    if lettre == "h":
                            if gauche() != -1:
                                return explorer(laby,'g', "normal")
                            if droite() != -1:
                                return explorer(laby,'d', "normal")  
                    if lettre == "b":  
                         if gauche() != -1:
                                return explorer(laby,'g', "normal")
                         if droite() != -1:
                                return explorer(laby,'d', "normal")     
                            
                return explorer(laby,lettre, type2)
            if type == "memorize":
                position_list.append(position)           
            if typeCellule(position[0],position[1],laby) == "impasse":
                return explorer(laby,reverse_lettre(lettre), "create_wall")
            


def explorer(laby,lettre,type):
    sortie_line = dicoJeu['sortie'][0]
    sortie_colonne = dicoJeu['sortie'][1]
    k = True
    global find_chemin
    global counter
    global position_list
    global const
    tmp = []
    
    position = pixel2cell(turtle.xcor(),turtle.ycor())
    if position[0] ==  sortie_line and position[1] ==sortie_colonne:
                     print("You have explored the game")
                     return 
    while (k==True):
        
        if lettre == "g": 
            if gauche() != -1:
                position = pixel2cell(turtle.xcor(),turtle.ycor())
                if position[0] ==  sortie_line and position[1] ==sortie_colonne:
                     print("You have explored the game")
                     return 
                explorer_mini(type,position,laby,lettre)
                   
                   
                return explorer(laby,"g",type)
            if haut() != -1:
                
                position = pixel2cell(turtle.xcor(),turtle.ycor())
                
                if position[0] ==  sortie_line and position[1] ==sortie_colonne:
                     print("You have explored the game")
                     return
                 
                 
                explorer_mini(type,position,laby,lettre)
                return explorer(laby,"h",type)
            if bas() != -1:
                
                position = pixel2cell(turtle.xcor(),turtle.ycor())
                if position[0] ==  sortie_line and position[1] ==sortie_colonne:
                    print("You have explored the game")
                    return
                
                explorer_mini(type,position,laby,lettre)
                return explorer(laby,"b",type)
        if lettre == "d": 
            if droite() != -1:
               
                position = pixel2cell(turtle.xcor(),turtle.ycor())
                
                
                if position[0] ==  sortie_line and position[1] ==sortie_colonne:
                    print("You have explored the game")
                    
                    return 1
            
                explorer_mini(type,position,laby,lettre)   
                return explorer(laby,"d",type)
            if haut() != -1:
                
                position = pixel2cell(turtle.xcor(),turtle.ycor())
                if position[0] ==  sortie_line and position[1] ==sortie_colonne:
                     print("You have explored the game")
                     return
               
                explorer_mini(type,position,laby,lettre)
                return explorer(laby,"h",type)
            if bas() != -1:
                
                position = pixel2cell(turtle.xcor(),turtle.ycor())
                if position[0] ==  sortie_line and position[1] ==sortie_colonne:
                    print("You have explored the game")
                    return
               
                explorer_mini(type,position,laby,lettre)
                return explorer(laby,"b",type)
            if gauche() != -1:
                
                position = pixel2cell(turtle.xcor(),turtle.ycor())
                if position[0] ==  sortie_line and position[1] ==sortie_colonne:
                    print("You have explored the game")
                    return
               
                explorer_mini(type,position,laby,lettre)
                return explorer(laby,"g",type)
        if lettre == "b": 
            if bas() != -1:
                position = pixel2cell(turtle.xcor(),turtle.ycor())
                if position[0] ==  sortie_line and position[1] ==sortie_colonne:
                    print("You have explored the game")
                    return
               
                explorer_mini(type,position,laby,lettre)
                return explorer(laby,"b",type)
            if gauche() != -1:
                position = pixel2cell(turtle.xcor(),turtle.ycor())
                if position[0] ==  sortie_line and position[1] ==sortie_colonne:
                     print("You have explored the game")
                     return
                explorer_mini(type,position,laby,lettre)
                return explorer(laby,"g",type)
            if droite() != -1:
                position = pixel2cell(turtle.xcor(),turtle.ycor())
                if position[0] ==  sortie_line and position[1] ==sortie_colonne:
                     print("You have explored the game")
                     return
                explorer_mini(type,position,laby,lettre)
                return explorer(laby,"d",type)
            if haut() != -1:
                position = pixel2cell(turtle.xcor(),turtle.ycor())
                if position[0] ==  sortie_line and position[1] ==sortie_colonne:
                     print("You have explored the game")
                     return
                explorer_mini(type,position,laby,lettre)
                return explorer(laby,"h",type)
        if lettre == "h": 
            if haut() != -1:
                position = pixel2cell(turtle.xcor(),turtle.ycor())
                if position[0] ==  sortie_line and position[1] ==sortie_colonne:
                    print("You have explored the game")
                    return
              
                explorer_mini(type,position,laby,lettre)
                return explorer(laby,"h",type)
            if gauche() != -1:
                position = pixel2cell(turtle.xcor(),turtle.ycor())
                if position[0] ==  sortie_line and position[1] ==sortie_colonne:
                     print("You have explored the game")
                     return
                
                explorer_mini(type,position,laby,lettre)
                return explorer(laby,"g",type)
            if droite() != -1:
                position = pixel2cell(turtle.xcor(),turtle.ycor())
                if position[0] ==  sortie_line and position[1] ==sortie_colonne:
                     print("You have explored the game")
                     return
              
                explorer_mini(type,position,laby,lettre)
                return explorer(laby,"d","normal")
            if bas() != -1:
                position = pixel2cell(turtle.xcor(),turtle.ycor())
                if position[0] ==  sortie_line and position[1] ==sortie_colonne:
                     print("You have explored the game")
                     return
              
                explorer_mini(type,position,laby,lettre)
                return explorer(laby,"b","normal")
    return


xclick = 0
yclick = 0
def getcoordinates():
    turtle.onscreenclick(testClic) 

def testClic(x,y):
    global xclick
    global yclick
    global dicojeu
    xclick = int(x//1)
    yclick = int(y//1)
    xclick = (xclick - dicoJeu["coordx"])/24
    yclick = (dicoJeu["coordy"]-yclick)/24
    colonne = xclick
    line = yclick
    if line<0 or colonne<0 or line >11 or colonne > 15:
        print("outside bounds")
    else:
        print(int(line))
        print(int(colonne))




wn = turtle.Screen()
wn.title("Turtle")
wn.bgcolor("black")
wn.setup(width=800, height = 600)


class RivalTurtle(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        
        self.color("yellow")
        self.penup()
        self.speed(0)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)        

def afficheGraphique(laby,coordx,coordy):
  
    dicoJeu["coordx"]  = coordx + -1*(len(laby[0])*12)
    dicoJeu["coordy"] = coordy + (len(laby)*12)
    print(dicoJeu)
    for y in range(len(laby)):
        for x in range(len(laby[y])):
            number = laby[y][x]
            
            screen_x = -1*(len(laby[0])*12) + (x*24) + coordx
            screen_y = (len(laby)*12) - (y *24)+ coordy
            if number == 0:
                pen.goto(screen_x,screen_y)
                pen.stamp()
            if ( x == dicoJeu["sortie"][1] and y == dicoJeu["sortie"][0]) or (x == dicoJeu["entre"][1] and  y == dicoJeu["entre"][0]):             
                pen.goto(screen_x,screen_y)
                pen.color("purple")
                pen.stamp()
                pen.color("white")
            if typeCellule(y,x,laby) == "carrefour":
                pen.goto(screen_x,screen_y)
                pen.color("red")
                pen.stamp()
                pen.color("white")
                
def typeCellule(ligne,colonne,laby):
    counter = 0
    if ligne<0 or colonne <0 or ligne>len(laby)-1 or colonne > len(laby[0])-1:
        return "outside"
    if laby[ligne][colonne] == 1:
        return "mur"   
    if (ligne == dicoJeu["sortie"][0] and colonne == dicoJeu["sortie"][1]):
        return "sortie"    
    elif (ligne == dicoJeu["entre"][0] and  colonne == dicoJeu["entre"][1]):
        return "entre"
   
    else:
       
    
        if ligne< len(laby)-1:
            if colonne<len(laby[ligne])-1:
                
                    if laby[ligne][colonne] == 0:
                        counter= counter + 1
                    if laby[ligne+1][colonne] == 0:   
                       counter= counter + 1  
                    if laby[ligne][colonne+1] == 0:
                        counter= counter + 1    
                    if laby[ligne][colonne-1] == 0:
                        counter= counter + 1  
                    
                    if laby[ligne-1][colonne] == 0 :
                        counter= counter + 1  
                    
                    
    if  counter == 4:
            return "carrefour"
    elif counter == 3:
            return "passage standard"
                
    elif counter == 2:
            return "impasse"
            
def pixel2cell(x,y):
    
    ligne = int((dicoJeu["coordy"]-y)  / 24)
    colonne =  int((x -dicoJeu["coordx"]) / 24)
    return  [ligne,colonne]
    
    
def cell2pixel(i,j):
    x = j*24 + dicoJeu["coordx"]
    y =  dicoJeu["coordy"] - i*24
 
    return [x,y]
    

afficheLisible()
pen = Pen()
afficheGraphique(LABY_DECIDER,0,0)  

turtle.left(90)
turtle.penup()
turtle.shape("turtle")
turtle.color("blue")

start = cell2pixel(dicoJeu["entre"][0],dicoJeu["entre"][1])
turtle.goto(start[0], start[1])
getcoordinates()          
explorer(LABY_DECIDER,"d","normal")



turtle.mainloop()

