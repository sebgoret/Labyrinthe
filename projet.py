#!/usr/bin/env python3

from tkinter import *
from time import sleep
import sys, os.path
import random

class Labyrinthe():
    def __init__(self, largeur, hauteur):
        self.fenetre = Tk()
        self.width=largeur
        self.height=hauteur
        self.graph=Canvas(width=largeur+100, height=hauteur, bg='lightyellow')
        self.graph.pack()
        self.murs=[]
        self.obstacles=[]
        self.objets=[]
        self.parcours=[]
        self.fenetre.bind_all("<Key>", self.onKeyPressed)
        
    
    def afficher(self):
        s=''
        for d,x1,y1,x2,y2 in self.parcours:
            s+=d
            if d=='G' or d=='*G':
                liste.append(self.graph.create_line(x1+11,y1+10,x1-39,y1+10, width=2, fill='red'))
            if d=='D' or d=='*D':
                liste.append(self.graph.create_line(x1+11,y1+10,x2+41,y1+10, width=2, fill='red'))
            if d=='H' or d=='*H':
                liste.append( self.graph.create_line(x1+11,y1+10,x1+11,y1-40, width=2, fill='red'))
            if d=='B' or d=='*B':
                liste.append(self.graph.create_line(x1+11,y1+10,x1+11,y2+40, width=2, fill='red'))
        print(s)
        aff.config(text="Cacher parcours", command=self.cacher)

    def cacher(self):
        for l in liste:
            self.graph.delete(l)
        aff.config(text="Afficher parcours", command=self.afficher)
            

    def deplacer(self, s):
        l=self.graph.coords(self.objets[0].point)
        if s=='G':
            self.objets[0].direction='G'
            if(l[0]-15,l[1]-15,l[2]-35,l[3]+15) in self.murs or (l[0]-15,l[1]-15,l[2]-35,l[3]+15) in self.obstacles:
                print("pas possible")
                return 42
            else:
                if l[0]-15==0:
                    pass
                else:
                    self.parcours.append(('G', l[0], l[1], l[2], l[3]))
                    self.graph.move(self.objets[0].point,-50,0)
        if s=='H':
            self.objets[0].direction='H'
            if (l[0]-15,l[1]-15,l[2]+15,l[3]-35) in self.murs or (l[0]-15,l[1]-15,l[2]+15,l[3]-35) in self.obstacles:
                print("pas possible")
                return 42
            else:
                if l[1]-15==0:
                    pass
                else:
                    self.parcours.append(('H', l[0], l[1], l[2], l[3]))
                    self.graph.move(self.objets[0].point,0,-50)
        if s=='B':
            self.objets[0].direction='B'
            if (l[0]-15,l[1]+35,l[2]+15,l[3]+15) in self.murs or (l[0]-15,l[1]+35,l[2]+15,l[3]+15) in self.obstacles:
                print("pas possible")
                return 42
            else:
                if l[3]+15==self.height:
                    pass
                else:
                    self.parcours.append(('B', l[0], l[1], l[2], l[3]))
                    self.graph.move(self.objets[0].point,0,+50)
        if s=='D':
            self.objets[0].direction='D'
            if (l[0]+35,l[1]-15,l[2]+15,l[3]+15) in self.murs or (l[0]+35,l[1]-15,l[2]+15,l[3]+15) in self.obstacles:
                print("pas possible")
                return 42
            else:
                if l[2]+15==self.width:
                    pass
                else:
                    self.parcours.append(('D', l[0], l[1], l[2], l[3]))
                    self.graph.move(self.objets[0].point,+50,0)

    def reset(self):
        self.parcours=[]
        point = Point (self, self.objets[0].x_initial, self.objets[0].y_initial)
        self.graph.delete(self.objets[0].point)
        self.objets[0]=point
        self.graph.update()
    
    
    def onKeyPressed(self, k):
        if(k.keysym=='q' or k.keysym=='Left'):
            self.deplacer('G')
        if(k.keysym=='z' or k.keysym=='Up'):
            self.deplacer('H')
        if(k.keysym=='s' or k.keysym=='Down'):
            self.deplacer('B')
        if(k.keysym=='d' or k.keysym=='Right'):
            self.deplacer('D')
        if(k.keysym=='Escape'):
            self.fenetre.quit()
        if(k.char==' '):
            self.objets[0].sauter()


class Point():
    def __init__(self, laby, x, y):
        self.laby = laby
        self.graph = laby.graph
        self.x_initial = x
        self.y_initial = y
        self.x = x
        self.y = y
        self.point = self.graph.create_oval(x+15, y-35, x+35, y-15, fill='blue')
        self.direction = 'H'
        laby.objets.append(self)

    def sauter(self):
        l=self.graph.coords(self.point)
        if self.direction=='H':
            if (l[0]-15,l[1]-15,l[2]+15,l[3]-35) in self.laby.murs:
                print("pas possible")
                return 42
            else:
                if l[1]-15==0:
                    pass
                else:
                    self.laby.parcours.append(('*H', l[0], l[1], l[2], l[3]))
                    for a in range(0,50,10):
                        self.laby.fenetre.bind_all("<Key>", lambda e: None)
                        sleep(0.1)
                        if a<30:
                            self.graph.move(self.point, -10, -10)
                            self.graph.update()
                        else:
                            self.graph.move(self.point, +15, -10)
                            self.graph.update()
                            self.laby.fenetre.bind_all("<Key>", self.laby.onKeyPressed)
        if  self.direction=='B':
            if (l[0]-15,l[1]+35,l[2]+15,l[3]+15) in self.laby.murs:
                print("pas possible")
                return 42
            else:
                if l[3]+15==self.laby.height:
                    pass
                else:
                    self.laby.parcours.append(('*B', l[0], l[1], l[2], l[3]))
                    for a in range(0,50,10):
                        self.laby.fenetre.bind_all("<Key>", lambda e: None)
                        sleep(0.1)
                        if a<30:
                            self.graph.move(self.point, -10, +10)
                            self.graph.update()
                        else:
                            self.graph.move(self.point, +15, +10)
                            self.graph.update()
                            self.laby.fenetre.bind_all("<Key>", self.laby.onKeyPressed)
        if self.direction=='G':
            if(l[0]-15,l[1]-15,l[2]-35,l[3]+15) in self.laby.murs:
                print("pas possible")
                return 42
            else:
                if l[0]-15==0:
                    pass
                else:
                    self.laby.parcours.append(('*G', l[0], l[1], l[2], l[3]))
                    for a in range(0,50,10):
                        self.laby.fenetre.bind_all("<Key>", lambda e: None)
                        sleep(0.1)
                        if a<30:
                            self.graph.move(self.point, -10, -10)
                            self.graph.update()
                        else:
                            self.graph.move(self.point, -10, +15)
                            self.graph.update()
                            self.laby.fenetre.bind_all("<Key>", self.laby.onKeyPressed)
        if self.direction=='D':
            if (l[0]+35,l[1]-15,l[2]+15,l[3]+15) in self.laby.murs:
                print("pas possible")
                return 42
            else:
                if l[2]+15==self.laby.width:
                    pass
                else:
                    self.laby.parcours.append(('*D', l[0], l[1], l[2], l[3]))
                    for a in range(0,50,10):
                        self.laby.fenetre.bind_all("<Key>", lambda e: None)
                        sleep(0.1)
                        if a<30:
                            self.graph.move(self.point, +10, -10)
                            self.graph.update()
                        else:
                            self.graph.move(self.point, +10, +15)
                            self.graph.update()
                            self.laby.fenetre.bind_all("<Key>", self.laby.onKeyPressed)


def genere_lab(laby):
    
    x = 50
    y = 50
    p_x = 0
    p_y = 0
    for i,ligne in enumerate(lignes):
        s=''
        if i%2==0:
            for e in ligne:
                if e=='1':
                    laby.graph.create_line(x, y, x+50, y, width=2)
                    laby.murs.append((x, y, x+50, y))
                    x+=50
                    s+='---'
                if e=='0':
                    x+=50
                    s+='   '
                if e=='E':
                    p_x=x
                    p_y=y
                    laby.graph.create_line(x, y-50, x, y, fill='lightyellow')
                    laby.graph.create_line(x+50, y-50, x+50, y, fill='lightyellow')
                    laby.murs.append((x,y-50,x,y))
                    laby.murs.append((x+50,y-50,x+50,y))
                    x+=50
                    s+=' E '
                if e=='O':
                    laby.graph.create_line(x, y, x+50, y, width=2, fill='green')
                    laby.obstacles.append((x, y, x+50, y))
                    x+=50
                    s+=' O '
                if e=='\n':
                    x=50
                    y+=50
                    print(s)
        else:
            for e in ligne:
                if e=='1':
                    laby.graph.create_line(x, y, x, y-50, width=2)
                    laby.murs.append((x,y-50,x,y))
                    x+=50
                    s+='|  '
                if e=='0':
                    x+=50
                    s+='   '
                if e=='E':
                    p_x=x-50
                    p_y=y
                    laby.graph.create_line(x-50, y-50, x, y-50, fill='lightyellow')
                    laby.graph.create_line(x-50, y, x, y, fill='lightyellow')
                    laby.murs.append((x-50,y-50,x,y-50))
                    laby.murs.append((x-50,y,x,y))
                    x+=50
                    s+='E  '
                if e=='O':
                    laby.graph.create_line(x, y, x, y-50, width=2, fill='green')
                    laby.obstacles.append((x, y-50, x, y))
                    x+=50
                    s+=' O '
                if e=='\n':
                    x=50
                    print(s)
    point = Point(laby, p_x, p_y)

def random_lab(nom_fichier, choix):
    with open(nom_fichier) as fichier:
        texte=fichier.read()
        liste=texte.split('@')
        with open("temp.lab", 'w') as temp:
            if choix==0:
               temp.write(liste[0])
            else :
                temp.write(random.choice(liste))
            return "temp.lab"



def demo(nom_fichier):
    with open(nom_fichier) as fichier:
        demo=fichier.read().split(',')
        
        genere_lab(laby)
        s=''
        laby.graph.update()
        for elt in demo:
            laby.fenetre.bind_all("<Key>", lambda e: None)
            s+=elt+' -> '
            if elt=='B':
                laby.deplacer('B')
                sleep(0.3)
            if elt=='H':
                laby.deplacer('H')
                sleep(0.3)
            if elt=='G':
                laby.deplacer('G')
                sleep(0.3)
            if elt=='D':
                laby.deplacer('D')
                sleep(0.3)
            if '*' in elt:
                laby.objets[0].sauter()
            
            laby.graph.update()
        s+='Well Done !'
        print("Solution :\n"+s+"\n\nPress escape to leave.")
        laby.fenetre.bind_all("<Key>", laby.onKeyPressed)

#def IA():
#    sortie=False
#    genere_lab(laby)
#    laby.deplacer('B')
#    laby.deplacer('G')
#    while sortie==False:
#        deplacement_Ia('B')
#    laby.fenetre.bind_all("<Key>", laby.onKeyPressed)

#def deplacement_Ia(test):
#    l=laby.graph.coords(laby.objets[0].point)
#    sleep(0.3)
#    laby.fenetre.bind_all("<Key>", lambda e: None)
#    laby.graph.update()
    
#    if test=='B' :
#        while (l[0]-15,l[1]-15,l[2]-35,l[3]+15) in laby.murs:
#            if laby.deplacer('B')==42 and laby.objets[0].sauter()==42:
#                if (l[0]+35,l[1]-15,l[2]+15,l[3]+15) in laby.murs:
#                    deplacement_Ia('H')
#                else:
#                    deplacement_Ia('D')
#        deplacement_Ia('G')
        

#    if test=='D' :
#        while (l[0]-15,l[1]+35,l[2]+15,l[3]+15) in laby.murs:
#            if laby.deplacer('D')==42 and laby.objets[0].sauter()==42:
#                if (l[0]-15,l[1]-15,l[2]+15,l[3]-35) in laby.murs:
#                    deplacement_Ia('G')
#                else:
#                    deplacement_Ia('H')
#        deplacement_Ia('B')

 #   if test=='G' :
 #       while (l[0]-15,l[1]-15,l[2]+15,l[3]-35) in laby.murs:
 #           if laby.deplacer('G')==42 and laby.objets[0].sauter()==42:
 #               if (l[0]-15,l[1]+35,l[2]+15,l[3]+15) in laby.murs:
 #                   deplacement_Ia('D')
 #               else:
 #                   deplacement_Ia('B')
 #       deplacement_Ia('H')
            


#    if test=='H' :
#        while (l[0]+35,l[1]-15,l[2]+15,l[3]+15) in laby.murs:
#            if laby.deplacer('H')==42 and laby.objets[0].sauter()==42:
#                if (l[0]-15,l[1]-15,l[2]-35,l[3]+15) in laby.murs:
#                    deplacement_Ia('B')
#                else:
#                   deplacement_Ia('G')
#        deplacement_Ia('D')

#def update_fenetre(nom_fichier, laby):
    
#    with open(nom_fichier) as fichier:
#        lignes=fichier.readlines()
#        laby.hauteur=(len(lignes)//2+2)*50
#        laby.largeur=(len(lignes[0])+1)*50
#   print("TIMMY")
#   laby.graph.delete(ALL)
#   laby.graph.update()

if __name__=='__main__':
    
    liste=[]

    if len(sys.argv)>3:
        print("Trop d'arguments")
    elif len(sys.argv)>1:
        if sys.argv[1]=="-demo":
            if os.path.isfile(sys.argv[2]):
                print("Mode Démo :\n")
                
                with open(random_lab("map.lab", 0)) as fichier:
                    lignes=fichier.readlines()
                    hauteur=(len(lignes)//2+2)*50
                    largeur=(len(lignes[0])+1)*50
                    laby=Labyrinthe(largeur, hauteur)
                        
                aff = Button(laby.fenetre, text="Afficher parcours", command=laby.afficher)
                aff.pack(side=RIGHT)

                demo(sys.argv[2])
                laby.fenetre.mainloop()
            else:
                print("Le 2nd argument n'est pas un fichier")
        elif sys.argv[1]=="-IA":
            print("Mode IA :\n")
            #IA()
            print("IA en construction.. Bug a corriger")
        else:
            print("L'argument n'est pas reconnu")
    else:
        
        with open(random_lab("map.lab", 1)) as fichier:
            lignes=fichier.readlines()
            hauteur=(len(lignes)//2+2)*50
            largeur=(len(lignes[0])+1)*50
            laby=Labyrinthe(largeur, hauteur)
        
        aff = Button(laby.fenetre, text="Afficher parcours", command=laby.afficher)
        aff.pack(side=RIGHT)
        res = Button(laby.fenetre, text="Reset", command=laby.reset)
        res.pack(side=RIGHT)
        #switch = Button(laby.fenetre, text="Switch Labyrinthe", command=update_fenetre(random_lab("map.lab", 1),laby))
        #switch.pack(side=RIGHT)

        genere_lab(laby)
        laby.fenetre.mainloop()
