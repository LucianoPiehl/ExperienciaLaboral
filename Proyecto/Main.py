from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pyautogui
import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def añadir_cuenta():
    def obtener_nombre():
        nombre_cuenta = entry.get()
        try:
            with open("cookies.pkl", "rb") as f:
                cookies = pickle.load(f)
        except:
            cookies = {}

        driver = webdriver.Chrome()
        driver.get("https://www.instagram.com/")
        time.sleep(45)
        all_cookies = driver.get_cookies()
        cookies[nombre_cuenta] = all_cookies

        with open("cookies.pkl", "wb") as f:
            pickle.dump(cookies, f)
        driver.close()

        messagebox.showinfo("Cuenta añadida", "Cuenta añadida con éxito")
        window.destroy()

    window = tk.Tk()
    window.title("Añadir cuenta")

    tk.Label(window, text="Nombre de la cuenta").pack()
    entry = tk.Entry(window)
    entry.pack()
    tk.Button(window, text="Añadir", command=obtener_nombre).pack()
    window.mainloop()


def Comentarios():
    try:
        if selected_key == None:
            messagebox.showinfo("Cuenta no seleccionada", "La cuenta todavia no fue proporcionada")
            return
    except:
        messagebox.showinfo("Cuenta no seleccionada", "La cuenta todavia no fue proporcionada")
        return
    try:
        cuenta = selected_key
    except:
        messagebox.showinfo("Cuenta no seleccionada","Para utilizar esta funcion debe seleccionar una cuenta")
        return
    comment_window = Toplevel(ventana)
    comment_label = Label(comment_window, text="Ingrese el comentario que desea escribir:")
    comment_label.pack()
    comment_entry = Entry(comment_window)
    comment_entry.pack()
    url_label = Label(comment_window, text="Ingrese la url de la publicacion:")
    url_label.pack()
    url_entry = Entry(comment_window)
    url_entry.pack()
    submit_button = Button(comment_window, text="Enviar", command=lambda: submit_comment(comment_entry.get(), url_entry.get()))
    submit_button.pack()


def submit_comment(comentario, url):
    cuenta = selected_key
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com")
    try:
        with open("cookies.pkl", "rb") as f:
            cookies = pickle.load(f)
    except:
        print("No se pudo cargar el archivo de cookies.")
        return


    if cuenta not in cookies:
        print("La cuenta no existe o no tiene cookies guardadas.")
        return

    for cookie in cookies[cuenta]:
        if cookie['domain'] == ".instagram.com":
            try:
                driver.add_cookie(cookie)
            except Exception as e:
                print(e)

    driver.get("https://www.instagram.com")
    time.sleep(5)

    print("Iniciando sesion con las cookies de la cuenta: ", cuenta)
    time.sleep(5)
    try:
        driver.get(url)
    except:
        messagebox.showinfo("URL Invalida", "La URL proporcionada es invalida")
    time.sleep(14)
    wait = WebDriverWait(driver, 10)
    a = driver.find_elements(By.CLASS_NAME, "_abl-")
    a[2].click()
    time.sleep(4)
    pyautogui.typewrite(comentario)
    time.sleep(4)
    pyautogui.press('enter')
    time.sleep(4)


def ComentariosTodas():
    try:
        with open("cookies.pkl", "rb") as f:
            cookies = pickle.load(f)
            print(cookies)
    except:
        cookies = {}
    if cookies == {}:
        messagebox.showinfo("No hay cuentas", "No existen cuentas para utilizar")
        return

    comment_window = Toplevel(ventana)
    comment_label = Label(comment_window, text="Ingrese el comentario que desea escribir:")
    comment_label.grid(row=0, column=0)
    comment_entry = Entry(comment_window)
    comment_entry.grid(row=0, column=1)
    url_label = Label(comment_window, text="Ingrese la url de la publicacion:")
    url_label.grid(row=1, column=0)
    url_entry = Entry(comment_window)
    url_entry.grid(row=1, column=1)
    submit_button = Button(comment_window, text="Enviar", command=lambda: submit_comments_all(comment_entry.get(), url_entry.get()))
    submit_button.grid(row=2, column=1)


def submit_comments_all(comentario, url):
    try:
        with open("cookies.pkl", "rb") as f:
            cookies = pickle.load(f)
    except:
        print("No se pudo cargar el archivo de cookies.")
        return

    for cuenta in cookies:
        driver = webdriver.Chrome()
        driver.get("https://www.instagram.com")
        for cookie in cookies[cuenta]:
            if cookie['domain'] == ".instagram.com":
                try:
                    driver.add_cookie(cookie)
                except Exception as e:
                    print(e)
        driver.get("https://www.instagram.com")
        time.sleep(5)
        print("Iniciando sesion con las cookies de la cuenta: ", cuenta)
        time.sleep(5)
        driver.get(url)
        time.sleep(14)
        wait = WebDriverWait(driver, 10)
        a = driver.find_elements(By.CLASS_NAME, "_abl-")
        a[2].click()
        time.sleep(4)
        pyautogui.typewrite(comentario)
        time.sleep(4)
        pyautogui.press('enter')
        time.sleep(4)

def ElegirCuenta():
    global cookies
    try:
        with open("cookies.pkl", "rb") as f:
            cookies = pickle.load(f)
            print(cookies)
    except:
        cookies = {}
    if cookies == {}:
        messagebox.showinfo("No hay cuentas", "No existen cuentas para elegir")
        return
    cuentas_ventana = Toplevel(ventana)

    with open("cookies.pkl", "rb") as f:
        cookies = pickle.load(f)

    for key in cookies.keys():
        boton = Button(cuentas_ventana, text=key, width=35, command=lambda key=key: seleccionar_cuenta(key,cuentas_ventana))
        boton.pack()


def seleccionar_cuenta(key,cuentas_ventana):
    global selected_key
    selected_key = key
    messagebox.showinfo("Cuenta Seleccionada", "Selected key: "+selected_key)
    cuentas_ventana.destroy()
    return selected_key


def eliminar():
    try:
        with open("cookies.pkl", "rb") as f:
            cookies = pickle.load(f)
    except:
        messagebox.showerror("Error", "No se encontraron cuentas guardadas")
        return

    account_list = list(cookies.keys())
    if len(account_list) == 0:
        messagebox.showerror("Error", "No se encontraron cuentas guardadas")
        return

    delete_window = Toplevel(ventana)
    delete_window.title("Eliminar cuenta")

    for cuenta in account_list:
        tk.Button(delete_window, text=cuenta, command=lambda cuenta=cuenta: eliminar_cuenta(cuenta,delete_window)).grid(row=account_list.index(cuenta), column=1)


def eliminar_cuenta(cuenta,delete_window):
    try:
        with open("cookies.pkl", "rb") as f:
            cookies = pickle.load(f)
    except:
        messagebox.showerror("Error", "No se encontraron cuentas guardadas")
        return
    del cookies[cuenta]
    with open("cookies.pkl", "wb") as f:
        pickle.dump(cookies, f)
    messagebox.showinfo("Cuenta eliminada", "La cuenta ha sido eliminada con éxito")
    delete_window.destroy()


def deseleccionar_cuenta():
    global selected_key
    selected_key = None




ventana = Tk()
ventana.title("Instagram")
ventana.resizable(False, False)
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()
width, height = 500, 400
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
ventana.geometry("%dx%d+%d+%d" % (width, height, x, y))
ventana.columnconfigure(1, weight=1)


BotonAgregarUsuario = Button(ventana, text="Agregar Usuario", width=18, height=2)
BotonAgregarUsuario.grid(row=1, column=1, columnspan=2, padx=(14, 0), pady=10, sticky="nsew")
BotonAgregarUsuario.config(command=añadir_cuenta)


BotonElegirCuenta = Button(ventana, text="Elegir cuenta", width=18, height=2)
BotonElegirCuenta.grid(row=5, column=2, columnspan=2, padx=(0, 65), pady=(14,0))  # sticky="nsew")
BotonElegirCuenta.config(command=ElegirCuenta)


BotonDeseleccionarCuenta = Button(ventana, text="Deseleccionar cuenta", width=18, height=2)
BotonDeseleccionarCuenta.grid(row=6, column=2, columnspan=2, padx=(0, 65), pady=(14, 0))
BotonDeseleccionarCuenta.config(command=deseleccionar_cuenta)


BotonComentarios = Button(ventana, text="Comentarios en una publicación", width=18, height=2)
BotonComentarios.grid(row=2, column=1, columnspan=2, padx=(14, 0), pady=20, sticky="nsew")
BotonComentarios.config(command=Comentarios)

comment_all_button = Button(ventana, text="Comentar con todas las cuentas", command=ComentariosTodas, height=2)
comment_all_button.grid(row=3, column=1,columnspan=2, padx=(14, 0), pady=20, sticky="nsew")

delete_button = Button(ventana, text="Eliminar cuenta", command=eliminar, height=2, width=18)
delete_button.grid(row=7, column=2, columnspan=2, padx=(0, 65), pady=(14, 0))



ventana.mainloop()