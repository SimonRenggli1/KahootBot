from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

pin = input("PIN: ")
names = ["Kahoot me", "Pill Cosby", "Claustrophobic Teletubby", "Mr.stark I don’t feel so good", "HortonHearsAJew", "Kahoot the Teacher", "Honey wheres my super kah00t", "Nerdy-Poo", "KahToot", "Loud Mouth", "Inky", "Chunkie","Confused Teletuby", "KaShootMe", "Sub2PewDiePie", "Kim Jong Uno", "Comedy Central", "Homer", "Couch Potato", "Kashoot me", "Kim Jong OOF", "Moe Lester", "Third Wheeler", "Nugget", "Kashoot da teacher", "Chungus the fungus", "Kermit Kermicide", "Lil Diabetus", "Big Chungus", "Walking Dictionary", "Summer Teeth", "Gucci Flippidy Flops", "Johnny Johnny", "Weird Beard", "Kermit", "Deja View", "Fire Guy", "Fuzzy Pack", "Butternut", "Organic Punk", "Chris P Chicken", "Ligma", "Kool Kids Klub", "Married Man", "Metal Star", "Ctrl W = Win", "Peter file", "TRIGGERED", "Nerf Bastion", "Billy Hills","Night Magnet", "Dancing Madman", "Egghead", "Babysaurus", "Enigma", "Eye Candy", "Cheeky Monkey", "Butter Scotch", "Junior Jumper", "Floating Heart", "Loading…", "Yeet or be Yeeted", "Pink Nightmare", "Wildcat Talent", "Koi Diva", "TeKilla Sunrise", "Gabe itch", "Loaf of Beans", "Dixie Normous", "Cheese Ball", "Candy Cough", "Panda Heart", "Cranberry Sprite", "Crayon Munchers", "Magic Peach", "Tiger Kitty", "Flower Child", "Freckles", "Tragic Girl", "Girls of Neptune", "Candycane Missy", "Cutie Bun", "Huggable Bab", "Missie Lucky", "Broken Paws", "Anonymous Girl", "Tiny Hunter", "Super Giggles", "Lady Fantastic", "Mafia Princess", "Eye Candy Kitten", "Troubled Chick", "Feral Filly", "Sassy Muffin", "Canary Apple Red", "Woodland Beauty", "Miss Fix It", "Miss Meow", "Emerald Goddess" ,"Marshmallow Treat", "Leading Light", "Queen Bee", "Microwave Chardonnay", "Gentle Woman", "Cute Pumpkin", "Titanium Ladybug", "Freeze Queen", "Young Lady", "Winner Woman", "Wonk Sidewalk", "EnforcerTeen", "Me Miss", "Undergrad Split", "Triple Adorable", "Her Majesty", "Cinderella", "The Beekeeper", "Cool Whip", "Digital Goddess", "Peanut Butter Woman", "Fresh Lovely", "Fisher Teen", "Lady Turnip", "Luna Star", "Princess Fuzzie", "Rainbow Sweety"]
botamount = int(input("How many Bots would you like to Generate? "))
i = 0

options = webdriver.ChromeOptions()
options.add_argument("--headless")

# Initialize the Chrome driver using webdriver-manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

while i < botamount:
    name = random.choice(names)
    driver.get("https://kahoot.it")
    
    # Locate the PIN input field
    pin_textbox = driver.find_element(By.ID, "game-input")
    
    # Simulate realistic typing for the PIN
    for char in pin:
        pin_textbox.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))  # Random delay between 0.1 to 0.3 seconds
    
    # Click the Enter button
    enter_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Enter') or contains(text(), 'Eingabe')]")
    enter_button.click()
    time.sleep(1)  # Wait for the next page to load
    
    # Locate the nickname input field
    name_textbox = driver.find_element(By.ID, "nickname")
    
    # Simulate realistic typing for the nickname
    for char in name:
        name_textbox.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))  # Random delay between 0.1 to 0.3 seconds
    
    names.remove(name)
    
    # Click the OK, go! button
    start_button = driver.find_element(By.XPATH, "//button[contains(text(), 'OK, go!') or contains(text(), 'OK, los!')]")
    start_button.click()
    
    # Open a new tab for the next bot
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    i += 1

# Close the driver after all bots have been generated
driver.quit()
