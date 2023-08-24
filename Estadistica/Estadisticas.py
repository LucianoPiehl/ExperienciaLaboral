import tkinter as tk
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_messages():
    # Obtener los valores ingresados por el usuario
    email = email_entry.get()
    password = password_entry.get()
    mensaje = mensaje_entry.get()

    # Inicializar el navegador
    driver = webdriver.Chrome()

    # Ir a la página de inicio de LinkedIn
    driver.get("https://www.linkedin.com/login")

    # Ingresar el correo electrónico y la contraseña
    wait = WebDriverWait(driver, 10)

    email_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
    email_input.send_keys(email)

    password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password_input.send_keys(password)
    csv = []
    # Presionar el botón de inicio de sesión
    login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn__primary--large")))
    login_button.click()
    time.sleep(17)
    driver.get('https://www.linkedin.com/messaging/')
    time.sleep(7)
    cont=0
    elements = driver.find_elements(By.CSS_SELECTOR, "li.scaffold-layout__list-item")
    for elemento in range(0,len(elements)):
        time.sleep(13)
        elements[elemento].click()
        time.sleep(3)
        li_elements = driver.find_elements(By.CLASS_NAME, 'msg-s-event-listitem__body')
        time.sleep(3)
        name = driver.find_element(By.CSS_SELECTOR, ".msg-entity-lockup__entity-title").text
        for i,element in enumerate(li_elements):
            try:
                nombre_element = driver.find_element(By.CSS_SELECTOR, ".msg-s-message-group__profile-link").text
            except:
                pass

            lista = driver.find_element(By.ID, "thread-detail-jump-target").text.split(' ')
            print('ACA', element.text, 'ACA 2', mensaje.replace('[FIRSTNAME]', lista[0]))
            if element.text == mensaje.replace('[FIRSTNAME]', lista[0]):
                cont += 1
                enlace = driver.find_elements(By.TAG_NAME, 'a')
                url_actual = enlace[17].get_attribute("href")
                a= [cont,name,url_actual]
                csv.append(a)
    with open('statistics.csv', 'w', encoding='utf-8') as arch:
        for i in csv:
            arch.write(f'{i[0]};{i[1]};{i[2]}\n')

    # Cerrar el navegador
    driver.quit()

# Crear la ventana principal
root = tk.Tk()
root.title("LinkedIn Messenger Search")

# Crear los widgets de la interfaz
email_label = tk.Label(root, text="Correo electrónico:")
email_entry = tk.Entry(root)

password_label = tk.Label(root, text="Contraseña:")
password_entry = tk.Entry(root, show="*")

mensaje_label = tk.Label(root, text="Mensaje:")
mensaje_entry = tk.Entry(root)

search_button = tk.Button(root, text="Buscar", command=search_messages)

# Crear los widgets de la interfaz
email_label = tk.Label(root, text="Correo electrónico:")
email_entry = tk.Entry(root)

password_label = tk.Label(root, text="Contraseña:")
password_entry = tk.Entry(root, show="*")

mensaje_label = tk.Label(root, text="Mensaje:")
mensaje_entry = tk.Entry(root)

search_button = tk.Button(root, text="Buscar", command=search_messages)

# Organizar los widgets en una grilla
email_label.grid(row=0, column=0)
email_entry.grid(row=0, column=1)

password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)

mensaje_label.grid(row=2, column=0)
mensaje_entry.grid(row=2, column=1)

search_button.grid(row=3, column=1)

root.mainloop()


"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el navegador
driver = webdriver.Chrome()

# Ir a la página de inicio de LinkedIn
driver.get("https://www.linkedin.com/login")

# Ingresar el correo electrónico y la contraseña
wait = WebDriverWait(driver, 10)

email = wait.until(EC.presence_of_element_located((By.ID, "username")))
email.send_keys("mcgregor2333@yahoo.com")

password = wait.until(EC.presence_of_element_located((By.ID, "password")))
password.send_keys("webcn2021")
mensaje = ""Hola wacho""
# Presionar el botón de inicio de sesión
login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn__primary--large")))
login_button.click()
time.sleep(17)
driver.get('https://www.linkedin.com/messaging/')
time.sleep(7)
dict = {}
cont=0
elements = driver.find_elements(By.CSS_SELECTOR, "li.scaffold-layout__list-item")
for elemento in range(0,len(elements)):
    flag = True
    time.sleep(13)
    elements[elemento].click()
    time.sleep(3)
    li_elements = driver.find_elements(By.CLASS_NAME, 'msg-s-event-listitem__body')
    time.sleep(3)
    name = driver.find_element(By.CSS_SELECTOR, ".msg-entity-lockup__entity-title").text
    for i,element in enumerate(li_elements):
        try:
            nombre_element = driver.find_element(By.CSS_SELECTOR, ".msg-s-message-group__profile-link").text
        except:
            pass

        lista = driver.find_element(By.ID, "thread-detail-jump-target").text.split(' ')
        print('ACA', element.text, 'ACA 2', mensaje.replace('[FIRSTNAME]', lista[0]))
        if element.text == mensaje.replace('[FIRSTNAME]', lista[0]):
            cont += 1
            with open('statistics.csv', 'a', encoding='utf-8') as arch:
                enlace = driver.find_elements(By.TAG_NAME, 'a')
                url_actual = enlace[17].get_attribute("href")
                arch.write(f'{cont};{name};{url_actual}\n')




# Cerrar el navegador
driver.quit()
"""