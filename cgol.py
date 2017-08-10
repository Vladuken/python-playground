# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 03:48:57 2017

@author: Vlad
"""

import tkinter

#creating window
root = tkinter.Tk()

#size
win_width = 1000
win_height =500

#cell size in pixels
cell_size = 10

#resize window 
win_width = win_width - win_width % cell_size
win_height = win_height - win_height % cell_size

#create button
btn = tkinter.Button(root, text="Step", width = 30,height = 3, command = step)
btn.pack()

#set size of window
root.geometry("{}x{}".format(win_width,win_height))

#create and pack(show) canvas
canv = tkinter.Canvas(root, width = win_width, height = win_height,bg = "white")
canv.pack()

#create cells
x_cells = win_width // cell_size
y_cells = win_height // cell_size

#drow cells
cell_matrix = []
for i in range(x_cells):
    cell_list = []
    for j in range(y_cells):
        cell = canv.create_rectangle(cell_size*i,cell_size*j,cell_size*(i+1),cell_size*(j+1),fill = "black")
        canv.itemconfig(cell,state = HIDDEN,tags = ("hidden","0"))
        cell_list.append(cell)
    cell_matrix.append(cell_list)

#show cell onclick
def draw_cell(e):
    x_cord = e.x//cell_size
    y_cord = e.y//cell_size
    canv.itemconfig(cell_matrix[x_cord][y_cord],state = NORMAL, tags =("visible","0") )
   
#checking for conditions
def check():
    #for every cell
    for i in range(x_cells):
        for j in range(y_cells):
            k = 0
            #check neighbors
            for i_neigh in range(-1,2):
                for j_neigh in range(-1,2):
                    if (i_neigh + i >= x_cells) or (j_neigh + j >= y_cells):
                        pass
                    else:
                        if canv.gettags(cell_matrix[i+i_neigh][j+j_neigh])[0] == "visible" and (i_neigh != 0 or j_neigh !=0):
                            k +=1
            #check rules for each cell
            current_tag = canv.gettags(cell_matrix[i][j])[0]
            if k == 3 and current_tag =="hidden":
                canv.itemconfig(cell_matrix[i][j], tags = (current_tag,"to_visible"))
            if k == 2 or k == 3 and current_tag == "visible":
                pass
            if k == 0 or k == 1 or k == 4 and current_tag == "visible":
                canv.itemconfig(cell_matrix[i][j], tags = (current_tag,"to_hidden"))
                

def redraw():
    for i in range(x_cells):
        for j in range(y_cells):
            if canv.gettags(cell_matrix[i][j])[1] == "to_visible":
                canv.itemconfig(cell_matrix[i][j], state = NORMAL, tags = ("visible","0"))
            if canv.gettags(cell_matrix[i][j])[1] == "to_hidden":
                canv.itemconfig(cell_matrix[i][j], state = HIDDEN, tags = ("hidden","0"))
            
def step():
    check()
    redraw()

    
#mousebinding
canv.bind("<Button-1>",draw_cell)

root.mainloop()