#Librerias
from time import sleep
from random import randint as rn
from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy as By
#Funciones

def login():
    """
    Precondicion: La cuenta ingresada en el campo de datos existe en la base de datos de instagram.
    No hay una cuenta cargada previamente. El dispositivo no usa google smartlock.
    Proceso:
    Click en iniciar sesion
    Ingresa usuario
    Ingresa contraseña
    Click en next
    Devuelve: Instagram abierto con la cuenta iniciada
    """
    try:
        sleep(datos['tiempo'])
        driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]").click()
        sleep(datos['tiempo'])
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText").send_keys(datos['usuario'])
        sleep(datos['tiempo'])
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]").send_keys(datos['contraseña'])
        sleep(datos['tiempo'] * 4)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout").click()
        sleep(datos['tiempo'])
    except:
        pass


def feed():
    """
    Precondicion: Hay publicaciones en el feed

    Proceso:
    Genera un numero de veces en las que se hará un scroll para abajo,
    Realiza el scroll y da like a la publicacion visible con una posibilidad de 1 entre 3

    Devuelve: Algunas publicaciones en el feed fueron vistas y likeadas
    """
    sleep(datos['tiempo'] * 3)
    size = driver.get_window_size()
    veces = rn(2,7)
    driver.swipe(start_x=size['width'] - (size['width'] // 2), start_y=size['height'] * 0.6,end_x=size['width'] - (size['width'] // 2), end_y=size['height'] * 0.4, duration=200)
    for i in range(veces):
        driver.swipe(start_x=size['width'] - (size['width'] // 2), start_y=size['height'] * 0.7,end_x=size['width'] - (size['width'] // 2), end_y=size['height'] * 0.3, duration=200)
        like = rn(1,3)
        if like == 1:
            sleep(rn(3,8))
            driver.find_element(By.ID, "com.instagram.android:id/row_feed_button_like").click()

def feed_lupa():
    """
    Precondicion: Ninguna
    Proceso:
    Se genera un numero entre 1 y 7 que determina cuantas publicaciones se van a ver
    y otro numero entre 1,5 que determina si las mismas seran likeadas o no
    (En caso del numero ser 1 se hace click en like, posibilidad de 1 entre 5)
    Se elige una publicacion al azar dentro de las visibles,
    Se espera un tiempo y en caso de like==1 se da click en like
    Click para atras y se repite si veces > 0
    Devuelve: Algunas publicaciones en la lupa fueron vistas
    """
    sleep(datos['tiempo']*3)
    size = driver.get_window_size()
    veces = rn(1,7)
    while True:
        sleep_tiempo = rn(1,12)
        like = rn(1,5)
        sleep(datos['tiempo'])
        driver.find_element(By.ID,'com.instagram.android:id/search_tab').click()
        sleep(datos['tiempo'])
        elements = driver.find_elements(By.CLASS_NAME, 'android.widget.Button')
        publicacion = rn(0,len(elements)-1)
        sleep(datos['tiempo'])
        elements[publicacion].click()
        sleep(sleep_tiempo)
        if like == 1:
            driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="Me gusta"]')
        driver.back()
        driver.swipe(start_x=size['width'] - (size['width'] // 2), start_y=size['height'] * 0.20,end_x=size['width'] - (size['width'] // 2), end_y=size['height'] * 0.80, duration=200)
        veces-=1
        if veces == 0:
            break

def historia():
    """
    Precondicion: Hay mas de 15 historias que el usuario pueda ver
    Proceso:
    Se genera un numero aleatorio para determinar cuantas historias seran vistas,
    Se hace click en la primera historia que aparece
    Se genera otro numero para ver si se realizara un swipe (posibilidad de 1 entre 5)
    Si no hay swipe se espera un numero aleatorio de tiempo entre 1 y 15 segundos y luego de esperar se da click
    Devuelve: Las historias fueron vistas y algunas fueron skipeadas
    """

    historias = rn(1, 15)
    size = driver.get_window_size()
    sleep(datos['tiempo']*3)
    elements = driver.find_elements(AppiumBy.ID, 'com.instagram.android:id/outer_container')
    print(elements)
    elements[1].click()
    for i in range(historias):
        swipe = rn(1, 5)
        try:
            sleep(datos['tiempo']//2)
            driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Seguir viendo historias"]').click()
            sleep(datos['tiempo']//2)
            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.Button/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]").click()
        except:
            pass
        if swipe == 1:
            try:
                driver.swipe(start_x=size['width']-100, start_y=size['height']//2, end_x=100, end_y=size['height']//2, duration=200)
                swipe = rn(1, 10)
            except:
                historias += 1
                continue
        sleep(rn(1,15))
        #Pasar de historia
        TouchAction(driver).tap(None, size['width']-100,size['height']//2, 1).perform()

    driver.back()
def seguir_usuarios():
    """
    Precondicion: Hay mas de 12 usuarios que el usuario no sigue en los likes de las publicaciones
    Proceso:
    Esto se repite para las 5 primeras publicaciones
    Se dirije hacia el usuario, y busca la publicacion que corresponde
    Clickea en las personas que dieron like a la publicacion
    Pregunta si hay algun usuario ahi dentro que la cuenta actual no este siguiendo, en caso de si lo sigue.
    En caso de no hace scroll para abajo y repite el proceso. En caso de no poder hacer scroll para abajo lo hace para arriba
    Devuelve: Los usuarios fueron seguidos correctamente
    """
    size = driver.get_window_size()
    #Dos for que representan el paso por la matriz de publicaciones
    for j in range(1,2):
        for i in range(1,3):
            driver.swipe(start_x=size['width'] // 2, start_y=size['height'] * 0.60, end_x=size['width'] // 2,end_y=size['height'] * 0.40, duration=200)
            #veces = la cantidad de personas que se van a seguir
            #contador_seguidos es la cantidad de personas que ya fueron seguidas
            veces = rn(4, 12)
            contador_seguidos = 0
            driver.get(datos['url_usuario'])
            sleep(datos['tiempo']*2)
            nombre = driver.find_element(By.ID,'com.instagram.android:id/profile_header_full_name').text
            xpath = '//android.widget.Button[@content-desc="Foto de '+nombre+' en fila '+str(j)+', columna '+str(i)+'"]'
            driver.find_element(By.XPATH,xpath).click()
            sleep(datos['tiempo'])
            #try:
            driver.find_element(By.ID,'com.instagram.android:id/row_feed_like_count_facepile_stub').click()
            #except:
                #driver.find_element(By.ID,'com.instagram.android:id/row_feed_textview_likes').click()
            sleep(datos['tiempo'])
            while contador_seguidos != veces:
                disponible = -1
                sleep(datos['tiempo'] // 2)
                driver.swipe(start_x=size['width'] // 2, start_y=size['height'] * 0.60, end_x=size['width'] // 2,end_y=size['height'] * 0.40, duration=200)
                sleep(datos['tiempo'] // 2)
                lista = driver.find_elements(By.ID, 'com.instagram.android:id/row_follow_button')
                sleep(datos['tiempo']//2)
                #Este while es para que cada vez que haga un swipe busque todas las posibilidades para seguir almenos un usuario
                while True:
                    disponible += 1
                    try:
                        libre = lista[disponible].text
                    except:
                        break
                    if libre == 'Seguir':
                        lista[disponible].click()
                        contador_seguidos += 1
                        break
            #volver a las publicaciones del usuario
            driver.back()
def main():
    """
    Precondiciones: Instagram debe estar abierto y debe tener una cuenta iniciada
    Proceso:
    Ejecuta una de las 3 funcionalidades de evasion de deteccion por la IA
    Y luego la funcion para seguir personas
    Devuelve: Las funciones realizadas correctamente
    """
    while True:
        #login()
        driver.get('https://www.instagram.com/')
        opcion = rn(1, 3)
        if opcion == 1:
            historia()
        elif opcion == 2:
            feed_lupa()
        else:
            feed()
        seguir_usuarios()
        sleep(3600)#1 hora




#Variables Globales
datos = {
    'usuario': 'lucho_pct',
    'contraseña': 'uadelucho43',
    'url_usuario': 'https://www.instagram.com/datazosparalagente/?next=%2F',
    'tiempo': 3
}
"""
usuario = input('Ingrese el usuario')
contraseña = input('Ingrese la contraseña')
url_usuario = input('Ingrese la url de el usuario competencia')
"""
driver = {
    "platformName": "Android",
    "appium:platformVersion": "7.1.2",
    "appium:deviceName": "G011A model:G011A",
    "appium:automationName": "UiAutomator2",
    "appium:appPackage": "com.instagram.android",
    "noReset": True
    }
driver = webdriver.Remote('http://localhost:4723/wd/hub', driver)
#Ejecucion
main()



