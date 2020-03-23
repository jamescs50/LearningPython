import tkinter as tk
import random

TilePos = dict()
Tiles = []
EmptyTile = tuple()
MoveCount = 0
root = tk.Tk()

#class Tile(tk.Button):
#    number = 0


#returns 15 numbers in a random order
def RandSeq():
    nums=[]
    numsout=[]
    for i in range(15):
        nums.append(i+1)

    for i in range(15):
        j = random.choice(nums)
        numsout.append(j)
        nums.remove(j)
    return numsout    

#makes actions for each button as they are generated. 
def MakeAction(nin):
    def Action(n=nin):
        #print([n])
        MoveButtons(n)
    return Action

def MoveButtons(bno):
    global Tiles
    global TilePos
    global EmptyTile
    global MoveCount
    btnpos = TilePos.get(bno)
    
    #print(btnpos)
    #print(EmptyTile)
    if not is_adjacent(btnpos,EmptyTile):
        return
    EmptyTile,btnpos = btnpos,EmptyTile #swap positions
    #print(btnpos)
    #print(TilePos)
    #TilePos.[bno] = btnpos
    TilePos.update({bno:btnpos})
    for t in Tiles:
        if t.number == bno:
            t.grid(row=btnpos[0], column=btnpos[1])
    MoveCount += 1
    TestWin()



def TestWin():
    b=0
    for r in range(4):
        for c in range(4):
            if b != 15:
                b+=1
                if TilePos.get(b) != (r,c):
                    return(False)
    WinMessage = tk.Label('Completed in ' + str(MoveCount) + ' moves')
    WinMessage.grid(row=4,column=0)

def is_adjacent(posa,posb):
    if ((abs(posa[0] - posb[0]) == 1) and (posa[1] == posb[1])):
        return(True)
    if ((posa[0] == posb[0]) and (abs(posa[1] - posb[1]) == 1)):
        return(True)
    return False      


shuffle = []
shuffle = RandSeq()

b = 0
for r in range(4):
    for c in range(4):
        if b != 15:
            b += 1
            n = shuffle[b-1]
            B =tk.Button(root,text=n,command= MakeAction(n))
            B.number = n            
            B.grid(row=r,column=c)
            Tiles.append(B)
            TilePos[n]= (r,c)

EmptyTile = (3,3)

#print(str(TilePos))

root.mainloop()