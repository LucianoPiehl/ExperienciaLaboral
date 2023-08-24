import tkinter as tk
import mysql.connector

# Conexión a la base de datos
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="linkedin"
)
cursor = cnx.cursor()

# Función para agregar usuario
def agregar():
    idusuario = entry_idusuario.get()
    carpeta = entry_carpeta.get()
    query = "INSERT INTO usuarios (idusuario, carpeta) VALUES (%s, %s)"
    cursor.execute(query, (idusuario, carpeta))
    cnx.commit()
    label_resultado.config(text="Usuario agregado exitosamente.")

# Función para modificar usuario
def modificar():
    idusuario = entry_idusuario.get()
    carpeta = entry_carpeta.get()
    query = "UPDATE usuarios SET carpeta = %s WHERE idusuario = %s"
    cursor.execute(query, (carpeta, idusuario))
    cnx.commit()
    label_resultado.config(text="Usuario modificado exitosamente.")

# Función para eliminar usuario
def eliminar():
    idusuario = entry_idusuario.get()
    query = "DELETE FROM usuarios WHERE idusuario = %s"
    cursor.execute(query, (idusuario,))
    cnx.commit()
    label_resultado.config(text="Usuario eliminado exitosamente.")

# Ventana principal
ventana = tk.Tk()
ventana.title("ABM Usuarios")

# Etiquetas
label_idusuario = tk.Label(ventana, text="ID Usuario")
label_carpeta = tk.Label(ventana, text="Carpeta")
label_resultado = tk.Label(ventana, text="")

# Entradas
entry_idusuario = tk.Entry(ventana)
entry_carpeta = tk.Entry(ventana)

# Botones
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar)
boton_modificar = tk.Button(ventana, text="Modificar", command=modificar)
boton_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar)

# Grilla
label_idusuario.grid(row=0, column=0)
entry_idusuario.grid(row=0, column=1)
label_carpeta.grid(row=1, column=0)
entry_carpeta.grid(row=1, column=1)
boton_agregar.grid(row=2, column=0)
boton_modificar.grid(row=2, column=1)
boton_eliminar.grid(row=2, column=2)
label_resultado.grid(row=3, column=0, columnspan=3)

# Iniciar ventana
ventana.mainloop()

