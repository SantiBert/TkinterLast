from tkinter import *

window = Tk()
window.geometry('600x500')
window.title('Productos')
window.resizable(0, 0)


def home():
    home_label = Label(window, text='Inicio')
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=160,
        pady=20,
    )
    home_label.grid(row=0, column=0)
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()

    return True


def add():
    add_label = Label(window, text='Añadir producto')
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=60,
        pady=20,
    )

    add_label.grid(row=0, column=0, columnspan=10)
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
    add_price_label.grid(row=2, column=0, padx=5, pady=5)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
    add_description_label.grid(row=3, column=0, padx=5, pady=5)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_separator.grid(row=4, column=1, sticky=E)
    boton.grid(row=5, column=1, sticky=NW)
    boton.config(
        fg="white",
        bg="green",
        padx=15,
        pady=5,
    )

    home_label.grid_remove()
    info_label.grid_remove()
    return True


def info():
    info_label = Label(window, text='Información')
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=100,
        pady=20,
    )
    info_label.grid(row=0, column=0)
    home_label.grid_remove()
    add_frame.grid_remove()
    add_label.grid_remove()

    return True


# Imputs de productos:
name_data = StringVar()
price_data = StringVar()

# Campos de pantallas
home_label = Label(window, text='Inicio')
add_label = Label(window, text='Añadir')
info_label = Label(window, text='Información')

# Campos de formulario
add_frame = Frame(window)

add_name_label = Label(add_frame, text='Nombre del producto: ')
add_name_entry = Entry(add_frame, textvariable=name_data)
add_price_label = Label(add_frame, text='Precio del producto: ')
add_price_entry = Entry(add_frame, textvariable=price_data)
add_description_label = Label(add_frame, text='Descripción del producto: ')
add_description_entry = Entry(add_frame)
add_separator = Label(add_frame)

boton = Button(add_frame, text='Guarda')

# Cargar pantalla de inicio
home()

# Menu superior
hight_menu = Menu(window)
hight_menu.add_command(label="Inicio", command=home)
hight_menu.add_command(label="Añadir", command=add)
hight_menu.add_command(label="Información", command=info)
hight_menu.add_command(label="Salir", command=window.quit)

# Cargar menu superior
window.config(menu=hight_menu)

window.mainloop()
