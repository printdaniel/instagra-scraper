# Usuario
from dotenv import load_dotenv
import os
load_dotenv()
USER = os.getenv('IGUSER')
TARGET = 'python3.py'
#################
# User & Password
#################
LOGIN_1 = "//*[@id='loginForm']/div/div[1]/div/label/input"
LOGIN_2 = "//*[@id='loginForm']/div/div[2]/div/label/input"

#####################
# Search 
#####################
SEARCH_1 = "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[2]"

SEARCH_2 = "x19g9edo" 

#################
# Select
#################
SELECT = "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div/div[2]/div/div/span/span"

