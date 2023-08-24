import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys


def mensajes_no_leidas(mensaje):
    # Cargo variables de entorno
    load_dotenv()
    # Accedo a las credenciales de la cuenta, del archivo .env
    username = os.environ.get('USERNAME_LINKEDIN')
    password = os.environ.get('PASSWORD_LINKEDIN')
    # Abro el navegador y acceder a LinkedIn
    driver = webdriver.Chrome()
    driver.get('https://linkedin.com/login')

    # Inicio sesión en LinkedIn
    username_input = driver.find_element(By.ID, 'username')
    password_input = driver.find_element(By.ID, 'password')
    username_input.send_keys(username)
    password_input.send_keys(password)
    driver.find_element(By.XPATH, '//button[text()="Iniciar sesión"]').click()
    time.sleep(16)

    # Capturo el nombre del usuario para luego usarlo
    nombre_usuario = driver.find_element(By.CSS_SELECTOR, '.t-16.t-black.t-bold').text
    time.sleep(7)

    # Accedo a la página de mensajes
    driver.get('https://www.linkedin.com/messaging/')
    time.sleep(7)
    # Recorro cada chat
    elements = driver.find_elements(By.CSS_SELECTOR, "li.scaffold-layout__list-item")
    for elemento in elements:
        flag = True
        elemento.click()
        time.sleep(3)
        # Recorro cada mensaje
        li_elements = driver.find_elements(By.CSS_SELECTOR, "li.msg-s-message-list__event.clearfix")
        time.sleep(3)
        for element in li_elements:
            time.sleep(3)
            #Busco el nombre de cada mensaje
            try:
                name_element = element.find_element(By.CSS_SELECTOR,"span.msg-s-message-group__name")
                name = name_element.text
            except:
                pass
            #Lo comparo con el mio.
            if name == nombre_usuario:
                flag = False
                break  # Detenemos el ciclo al encontrar un mensaje enviado por el usuario
        #Si no hay ningun mensaje mio, se envia el mensaje
        if flag:
            #try: -> Por si es un mensaje no contestable de linkedin.
            try:
                texto = driver.find_element(By.CSS_SELECTOR,'.msg-form__contenteditable.t-14.t-black--light.t-normal.flex-grow-1.full-height.notranslate')
                texto.send_keys(mensaje)
                time.sleep(5)
                button_element = driver.find_element(By.CSS_SELECTOR,'.msg-form__send-button.artdeco-button.artdeco-button--1')
                button_element.click()
                time.sleep(5)
            except:
                pass
def mensaje_primera_interaccion(mensaje):

    # Cargo variables de entorno
    load_dotenv()
    # Accedo a las credenciales de la cuenta, del archivo .env
    username = os.environ.get('USERNAME_LINKEDIN')
    password = os.environ.get('PASSWORD_LINKEDIN')
    # Abro el navegador y acceder a LinkedIn
    driver = webdriver.Chrome()
    driver.get('https://linkedin.com/login')

    # Inicio sesión en LinkedIn
    username_input = driver.find_element(By.ID, 'username')
    password_input = driver.find_element(By.ID, 'password')
    username_input.send_keys(username)
    password_input.send_keys(password)
    driver.find_element(By.XPATH, '//button[text()="Iniciar sesión"]').click()
    time.sleep(16)
    # Capturo el nombre del usuario para luego usarlo
    nombre_usuario = driver.find_element(By.CSS_SELECTOR, '.t-16.t-black.t-bold').text
    time.sleep(7)

    # Accedo a la página de mensajes
    driver.get('https://www.linkedin.com/messaging/')
    time.sleep(7)
    # Recorro cada chat
    elements = driver.find_elements(By.CSS_SELECTOR, "li.scaffold-layout__list-item")
    for elemento in elements:
        flag = True
        elemento.click()
        time.sleep(3)
        # Recorro cada mensaje
        li_elements = driver.find_elements(By.CSS_SELECTOR, "li.msg-s-message-list__event.clearfix")
        time.sleep(3)
        for element in li_elements:
            time.sleep(3)
            #Busco el nombre de cada mensaje
            try:
                name_element = element.find_element(By.CSS_SELECTOR,"span.msg-s-message-group__name")
                name = name_element.text
            except:
                pass
            #Lo comparo con el mio.
            if name == nombre_usuario:
                flag = False
        #Si no hay ningun mensaje mio, se envia el mensaje
        if flag:
            #try: -> Por si es un mensaje no contestable de linkedin.
            try:
                texto = driver.find_element(By.CSS_SELECTOR,'.msg-form__contenteditable.t-14.t-black--light.t-normal.flex-grow-1.full-height.notranslate')
                texto.send_keys(mensaje)
                time.sleep(5)
                button_element = driver.find_element(By.CSS_SELECTOR,'.msg-form__send-button.artdeco-button.artdeco-button--1')
                button_element.click()
                time.sleep(5)
            except:
                pass
#mensajes_no_leidas('Buenos dias. Mis horarios son de 12 PM en adelante.')
#mensaje_primera_interaccion('Buenos dias.')
