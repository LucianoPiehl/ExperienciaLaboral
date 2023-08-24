from tkinter import *
ventana = Tk()
ventana.title("Agregar cuenta")
ventana.resizable(False, False)
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()
width, height = 300, 300
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
ventana.geometry("%dx%d+%d+%d" % (width, height, x, y))
ventana.columnconfigure(1, weight=1)
username = Entry(ventana, font=("Calibri 10"), width=35)
username.insert(0, "Ingrese su nombre de usuario")
username.grid(row=0, column=1, columnspan=2, padx=25, pady=35, sticky="nsew")

def on_focusin_user(event):
    if username.get() == "Ingrese su nombre de usuario":
        username.delete(0, END)

username.bind("<FocusIn>", on_focusin_user)

password = Entry(ventana, font=("Calibri 10"), width=35)
password.insert(0, "Ingrese su contraseña")
password.grid(row=1, column=1, columnspan=2, padx=25, pady=15, sticky="nsew")
def on_focusin_pass(event):
    if password.get() == "Ingrese su contraseña":
        password.delete(0, END)

password.bind("<FocusIn>", on_focusin_pass)
BotonInicioSesion = Button(ventana, text="Iniciar Sesion", width=15, height=2)
BotonInicioSesion.grid(row=3, column=1, columnspan=2, padx=35, pady=10, sticky="nsew")
def save_credentials():
    global username_value, password_value
    username_value = username.get()
    password_value = password.get()
    if username_value == "" or username_value == "Ingrese su usuario" or password_value == "" or password_value == "Ingrese su contraseña":
        quit()
    with open("cuentas.txt", 'a', encoding="utf-8") as file:
        file.write(f'USERNAME={username_value};PASSWORD={password_value}\n')
    if password.get() == password_value:
        password.delete(0, END)
        password.insert(0, "Ingrese su contraseña")
    if username.get() == username_value:
        username.delete(0, END)
        username.insert(0, "Ingrese su usuario")
    ventana.quit()
BotonInicioSesion.config(command=save_credentials)
ventana.mainloop()
