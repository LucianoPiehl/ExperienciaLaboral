from selenium.webdriver.common.by import By
from appium import webdriver
import time
"""
Los time.sleep() son de numeros grandes porque mi telefono es lento al abrir nuevas interfaces,
para cambiarlo modificar la siguiente variable
"""
datos = {
'usuario' : 'wendyturner329ysu',
'contraseña' : 'MpEgPAhd',
'url_publicacion' : 'https://www.instagram.com/p/ClZj_e4vZCF/',
'comentario' : 'Este es un comentario automatizado!',
'tiempo' : 3
}
"""
Conexión
"""
driver = {
  "platformName": "Android",
  "appium:platformVersion": "8.1",
  "appium:deviceName": "j2corelteub",
  "appium:automationName": "UiAutomator1",
  "appium:appPackage": "com.instagram.android",
  "appium:appActivity": "com.instagram.mainactivity.MainActivity"
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)
"""
Driver.get para ir a la página específica de la publicación
"""
while True:
    driver.get(datos['url_publicacion'])
    time.sleep(datos['tiempo'])
    try:

        time.sleep(datos['tiempo'])
        driver.find_element(By.ID, "com.instagram.android:id/log_in_button").click()
        time.sleep(datos['tiempo'])
        driver.find_element(By.CLASS_NAME, "android.widget.EditText").send_keys(datos['usuario'])
        time.sleep(datos['tiempo'])
        driver.find_element(By.ID, "com.instagram.android:id/password").send_keys(datos['contraseña'])
        time.sleep(datos['tiempo'])
        driver.find_element(By.ID, "com.instagram.android:id/next_button").click()
        time.sleep(datos['tiempo'] * 3)
        driver.find_element(By.XPATH, '// android.widget.Button[ @ content - desc = "Ahora no"]').click()
        time.sleep(datos['tiempo'] * 3)
        """Esta notificacion solo aparece cuando no hay cuentas registradas"""
    except:
        pass
    finally:
        """
        Escribir Comentario
        """
        time.sleep(datos['tiempo']*2)
        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="Comentar"]').click()
        time.sleep(datos['tiempo'])
        driver.find_element(By.ID, 'com.instagram.android:id/layout_comment_thread_edittext').click()
        time.sleep(datos['tiempo'])
        driver.find_element(By.ID, 'com.instagram.android:id/layout_comment_thread_edittext').send_keys(datos['comentario'])
        time.sleep(datos['tiempo'])
        driver.find_element(By.ID, 'com.instagram.android:id/layout_comment_thread_post_button').click()
        time.sleep(datos['tiempo']*5)
        time.sleep(3600)    #1 Hora = 3600 segs
        driver.close_app()


