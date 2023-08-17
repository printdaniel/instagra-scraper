# Import statements
import selenium
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep 
import wget
import getpass
import os

#  Instagram User data
my_user = "ig_user"
target = "juliana.romero.75"
#my_pwd =  getpass.getpass()
my_psw = getpass.getpass()


#  Opciones
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_experimental_option('detach', True)

# Output dir 
current_dir = os.getcwd()
dest_loc = current_dir + '/images/'

if not os.path.exists(dest_loc):
    os.makedirs(dest_loc)

# Driver init
# driver = webdriver.Chrome('/var/task/scraper/chromedriver/chromedriver', options=chrome_options)
driver = webdriver.Chrome(options=options)
driver.get("https://instagram.com/")

#################
# User & Password
#################
WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((
            By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'
            ))
        ).click()

WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((
            By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'
            ))
        ).send_keys(my_user)


WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((
            By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'
            ))
        ).click()


WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((
            By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'
            ))
        ).send_keys(my_psw)


#################
# Iniciar session
#################
WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((
            By.CLASS_NAME, '//*[@id="loginForm"]/div/div[3]/button/div'
            ))
        ).click()



WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((
            By.CLASS_NAME, 'xa49m3k'
            ))
        ).click()

WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((
            By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'
            ))
        ).click()
#####################
# Search 
#####################
WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((
            By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div/div[1]/div/div'
            ))
        ).click()

WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((
            By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input'
            ))
        ).click()


busqueda = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((
            By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input'
            ))
        ).send_keys(target)

# Seleccionar la búsqueda
WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((
            By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a/div/div/div/div[2]/div/div'
            ))
        ).click()

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
