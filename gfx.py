# Name    : MA20_2048
# Authors : Eldan Suljic
# Date    : 05.03.2026
# Version : 0.02
# ------import------------

from tkinter import *
from core import *

# ----variable------
dx = 10
dy = 10
game = [[2, 0, 0, 0],
        [0, 0, 2, 0],
        [0, 0, 0, 0],
        [2, 0, 0, 0]]

game2 = [[0, 2, 4, 8],
            [16, 32, 64, 128],
            [256, 512, 1024, 2048],
            [4096, 8192, 0, 0]]

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

#----- dans chaque def on vas positioner les numero dans le bon sense ---
#----- et on sort le nobre de mouvement pour voir si il y a du deplacement ou pas ---
def down(event):
    total_moves = 0
    for col in range (4):
        (game[3][col],game[2][col],game[1][col],game[0][col],nmove) = pack4(game[3][col],game[2][col],game[1][col],game[0][col])
        total_moves += nmove
    print(total_moves)
    display()


def left(event):
    total_moves = 0
    for line in range (4):
        (game[line][0],game[line][1],game[line][2],game[line][3],nmove) =pack4(game[line][0],game[line][1],game[line][2],game[line][3])
        total_moves += nmove
    print(total_moves)
    display()

def right(event):
    total_moves = 0
    for line in range (4):
        (game[line][3],game[line][2],game[line][1],game[line][0],nmove) =pack4(game[line][3],game[line][2],game[line][1],game[line][0])
        total_moves += nmove
    print(total_moves)
    display()


def up(event):
    total_moves = 0
    for col in range (4):
        (game[0][col],game[1][col],game[2][col],game[3][col],nmove) =pack4(game[0][col],game[1][col],game[2][col],game[3][col])
        total_moves += nmove
    print(total_moves)
    display()







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



