from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Ejercicio desafio - Unidad 1: GUI ")
root.geometry('300x300')

mi_id = 0
var_title = StringVar()
var_description = StringVar()
var_ruta = StringVar()

item=Label(root,text="Ingrese sus datos")
item.grid(row=0,column=1)

title = Label(root, text="Titulo")
title.grid(row=0, column=0, sticky= W)

description = Label(root, text="Descripcion")
description.grid(row=2, column=0, sticky= W)

ruta = Label(root, text="Ruta")
ruta.grid(row=1, column=0, sticky= W)

entry_title = Entry(root, textvariable=var_title, width=25, )
entry_title.grid(row=0, column=1)

entry_description = Entry(root, textvariable=var_description, width=25)
entry_description.grid(row=1, column=1)

entry_ruta= Entry(root, textvariable=var_ruta, width=25)
entry_ruta.grid(row=2, column=1)

def funtion_g():
    global mi_id
    mi_id += 1
    print(entry_title.get() + ' ' + entry_ruta.get() + ' ' + entry_description.get())
    tree.insert("", "end", text=str(mi_id), values=(var_title.get(), var_description.get(), var_ruta.get()))

def funtion_d():
    root.configure(background="red")

tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2", "col3")
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.column("col1", width=80, minwidth=80, anchor=W)
tree.column("col2", width=80, minwidth=80, anchor=W)
tree.column("col3", width=100, minwidth=100, anchor=W)

tree.grid(column=0, row=4, columnspan=4)

botom_g = Button(root, text="Alta", command=funtion_g)
botom_g.grid(row=3, column=1)

botom_delete = Button(root, text="Sorpresa", command=funtion_d)
botom_delete.grid(row=3, column=2)


root.mainloop()