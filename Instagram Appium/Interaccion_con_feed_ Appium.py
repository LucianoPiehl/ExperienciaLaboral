from appium import webdriver
import random

from selenium.common import NoSuchElementException


def iniciar_sesion_instagram(usuario, contraseña):
 driver_capabilities = {
  "platformName": "Android",
  "appium:platformVersion": "7.1.2",
  "appium:deviceName": "G011A model:G011A",
  "appium:automationName": "UiAutomator2",
  "appium:appPackage": "com.instagram.android",
  "noReset": True
 }

 # Inicializamos el driver de Appium
 driver = webdriver.Remote("http://localhost:4723/wd/hub", driver_capabilities)

 # Esperamos a que se cargue la página de inicio
 driver.implicitly_wait(10)

 # Hacemos click en el botón "Iniciar sesión"
 iniciar_sesion_button = driver.find_element_by_id('com.instagram.android:id/log_in_button')
 iniciar_sesion_button.click()

 # Esperamos a que se cargue la página de inicio de sesión
 driver.implicitly_wait(10)

 # Ingresamos el nombre de usuario
 usuario_input = driver.find_element_by_id('com.instagram.android:id/login_username')
 usuario_input.send_keys(usuario)

 # Ingresamos la contraseña
 contraseña_input = driver.find_element_by_id('com.instagram.android:id/login_password')
 contraseña_input.send_keys(contraseña)

 # Hacemos click en el botón "Iniciar sesión"
 iniciar_sesion_button = driver.find_element_by_id('com.instagram.android:id/button_text')
 iniciar_sesion_button.click()


driver=webdriver.Remote("http://localhost:4723/wd/hub",{"platformName":"Android","appium:platformVersion":"7.1.2","appium:deviceName":"G011A model:G011A","appium:automationName":"UiAutomator2","appium:appPackage":"com.instagram.android","noReset":True})
iniciar_sesion_instagram('lucho_pct','uadelucho44')
driver.implicitly_wait(10)
counter=1
while counter<=random.randint(10,20):
 posts=driver.find_elements_by_id('com.instagram.android:id/row_feed_button_like')
 for post in posts:
  if counter%3==0 and random.random()<0.5:
   post.click()
   counter+=1
 try:
  next_button=driver.find_element_by_id('com.instagram.android:id/button_next')
  next_button.click()
 except NoSuchElementException:break
