# Name    : MA20_2048
# Authors : Eldan Suljic
# Date    : 05.03.2026
# Version : 0.02
# ------import------------
import random
from hmac import digest_size
from tkinter import *
from tkinter import messagebox

from core import *
from random import *

# ----variable------
winn= 0
dx = 10
dy = 10
game2 = [[1024, 1024, 0, 0],
        [0, 0, 2, 0],
        [0, 0, 0, 0],
        [2, 0, 0, 0]]

game = [[4, 2, 4, 8],
            [16, 32, 64, 128],
            [256, 512, 1024, 4096],
            [4096, 8192, 8, 8]]

labels = [[None, None, None, None],
          [None, None, None, None],
          [None, None, None, None],
          [None, None, None, None]]

colors = {
    0: "#758073",
    2: "#2EE809",
    4: "#1E8C08",
    8: "#0D4B01",
    16: "#01306D",
    32: "#004AAA",
    64: "#019EFF",
    128: "#FF4AB6",
    256: "#AA0094",
    512: "#6C0381",
    1024: "#79040F",
    2048: "#C3030C",
    4096: "#FF4A4D",
    8192: "#F06400"

}


# ---------fonction--------

#---------foction posibiliter de mouvement
#on regarde si il y a des posibiliter de mouvement
def check():
    global game
    for row in range(4):
        for col in range(3):
            #la deux case l'un en dessous de l'autre son verifier
            if game[row][col] == game[row][col + 1]:
                return False
    for row in range(3):
        for col in range(4):
            #la l'une a coter de l'autre
            if game[row][col] == game[row + 1][col]:
                return False
    return True

#----------fonction tableau plein-------------
def FullGame():
    global game
    for row in range(4):
        for col in range(4):
            #la est verifier si il y a des case vide
            if game[row][col] == 0:
                return False
    return True

#---------fonction jeux et fini---------
def winngame():
    global winn
    for row in range(4):
        for col in range(4):
            #on regarde si il y a un 2048 et on fais qu'une fois le gagner
            if game[row][col] == 2048:
                winn += 1
                if winn == 1:
                    messagebox.showinfo("Gagné", "Tu as gagné!")

#-------fonction pour ajouter une tuille randome ------
def add():
    global game
#calcule et mise du nombre de zero dans une variable
    null_table = []
    for row in range(4):
        for col in range(4):
            if game[row][col] == 0:
                null_table.append((row, col))
#mettre dans la variable et chois de la case
    row, col = choice(null_table)
    game[row][col] = choice([2,2,2,2,4])

#---------la fonction pour changer les tuile -----------------
def display():
    for line in range(len(game)):
        for col in range(len(game[line])):
            if game[line][col] > 0:
                labels[line][col].config(bg=colors[game[line][col]],text=game[line][col],fg="white")
            else:
                labels[line][col].config(bg=colors[game[line][col]],text="")
#-----changement de la taile de la police------------
            if game[line][col] > 100:
                labels[line][col].config(font=("Arial", 20),width=6, height=3)
            else:
                labels[line][col].config(font=("Arial", 31),width=4, height=2)


#--------- dans chaque def on vas positioner les numero dans le bon sense ----------
#exemple pour le def down on commence 3 et on fini par 0 pour faire que ca dessende
#et on sort le nobre de mouvement pour voir si il y a du deplacement ou pas
def down(event):
    total_moves = 0
    for col in range (4):
        (game[3][col],game[2][col],game[1][col],game[0][col],nmove) = pack4(game[3][col],game[2][col],game[1][col],game[0][col])
        total_moves += nmove
    print(total_moves)
    if total_moves > 0:
        add()
#la on n'affiche le resultat et gagner si on n'est a 2048
        display()
        winngame()
    display()
# ici on verifie si le tableau peux faire des mouvement et et plein pour dire si on n'as perdu
    if FullGame() ==True and check() == True:
        messagebox.showinfo("Perdu", "Tu as perdu! Dommage tu feras mieu la prochaine fois.")
    return total_moves



def left(event):
    total_moves = 0
    for line in range (4):
        (game[line][0],game[line][1],game[line][2],game[line][3],nmove) =pack4(game[line][0],game[line][1],game[line][2],game[line][3])
        total_moves += nmove
    print(total_moves)
    if total_moves != 0:
        add()
        display()
        winngame()
    display()
    if FullGame() ==True and check() == True:
        messagebox.showinfo("Perdu", "Tu as perdu! Dommage tu feras mieu la prochaine fois.")
    return total_moves


def right(event):
    total_moves = 0
    for line in range (4):
        (game[line][3],game[line][2],game[line][1],game[line][0],nmove) =pack4(game[line][3],game[line][2],game[line][1],game[line][0])
        total_moves += nmove
    print(total_moves)
    if total_moves != 0:
        add()
        display()
        winngame()
    display()
    if FullGame() ==True and check() == True:
        messagebox.showinfo("Perdu", "Tu as perdu! Dommage tu feras mieu la prochaine fois.")
    return total_moves



def up(event):
    total_moves = 0
    for col in range (4):
        (game[0][col],game[1][col],game[2][col],game[3][col],nmove) =pack4(game[0][col],game[1][col],game[2][col],game[3][col])
        total_moves += nmove
    print(total_moves)
    if total_moves != 0:
        add()
        display()
        winngame()
    display()
    if FullGame() ==True and check() == True:
        messagebox.showinfo("Perdu", "Tu as perdu! Dommage tu feras mieu la prochaine fois.")
    return total_moves

# ----------programe-principale------------
# --l'écrant----
window = Tk()
window.geometry("800x800")
window.config(bg="#141414")
# -----------titre et score-----------

titleFrame = Frame(window)
titleFrame.config(bg="#141414")
titleFrame.pack(anchor="nw", pady=50)

label_score = Label(titleFrame, text="Score:", fg="#008819")
label_score.config(height=4, width=13, bg="#D9D9D9")
label_score.pack(side="left", padx=50)


label_best_score = Label(titleFrame, text="meilleur Score:", fg="#008819")
label_best_score.config(height=4, width=13, bg="#D9D9D9")
label_best_score.pack(side="left", padx=0)

label_title = Label(titleFrame, text="2048")
label_title.config(bg="#141414", fg="white", font=("arial", 50,))
label_title.pack(side="left", padx=100)
# ----------------bouton---------------
quitbutton = Button(titleFrame, text="Quitter", command=window.quit)
quitbutton.config(bg="#399626", fg="white", height=1, width=15, relief="flat")
quitbutton.pack(pady=10)

replaybutton = Button(titleFrame, text="Rejouer")
replaybutton.config(bg="#399626", fg="white", height=1, width=15, relief="flat")
replaybutton.pack()
# -------------boucle for-----------------
# ici on crée la frame du font
frameglobal = Frame(window, bg="#444444")
frameglobal.pack(side="left", padx=100)
for line in range(len(game)):
    framejeux = Frame(frameglobal, bg="#444444")
    framejeux.pack()

    # la on fais les label pour les tuile
    for col in range(len(game[line])):
        labels[line][col] = Label(framejeux, width=4, height=2,font=("Arial", 30))
        labels[line][col].pack(side="left", padx=dx, pady=dy)

# les touche son defini ici
window.bind("<Left>",left)
window.bind("<Right>",right)
window.bind("<Up>",up)
window.bind("<Down>",down)
window.bind("w",up)
window.bind("s",down)
window.bind("a",left)
window.bind("d",right)




display()
window.mainloop()



