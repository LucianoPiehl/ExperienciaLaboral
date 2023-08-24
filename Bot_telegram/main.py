from datetime import datetime
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui


media_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "media")
if not os.path.exists(media_folder):
    os.makedirs(media_folder)

file_descriptions=[]

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define the handler function for receiving messages
def start(update, context):
    update.message.reply_text('Por favor envíe una foto junto con un mensaje. El mensaje debe tener los siguientes datos: fecha, hora, descripcion de la publicacion, usuario y contraseña en ese orden. Ademas debe seguir el siguiente formato: 11/11/1111;11:11:11;Mensaje de ejemplo;UsuarioEjemplo;ContraseñaEjemplo')

def download_file(url, file_path):
    response = requests.get(url)
    open(file_path, "wb").write(response.content)

def receive_message(update, context):
    cola = []
    def tiempo(date, hour):
        target_time = datetime.strptime(f"{date} {hour}", "%d/%m/%Y %H:%M:%S")
        current_time = datetime.now()
        difference = target_time - current_time
        return int(difference.total_seconds())

    def post_insta(tupla):
        user, password, description, file_path = tupla[0],tupla[1],tupla[2],tupla[3]
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(8)

        field = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        field.send_keys(user)
        field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        field.send_keys(password)
        time.sleep(2)
        button = driver.find_element(By.XPATH, "//div[text()='Iniciar sesión']")
        button.click()
        time.sleep(10)
        button = driver.find_elements(By.XPATH, "//*[contains(text(), 'Not Now')]")
        if len(button) > 0:
            button[0].click()
        time.sleep(10)
        button = driver.find_elements(By.XPATH, "//*[contains(text(), 'Cancel')]")
        if len(button) > 0:
            button[0].click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//div[text()="Crear"]').click()
        time.sleep(4)
        driver.find_element(By.XPATH, "//button[text()='Seleccionar de la computadora']").click()
        time.sleep(5)
        pyautogui.typewrite(file_path)
        pyautogui.press("enter")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[text()='Siguiente']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[text()='Siguiente']").click()
        time.sleep(3)
        elemento = driver.find_element(By.XPATH,"//textarea[@aria-label='Escribe una descripción...' or @placeholder='Escribe una descripción...']")
        elemento.click()
        elemento.send_keys(description)
        button = driver.find_element(By.XPATH, "//*[contains(text(), 'Compartir')]")
        button.click()
        time.sleep(5)

        driver.quit()

    try:
        # Recibir la foto y el mensaje
        photo = update.message.photo[-1].get_file()
        text = update.message.caption
        file_url = photo.file_path

        # Separar los datos del texto
        date, hour, description, user, password = text.split(";")

        # Generar un nombre de archivo único
        file_name = "photo_{}_{}.jpg".format(update.message.message_id, int(time.time()))
        file_path = os.path.join(media_folder, file_name)

        # Descargar el archivo
        download_file(file_url, file_path)

        # Add the file name and description to the list
        cola.append((user, password, description, file_path, date, hour))
        for i in range(0,len(cola)):
            time.sleep(tiempo(cola[i][4],cola[i][5]))
            post_insta(cola[i])
    except:
        update.message.reply_text('Datos incorrectos, o formato no valido.')



def main():
    # Get the Bot API token
    token = "6205633843:AAHXDqjCAwohvoRB_s_fDUH5zGT6GiBV1SQ"

    # Create the Updater
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add message handler
    message_handler = MessageHandler(Filters.text | Filters.photo | Filters.video, receive_message)
    dp.add_handler(message_handler)


    updater.start_polling()


    updater.idle()








if __name__ == '__main__':
    main()
