from tkinter import StringVar  
from tkinter import DoubleVar 
from tkinter import Label
from tkinter import Entry
from tkinter import ttk
from tkinter import Button
from tkcalendar import DateEntry

from modelo import alta
from modelo import consultar
from modelo import borrar



def vista_principal(root):

    root.title("Registro de tickets")
            
    titulo = Label(root, text="Ingrese", bg="DarkOrchid3", fg="thistle1", height=1, width=60)
    titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky="w")

    ticket = Label(root, text="Ticket")
    ticket.grid(row=1, column=0, sticky="w")
    estado=Label(root, text="Estado")
    estado.grid(row=2, column=0, sticky="w")
    fecha=Label(root, text="Fecha")
    fecha.grid(row=3, column=0, sticky="w")

    # Defino variables para tomar valores de campos de entrada
    a_val, b_val, c_val = StringVar(), StringVar(), StringVar()
    w_ancho = 20

    entrada1 = Entry(root, textvariable = a_val, width = w_ancho) 
    entrada1.grid(row = 1, column = 1)
    entrada2 = ttk.Combobox(root, values=["Aprobado", "En proceso", "Cerrado", "Terminado"], textvariable = b_val, width = w_ancho)
    entrada2.grid(row = 2, column = 1)
    entrada3 = DateEntry(root, selectmode='day', textvariable = c_val, width = w_ancho) 
    entrada3.grid(row = 3, column = 1)

    # --------------------------------------------------
    # TREEVIEW
    # --------------------------------------------------

    tree = ttk.Treeview(root)
    tree["columns"]=("col1", "col2", "col3")
    tree.column("#0", width=90, minwidth=50, anchor="w")
    tree.column("col1", width=200, minwidth=80)
    tree.column("col2", width=200, minwidth=80)
    tree.column("col3", width=200, minwidth=80)
    tree.heading("#0", text="ID")
    tree.heading("col1", text="Producto")
    tree.heading("col2", text="cantidad")
    tree.heading("col3", text="precio")
    tree.grid(row=10, column=0, columnspan=4)

    boton_alta=Button(root, text="Alta", command=lambda:alta(a_val.get(), b_val.get(), c_val.get(), tree))
    boton_alta.grid(row=6, column=1)

    boton_consulta=Button(root, text="Consultar", command=lambda:consultar())
    boton_consulta.grid(row=7, column=1)

    boton_borrar=Button(root, text="Borrar", command=lambda:borrar(tree))
    boton_borrar.grid(row=8, column=1)

    # boton_borrar=Button(root, text="Modificar", command=lambda:update(tree))
    # boton_borrar.grid(row=8, column=1)