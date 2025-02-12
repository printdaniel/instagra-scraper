# -----------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from constantes import *
from time import sleep
import wget
import getpass
import os
import logging
import urllib.error

# -----------------------------------------------------------------------------
# Configuración básica del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Objeto logger
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
#  Instagram User data
my_user = USER

# Objetivo, ingreso de cuenta que se desea descargar.
print("Recuerda que el username debe ser exacto")
target = input("Ingrese el username de la cuenta: ")

# Password de su cuenta Insagram.
my_psw = getpass.getpass()
logger.info("Credenaciales cargadas")

# -----------------------------------------------------------------------------
# Selenium Options
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_experimental_option('detach', True)
logger.info("Opciones [webdriver, maximized, detach]")

# -----------------------------------------------------------------------------
# Output dir
current_dir = os.getcwd()
dest_loc = current_dir + '/images/'

if not os.path.exists(dest_loc):
    os.makedirs(dest_loc)
logger.info("Directorio de imágenes creado")

# Driver init
driver = webdriver.Chrome(options=options)
driver.get("https://instagram.com/")
logger.info("Chromium cargado")

#################
# User & Password
#################
# Parámetros
TIMEOUT = 12

def wait_and_click(driver, locator, log_message=""):
    """ Espera a que un elemento sea clickeable y lo clickea """
    try:
        element = WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable(locator))
        element.click()
        logger.info(log_message)
    except Exception as e:
        logger.error(f"Error al hacer clic en {locator}: {str(e)}")
        raise

def wait_and_send_keys(driver, locator, value, log_message=""):
    """ Espera a que un elemento sea clickeable y envía texto """
    try:
        element = WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable(locator))
        element.send_keys(value)
        logger.info(log_message)
    except Exception as e:
        logger.error(f"Error al enviar texto en {locator}: {str(e)}")
        raise

# Input user data
wait_and_click(driver, (By.XPATH, USERNAME_FIELD_XPATH), "User paso 1: Click en usuario")
wait_and_send_keys(driver, (By.XPATH, USERNAME_FIELD_XPATH), my_user, "User paso 2: Usuario ingresado")

# Input Passoword field
wait_and_click(driver, (By.XPATH, PASSWORD_FIELD_XPATH), "User paso 3: Click en contraseña")
wait_and_send_keys(driver, (By.XPATH, PASSWORD_FIELD_XPATH), my_psw, "User paso 4: Contraseña ingresada")

#################
# Sesion init
#################
wait_and_click(driver, (By.CLASS_NAME, "_acap"), "Inicio de sesión paso 1: Click en botón de inicio de sesión")
#wait_and_click(driver, (By.CLASS_NAME, "xlyipyv"), "Click en Now No")
#wait_and_click(driver, (By.XPATH, NOW_NO_XPATH), "Inicio de sesión paso 2: Click en 'Ahora no'")
#wait_and_click(driver, (By.XPATH, "x10wlt62"), "Inicio de sesión paso 2: Click en 'Ahora no'")
#wait_and_click(driver, (By.CLASS_NAME, "x6s0dn4"), "Now No")

sleep(5)
#####################
# Search
#####################
driver.get("https://instagram.com/" + target + "/")
logger.info("user url listo")

#############################
# Encontrar y recopilar links
#############################
my_images = set()
last_height = 0

while True:
    # Obtener la altura actual de la página
    new_height = driver.execute_script("return document.body.scrollHeight")

    # Scroll hacia abajo
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Encontrar y guardar los links
    images = driver.find_elements(By.CSS_SELECTOR,"._aagv img")
    for image in images:
        try:
            source = image.get_attribute("src")
        except:
            continue
        my_images.add(source)

    sleep(6)

    # Verificar si se han cargado todas las imágenes
    if new_height == last_height:
        print("Se han cargado todas las imágenes")
        break

    # Actualizar la altura anterior
    last_height = new_height

print(f"Total de imágenes recolectadas: {len(my_images)}")

########################
# Close googledrive
########################
driver.quit()
logger.info("Webdriver cerrado")

########################
# Download images
########################
count = 1
for image_url in my_images:
    try:
        # Descargar la imagen
        file_name = os.path.join(dest_loc, f"image_{count}.jpg")  # Nombre del archivo
        wget.download(image_url, out=file_name)
        print(f"\nImagen {count} de {len(my_images)} descargada: {file_name}")
    except urllib.error.URLError as e:
        print(f"\nError al descargar la imagen {count}: {e}")
    except Exception as e:
        print(f"\nError inesperado al descargar la imagen {count}: {e}")
    finally:
        count += 1
