# Importing necessary modules and libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from yaspin import yaspin
import warnings
from mtranslate import translate
import colorama
import time

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

# Suppressing warnings
warnings.simplefilter("ignore")
# Initializing colorama for colored output
colorama.init(autoreset=True)

# Function to initialize the Selenium WebDriver
def Initialize_AI(headless, chrome_driver_path):
    if headless:
        # For headless view
        warnings.simplefilter("ignore")
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

# Initializing the Selenium WebDriver
driver = Initialize_AI(headless=True, chrome_driver_path = r'D:\PI_AI-main-1\PI_AI-main\chromedriver.exe')

# Setting voice and query count
VOICE = 5 # Choose the Voice which You like Most
Queries = 1 # It will Count How many Queries you have asked

try:
    # Navigating to the website
    print("Loading website...")
    driver.get(url='https://pi.ai/talk')
    print(f"{colorama.Fore.GREEN}Website Loaded Successfully.")

    # Clicking on 'Next' button to proceed
    print("Clicking on 'Next' button...")
    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next')]")))
    next_button.click()

    # Clicking on 'Next' button again
    print("Clicking on 'Next' button again...")
    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next')]")))
    next_button.click()

    # Clicking on 'Next' button once more
    print("Clicking on 'Next' button once more...")
    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next')]")))
    next_button.click()

    # Entering name into the textarea
    print("Entering name into the textarea...")
    textarea = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
    textarea.send_keys("Sujal Rajpoot")

    # Clicking on submit button
    print("Clicking on submit button...")
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Submit text']")))
    submit_button.click()

    # Clicking on 'Pi {VOICE}' button
    print(f"Clicking on 'Pi {VOICE}' button...")
    pi_voice_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), 'Pi {VOICE}')]")))
    pi_voice_button.click()

    # Clicking on 'Choose voice' button
    print("Clicking on 'Choose voice' button...")
    later_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Choose voice')]")))
    later_button.click()

    # Clicking on 'I’ve got my own topic' button
    print("Clicking on 'I’ve got my own topic' button...")
    button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'I’ve got my own topic')]")))
    button.click()
    
    # Waiting for the text area to initialize
    while True:
        try:
            print('Finding Text Area to Initialize....\n')
            textarea = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
            if textarea:
                print(f"{colorama.Fore.GREEN}PI AI Initialize Successfully.\n")
                break
        except:
            continue

    # Main loop for user interaction
    while True:
        query = str(input('You: ')) # You can Even talk in hindi or hinglish language
        # Check if input is empty
        if not query.strip():
            continue
        else:
            try:
                # Translate Hinglish query to English
                translated_phrase, time_taken = translate_hinglish_to_english(query)
                print(colorama.Fore.YELLOW + f"TRANSLATED: {translated_phrase}")
                print(colorama.Fore.CYAN + f"TIME TAKEN TO TRANSLATE: {round(time_taken, 2)} seconds\n")

                # Attempting to handle pop-ups
                try:
                    print("Trying to click on Not now button\n")
                    not_now_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div/div/div/div/div/div[2]/button")))
                    not_now_button.click()
                    print('Clicked on Not Now Button Sucessfully.\n')

                    print("Trying to click on I don’t want an account Button\n")
                    i_do_not_want_account_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div/div/div/div/div/div/div[2]/button")))
                    i_do_not_want_account_button.click()
                    print('Clicked on I don’t want an account Button Sucessfully.\n')
                except:
                    pass

                # Entering translated query into the textarea
                print("Entering text into the textarea...")
                textarea = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
                textarea.send_keys(str(translated_phrase))
                print(f"{colorama.Fore.YELLOW}You Asked {Queries} Queries.\n")
                print(colorama.Fore.CYAN + f"You Asked to PI: {str(translated_phrase)}\n")

                # Clicking on submit button
                print("Clicking on submit button...\n")
                submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Submit text']")))
                submit_button.click()
                Queries = Queries+1

                # Displaying spinner while waiting for response
                with yaspin(text="Getting Response...", color="magenta") as spinner:
                    sleep(10)
                    response = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div'))).text
                    spinner.stop()
                    print(f'PI AI: {response}\n')
                
            except Exception as PIE:
                print(PIE)

except Exception as E:
    print(f"{colorama.Fore.RED} {E}")

'''
Example Usage:
You: hi
TRANSLATED: hi
TIME TAKEN TO TRANSLATE: 1.02 seconds

Trying to click on Not now button

Entering text into the textarea...
You Asked 1 Queries.

You Asked to PI: hi

Clicking on submit button...

PI AI: Hello there, Sujal! 👋 What’s on your mind today? 😊

You: kaisi ho tum aur kya kar rahi ho
TRANSLATED: how are you and what are you doing
TIME TAKEN TO TRANSLATE: 1.51 seconds

Trying to click on Not now button

Entering text into the textarea...
You Asked 2 Queries.

You Asked to PI: how are you and what are you doing

Clicking on submit button...

PI AI: I'm doing well, thanks for asking! 🤖 I'm just hanging out in the digital realm, ready to answer any questions you have or chat about anything that's on your mind! What's new with you? ��'''