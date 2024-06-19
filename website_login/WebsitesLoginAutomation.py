import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Load login details from YAML file
with open('loginDetails.yml', 'r') as file:
    conf = yaml.load(file, Loader=yaml.FullLoader)

myGithubEmail = conf['github_user']['email']
myGithubPassword = conf['github_user']['password']

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def login(url, usernameId, username, passwordId, password, submit_buttonId):
    try:
        driver.get(url)
        driver.find_element(By.ID, usernameId).send_keys(username)
        driver.find_element(By.ID, passwordId).send_keys(password)
        driver.find_element(By.NAME, submit_buttonId).click()
        
        # Added some wait time to observe the result
        import time
        time.sleep(5)  # Wait for 5 seconds to see the result
        
        # Keep the browser open for further inspection or interactions
        print("Login successful. The browser will remain open for further actions.")
        
        # Use input to keep the script running until user decides to close it
        input("Press Enter to close the browser and quit the script...")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()

# Call the login function
login("https://github.com/login", "login_field", myGithubEmail, "password", myGithubPassword, "commit")
