# Import statements
import selenium
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

# Configuración básica del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Crear un objeto logger
logger = logging.getLogger(__name__)

#  Instagram User data
my_user = USER
target = TARGET
#my_pwd =  getpass.getpass()
my_psw = getpass.getpass()
logger.info("Credenaciales cargadas")

#  Opciones
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_experimental_option('detach', True)
logger.info("Opciones [webdriver, maximized, detach]")

# Output dir 
current_dir = os.getcwd()
dest_loc = current_dir + '/images/'

if not os.path.exists(dest_loc):
    os.makedirs(dest_loc)
logger.info("Directorio de imágenes creado")

# Driver init
# driver = webdriver.Chrome('/var/task/scraper/chromedriver/chromedriver', options=chrome_options)
driver = webdriver.Chrome(options=options)
driver.get("https://instagram.com/")
logger.info("Chromium cargado")

#################
# User & Password
#################
WebDriverWait(driver, 12).until(EC.element_to_be_clickable((
            By.XPATH, LOGIN_1 ))).click()
logger.info("User paso 1")

WebDriverWait(driver, 12).until(EC.element_to_be_clickable((
            By.XPATH, LOGIN_1 ))).send_keys(my_user)
logger.info("User paso 2")

WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((
            By.XPATH, LOGIN_2 ))).click()
logger.info("User paso 3")

WebDriverWait(driver, 12).until(EC.element_to_be_clickable((
        By.XPATH, LOGIN_2))).send_keys(my_psw)
logger.info("User paso 4")

#################
# Iniciar session
#################
WebDriverWait(driver, 12).until(EC.element_to_be_clickable((
    By.XPATH, INIT_SESSION_1 ))).click()
logger.info("Inicio de sesión paso 1")

WebDriverWait(driver, 12).until(EC.element_to_be_clickable((
    By.CLASS_NAME, 'xa49m3k'))).click()
logger.info("Inicio de sesión paso 2 -> Ahora no")

WebDriverWait(driver, 12).until(EC.element_to_be_clickable((
    By.CLASS_NAME, NOTIFICACIONES))).click()
logger.info("Inicio de sesión paso 3 -> Ahora no 2")

#####################
# Search 
#####################
WebDriverWait(driver, 12).until(EC.element_to_be_clickable((
        By.XPATH, SEARCH_1 ))).click()
logger.info("Inicio de search paso 1 -> Click in search")

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
        By.XPATH, SEARCH_2 ))).click()
logger.info("Inicio de search paso 2 -> Click in box")

busqueda = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
        By.CLASS_NAME, "x1lugfcp" ))).send_keys(target)
logger.info("Inicio de search paso 3")

#########################
# Seleccionar la búsqueda
#########################
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
        By.XPATH, SELECT))).click()

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
    
    sleep(3)
    
    # Verificar si se han cargado todas las imágenes
    if new_height == last_height:
        print("Se han cargado todas las imágenes")
        break
    
    # Actualizar la altura anterior
    last_height = new_height

print(len(my_images))

########################
# Descargar las imágenes
########################
for image in my_images:
    try:
        wget.download(image,dest_loc)
    except:
        continue

driver.quit()
