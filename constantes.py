# Usuario
from dotenv import load_dotenv
import os
load_dotenv()

USER = os.getenv("USERIG") or int(input("Ingrese su cuenta: "))
#################
# User & Password
#################
USERNAME_FIELD_XPATH = "//*[@id='loginForm']/div/div[1]/div/label/input"
PASSWORD_FIELD_XPATH = "//*[@id='loginForm']/div/div[2]/div/label/input"

#################
# Select
#################
SELECT = "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div/div[2]/div/div/span/span"

NOW_NO_XPATH ="/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div[3]/div[2]/svg/path"

# Wait time
TIMEOUT = 12
