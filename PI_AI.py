import colorama
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from yaspin import yaspin
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from mtranslate import translate
from time import sleep
import time

# Suppressing warnings
colorama.init(autoreset=True)

# Setting voice and query count
VOICE = 5 # Choose the Voice which You like Most
Queries = 1 # It will Count How many Queries you have asked

# Function to translate Hinglish text to English
def translate_hinglish_to_english(hinglish_phrase):
    # Measure time taken for translation
    start = time.time()
    # Translate Hinglish phrase to English
    english_trans = translate(to_translate=hinglish_phrase, to_language="en", from_language="hi")
    end = time.time()
    # Calculate time taken
    time_taken = end-start
    return english_trans, time_taken

# Function to initialize the Selenium WebDriver
def Initialize_AI(headless, chrome_driver_path):
    if headless:
        # For headless view
        # Configuring Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        chrome_options.add_argument("--headless=new")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--log-level=3')
        service = Service(executable_path=chrome_driver_path)
        user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
        chrome_options.add_argument(f'user-agent={user_agent}')
        chrome_options.add_argument('--log-level=3')
        # Initializing Chrome WebDriver with configured options
        driver = webdriver.Chrome(service=service, options=chrome_options)
    else:
        # For non-headless view
        chrome_options = webdriver.ChromeOptions()  
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        # Initializing Chrome WebDriver with default options
        driver = webdriver.Chrome(service=Service(executable_path=chrome_driver_path, options=chrome_options))
    return driver

def Get_Ready_AI(headless:bool, chrome_driver_path:str, Your_Name:str) -> None:
    # Initializing the Selenium WebDriver
    driver = Initialize_AI(headless, chrome_driver_path)

    try:
         # Navigating to the website
        with yaspin(text="Loading website...", color="magenta") as spinner:
            driver.get(url='https://pi.ai/talk')
            spinner.stop()

        # Clicking on 'Next' button to proceed
        with yaspin(text="Clicking on 'Next' button...", color="magenta") as spinner:
            next_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next')]")))
            next_button.click()
            spinner.stop()

        # Clicking on 'Next' button again
        with yaspin(text="Clicking on 'Next' button again...", color="magenta") as spinner:
            next_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next')]")))
            next_button.click()
            spinner.stop()

        # Clicking on 'Next' button once more
        with yaspin(text="Clicking on 'Next' button once more...", color="magenta") as spinner:
            next_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next')]")))
            next_button.click()
            spinner.stop()

        # Entering name into the textarea
        with yaspin(text="Entering name into the textarea...", color="magenta") as spinner:
            textarea = WebDriverWait(driver, 1000).until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
            textarea.send_keys(Your_Name)
            spinner.stop()

        # Clicking on submit button
        with yaspin(text="Clicking on submit button...", color="magenta") as spinner:
            submit_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Submit text']")))
            submit_button.click()
            spinner.stop()

        # Clicking on 'Pi {VOICE}' button
        with yaspin(text=f"Clicking on 'Pi {VOICE}' button...", color="magenta") as spinner:
            pi_voice_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), 'Pi {VOICE}')]")))
            pi_voice_button.click()
            spinner.stop()

        # Clicking on 'Choose voice' button
        with yaspin(text="Clicking on 'Choose voice' button...", color="magenta") as spinner:
            later_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Choose voice')]")))
            later_button.click()
            spinner.stop()

        # Clicking on 'I’ve got my own topic' button
        with yaspin(text="Clicking on 'I’ve got my own topic' button...", color="magenta") as spinner:
            button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'I’ve got my own topic')]")))
            button.click()
            spinner.stop()
        

        # Waiting for the text area to initialize
        while True:
            try:
                with yaspin(text="Finding Text Area to Initialize....", color="magenta") as spinner:
                    textarea = WebDriverWait(driver, 1000).until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
                    if textarea:spinner.stop();break
            except:continue

        return driver, True
    except Exception as e:
        print(f"{colorama.Fore.RED}Error: {e}")
        return driver, False

# Example usage:
driver, status = Get_Ready_AI(headless=False, chrome_driver_path=r'enter your chromedriver path', Your_Name='')
print(f'Driver Session ID: {driver.session_id}, Status: {status}\n')

if status:
    while True:
        query = str(input('You: ')) # You can Even talk in hindi or hinglish language
        # Wait for the element with the specified text to appear
        try:
            WebDriverWait(driver, 2).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'div'), "Apologies, an unexpected error has occurred. Please check back again soon."))
            print("Apologies, an unexpected error has occurred. Please check back again soon.\n")
            driver.refresh()
        except:pass
        
        # Check if input is empty
        if not query.strip():continue
        try:
            # Translate Hinglish query to English
            translated_phrase, time_taken = translate_hinglish_to_english(query)
            print(colorama.Fore.YELLOW + f"TRANSLATED: {translated_phrase}")
            print(colorama.Fore.CYAN + f"TIME TAKEN TO TRANSLATE: {round(time_taken, 2)} seconds\n")

            # Attempting to handle pop-ups
            try:
                # Getting the textarea to enter query into the textarea
                with yaspin(text="Getting textarea to enter query into the textarea...", color="magenta") as spinner:
                    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
                    spinner.stop()
            except:
                with yaspin(text="Trying to click on Not now button...", color="magenta") as spinner:
                    not_now_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div/div/div/div/div/div[2]/button")))
                    not_now_button.click()
                    spinner.stop()
                    print('Clicked on Not Now Button Sucessfully.\n')
                
                with yaspin(text="Trying to click on I don’t want an account Button...", color="magenta") as spinner:
                    i_do_not_want_account_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div/div/div/div/div/div/div[2]/button")))
                    i_do_not_want_account_button.click()
                    spinner.stop()
                    print('Clicked on I don’t want an account Button Sucessfully.\n')

            # Entering translated query into the textarea
            with yaspin(text="Entering text into the textarea...", color="magenta") as spinner:
                textarea = WebDriverWait(driver, 1000).until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
                textarea.send_keys(str(translated_phrase))
                spinner.stop()
                print(f"{colorama.Fore.YELLOW}You Asked {Queries} Queries.")
                print(colorama.Fore.CYAN + f"You Asked to PI: {str(translated_phrase)}\n")

            # Clicking on submit button
            with yaspin(text="Clicking on submit button...", color="magenta") as spinner:
                submit_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Submit text']")))
                submit_button.click()
                spinner.stop()
                if Queries==49:
                    print(driver.get_cookies())
                    driver.delete_all_cookies()
                    sleep(1)
                    driver, status = Get_Ready_AI(headless=False, chrome_driver_path=r'enter your chromedriver path', Your_Name='')
                    print(f'Driver Session ID: {driver.session_id}, Status: {status}\n')
                    Queries = 0
                    
            Queries = Queries+1
                
            # Displaying spinner while waiting for response
            with yaspin(text="Getting Response...", color="magenta") as spinner:
                sleep(10)
                response = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div'))).text
                spinner.stop()
                print(f"{colorama.Fore.GREEN}PI AI: {response}\n")
            
        except Exception as PIE:print(f"{colorama.Fore.RED}{PIE}")
else:print('Sorry Sir, I am Facing issues while initializing AI.')