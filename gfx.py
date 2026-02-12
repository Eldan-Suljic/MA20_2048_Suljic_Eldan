# Name    : MA20_2048
# Authors : Eldan Suljic
# Date    : 12.02.2026
# Version : 0.01
# ------import------------

from tkinter import *


# ----variable------
dx = 10
dy = 10
game = [[0, 0, 0, 0],
        [0, 0, 2, 0],
        [0, 0, 0, 0],
        [2, 0, 0, 0]]

game = [[0, 2, 4, 8],
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
                labels[line][col].config(bg=colors[game[line][col]],text=game[line][col],font=("Arial", 20),fg="white")
            else:
                labels[line][col].config(bg=colors[game[line][col]],text="")


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
for line in range(len(game)):
    framejeux = Frame(window, bg="#444444")
    framejeux.pack()
    #ici on crée la frame du font

    for col in range(len(game[line])):
        labels[line][col] = Label(framejeux, width=6, height=3,font=("Arial", 20))
        labels[line][col].pack(side="left", padx=dx, pady=dy)
        #la on fais les label pour les tuile


display()
window.mainloop()



