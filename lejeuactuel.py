
# -----------------* MEMORY : MEME EDITION by YASSINE *----------------- #
 

from tkinter import *
from random import shuffle


# définir la taille des cartes + nbr de col/lig

COTE = 120
PAD = 5
SIDE = COTE + PAD

NB_LIG = 4
NB_COL = 5

LARG = SIDE * NB_COL
HAUT = SIDE * NB_LIG
X0 = Y0 = SIDE // 2

NB_CARTES=NB_LIG*NB_COL//2

MEME=['banane', 'bob', 'carlos', 'garcon','homer', 'kermit', 'NyanCat',
      'poney', 'saltbae', 'xbg93']


# mélanges des cartes

def melanger_grille():
    cartes=list(range(NB_CARTES))*2
    shuffle(cartes)

    P=[]
    k=0
    for lig in range(NB_LIG):
        L=[]
        for col in range(NB_COL):
            L.append(cartes[k])
            k+=1
        P.append(L)
        
    return P


#fenêtre 

fen = Tk()
cnv = Canvas(fen, width=LARG, height=HAUT, bg='#6a95a5')
cnv.pack()

cover = PhotoImage(file="./images/carte.png")
plateau=melanger_grille()


# LOGOS

logos=[]

for meme in MEME:
    fichier="./images/" + meme +  ".png"
    logo=PhotoImage(file=fichier)
    logos.append(logo)
cover=PhotoImage(file="./images/carte.png")
ids_cover=[]
    

# PLACEMENT DES IMAGES

for lig in range(NB_LIG):
    L=[]
    for col in range(NB_COL):
        centre = (X0 + col * SIDE, Y0 + lig * SIDE)
        i=plateau[lig][col]
        logo=logos[i]
        nro=plateau[lig][col]
        logo=logos[nro]
        cnv.create_image(centre, image=logo)
        id_cover=cnv.create_image(centre, image=cover)
        L.append(id_cover)
    ids_cover.append(L)


# clique unique de la souris
    
move=[None, None]

def clic(event):
    if move[1] is not None:
        return
    X=event.x
    Y= event.y
    col=X//SIDE
    lig=Y//SIDE
    if plateau[lig][col]!=-1:
        traiter_clic(lig, col)

def traiter_clic(lig, col):
    item=ids_cover[lig][col]
    cnv.delete(item)
    if move[0] is None:
        move[0]=(lig, col)
    else:
        if move[0]==(lig, col):
            return
        move[1]=(lig, col)
        i, j=move[0]
        if plateau[i][j]==plateau[lig][col]:
            plateau[i][j]=plateau[lig][col]=-1
            move[0]=move[1]=None
        else:
            cnv.after(400, cacher, i,j, lig, col)

def cacher(i, j, lig, col):
    centre = (X0 + j * SIDE, Y0 + i * SIDE)
    ids_cover[i][j]=cnv.create_image(centre, image=cover)
    centre = (X0 + col * SIDE, Y0 + lig * SIDE)
    ids_cover[lig][col]=cnv.create_image(centre, image=cover)

    move[0]=move[1]=None
    
        
 
cnv.bind("<Button>", clic)




fen.mainloop()
 
















