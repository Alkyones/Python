
from selenium import webdriver
import time
import sys, os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

platformInput = input("Please enter your platform : ")
usernameInput = input("Please enter your email : ")
passwordInput = input("Please enter your password : ")


if (usernameInput and passwordInput and platformInput):
    sys.argv.append(platformInput)
    sys.argv.append(usernameInput)
    sys.argv.append(passwordInput)

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--user-data-dir=C:\\Users\\lifeo\\AppData\\Local\\Google\\Chrome\\User Data')
chrome_options.add_argument("--window-size=%s" % "1920,1080")

platforms = {
    "dev": "dev.frupro.app",
    "qa": "qa.frupro.app",
    "stg": "staging.frupro.app",
}

accounts = {
    "gurkan.gursoy": {
        "username": "gurkan.gursoy@frupro.com",
        "password": "P@ssword"    
    },
    "lifeonshort": {
        "username": "lifeonshort@gmail.com",
        "password": "P@ssword"    
    },
    "nuri": {
        "username": "nuri@frupro.com",
        "password": "P@ssword"    
    },
    "user1": {
        "username": "user01-full@frupro.app",
        "password": "P@ssword"
    },
    "user2": {
        "username": "user02-full@frupro.app",
        "password": "P@ssword"
    },
    "user3": {
        "username": "user05-full@frupro.app",
        "password": "P@ssword"
    }
}

platform = sys.argv[1]
url = platforms[platform]

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

def getTokenWithPassword(args):
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(f"https://{url}")
    time.sleep(1)

    username = str(sys.argv[2])
    password = str(sys.argv[3])

    try:
        elementAccept = driver.find_element(By.CLASS_NAME, "jss79")
        if(elementAccept):
            elementAccept.click()
    except:
        pass

    elementEmail = driver.find_element(By.ID,"formEmail")
    elementEmail.click()
    elementEmail.send_keys(username)
    print(elementEmail)

    elementPass= driver.find_element(By.ID,"formPassword")
    elementPass.click();
    elementPass.send_keys(password)

    elementSubmit = driver.find_element(By.CLASS_NAME, "btn-primary");
    elementSubmit.click();
    time.sleep(1);

    token =driver.execute_script("return localStorage.token")
    addToClipBoard(token)

def getToken(args):
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(f"https://{url}")
    time.sleep(1)

    if(sys.argv[2] in accounts):
        username = accounts[sys.argv[2]]["username"]
        password = accounts[sys.argv[2]]["password"]
    else:
        return "No information available for given account"
    
    try:
        elementAccept = driver.find_element(By.CLASS_NAME, "jss79")
        if(elementAccept):
            elementAccept.click()
    except:
        pass

    elementEmail = driver.find_element(By.ID,"formEmail")
    elementEmail.click()
    elementEmail.send_keys(username)
    print(elementEmail)

    elementPass= driver.find_element(By.ID,"formPassword")
    elementPass.click();
    elementPass.send_keys(password)

    elementSubmit = driver.find_element(By.CLASS_NAME, "btn-primary");
    elementSubmit.click();
    time.sleep(1);

    token =driver.execute_script("return localStorage.token")
    addToClipBoard(token)

if(len(sys.argv) == 3):
    getToken(sys.argv)
elif(len(sys.argv) == 4):
    getTokenWithPassword(sys.argv);


print("Copied to clipboard!");
time.sleep(2);
x = input("\nPlease enter to exit program. ")
if not x :
    print("Exiting the Program.")
    exit()

