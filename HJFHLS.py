red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
reset = "\033[0m"
print("COLOUR CALIBRATION TEST")
print(f"{red}red{reset}")
print(f"{green}green{reset}")
print(f"{yellow}yellow{reset}")
print(f"{blue}blue{reset}")
print(f"{magenta}magenta{reset}")
import time
import random
loaf = False
drink = False
pocket = False
buff3t = False
searcher = False
potato = False
transport = False
suffer = False
pandemonium = False
inventory = {}
valid_choice = False
skip = False
def Print(text):
    global skip
    if skip:
        return
    print(text)
    pi = input("<more>")
    if pi.lower() == "s":
        skip = True
        print("\n Skipped \n")
        



print(f"Welcome to {blue}Help Jack Find His Lost Shampoo Somewhere In A Sidewalk In Los Angeles!{reset}")

while True:
   try:
     print("________________________")
     print("Menu: settings, credits,")
     print("changelog, start, exit.")
     print("________________________")
     print("***We Recommend Using The Lastest Python.***")
     menu = input("@")
     more = "<more>"
     if (menu == "exit"):
        valid_choice = True
        goodbye = random.randint(1, 5)
        if (goodbye == 1):
            print("Goodbye!")
        if (goodbye == 2):
            print("Wish you the bestest luck!")
        if (goodbye == 3):
            print("Hope you have a good day!")
        if (goodbye == 4):
            print("Really wishing you the best week!")
        if (goodbye == 5):
            print("Play again later!")
        break 
     elif (menu == "settings"):
        valid_choice = True
        print("settings is still a work in progress, thank you!")
     elif (menu == "credits"):
        print("Credits:")
        print("skate - Lead Programmer")
        print("noobo - Main Tester")
        print("_")
        print("_")
     elif (menu == "changelog"):
        valid_choice = True
        print("Developtment!!! version 0.1")
        print("--builded base game..")
        print("anddd nothing else!")
     elif (menu == "loaf"):
         valid_choice = True
         print("LOAF LOAF LOAF")
         print("+5 Bread Added Into Inventory")
         inventory["Bread"] = 5
         loaf = True
     elif (menu == "drink"):
         valid_choice = True
         print("hydration is good for your health")
         print("+2 Bottle Of Mineral Water Added Into Inventory")
         inventory["Mineral Water"] = 2
         drink = True
     elif menu == "pocket":
         valid_choice = True
         print("go to the atm and get som' pocket money quickly")
         pocket = True
         print("Bank Account: -30 Pocket Money: +30")
     if (menu == "start"):
         valid_choice = True
         
     if not valid_choice:
         print("Invalid Option!")
         
 
     if (menu == "start"):
        valid_choice = True
        Print("One Day....")
        time.sleep(1)
        Print(f"{green}Jack{reset} bought a shampoo from his local trusty shop... ")
        
        Print(f"{red}Unfortunately{reset} this time, he dropped it somewhere in a sidewalk while cycling to his home.")      
        Print("He only realized this after he was arrived at his home.")    
        Print("Oof! it is now night..")
        Print("Two days later..")       
        Print("Then, He started an incredible journey into finding his shampoo... ")
        Print("He suspected it couldve dropped off when he was cycling on the sidewalk..")
        time.sleep(3)
        print("In this game, you will be helping him search for his shampoo. he bought the shampoo with his last pocket money, and he cant afford to lose it.")
        time.sleep(1)
        hour = 1
        day = 1
        weather = random.randint(0, 10)                    
        umbrella = False
        mood = 100
        hunger = 50
        thirst = 50
        money = 0
        BA = 3800
        weather3 = 0
        weather2 = 0
        rain = False
        if pocket == True:
            money += 30
            BA -= 30
        event = random.randint(1, 45)
        def weather4():
            global weather2
            global rain 
            weather3 =  random.randint(1, 20)
            if weather3 in (1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19,):
                weather2 = "cloudy"
            if (weather3 in (5, 10, 15, 20)):
                rain = True
        if (weather in (0, 1, 2, 3)):
            weather2 = "sunny"
        if (weather in (4, 5, 6,)):
            weather2 = "cloudy"
            weather4()
        if (weather == 7):
            weather2 = "rainy"
        if (weather == 8):
            weather2 = "thunderstorm"
        if (weather == 9):
            weather2 = "windy"
        if (weather == 10):
            weather2 = "hurricane"
        time.sleep(3)
        choice = input("Bring umbrella..? [y/n]")
        if (choice == "y"):
            print("i guess thats the right choice.")
            umbrella = True
        if (choice == "n"):
            print("Mmkay.")
            umbrella = False
        time.sleep(2)    
        print(f"HOUR {hour} DAY {day}")
        print(f"It's {weather2} Outside.")
        print(f"Mood: {mood}")
        print(f"Pocket Money: {money}")
        print(f"Bank Account: {BA}")
        time.sleep(2)
        if weather in (0, 1, 2, 3):
            print("Its abit hot, but sure.")
        if weather in (4, 5, 6):
            print(f"Ah! its abit cool now... but there might be a chance for a {blue}rain{reset}...")
        if rain == True:
            print("Ahh! everything is getting wet! do i have an umbrella!?")
            if (umbrella == False):
                print("Dammit! Everything's soaked now! How am i supposed to be going out with everythings soaked!?")
                mood = mood - 30
                print(f"{red}Mood: -30{reset}")
                print(f"Mood: {mood}")
            if (umbrella == True):
                print("Just as handy.")
                time.sleep(4)
                print("Equipping...")
                time.sleep(3)
                print("Equipped")
                umbrella = True
                print("Yippeee")
                print(f"{green}Mood: 100{reset}")
        if (weather == 8):
            print(f"{red}WHY AM I EVEN OUT HERE?!?!{reset}")
            choice = input("Go indoors and skip this day? [y/n]")
            if (choice == "y"):
                print("Zzz..")
            if (choice == "n"):
                print(f"are you {red}insane?{reset}")
                time.sleep(5)
                print("perhaps...")
                time.sleep(4)
                print("Hold on.")
                if (umbrella == True):
                    print("Lifesaver! I got a handy umbrella that i brought earlier!")
                if (umbrella == False):
                    print("Shoot.")
                    mood = mood - 45
                    print(f"{red}Mood: -45{reset}")
                    print(f"Mood: {mood}")
        if (weather == 10):
             pass        
        def choice():  
            print("Im thinking of doing....")
            choice = input("@")
            if choice == "i":
                print("Let me check the inventory")
                time.sleep(1)
                print(f"Inventory: {inventory}")
            if choice == "weather":
                print("hmmm...weather.")
                choice2 = input("Source?")
                if choice2 == "sky":
                    print("Let me look the sky.")
                    if (weather in (0, 1, 2, 3)):
                        print("It's sunny.")
                    if (weather in (4, 5, 6)):
                   
                        if rain == True:
                            print("It's raining! Ouch my eyes is getting hit by the raindrops.")
                        else:
                            print("It's cloudy.")
                    
                    
                
            
            
        
        
        
                        
   except Exception as e:
       print(f"error004: crash/force close: {e}")
       break
   
        
                
                
             
        
            
            
    
    
    
   
    

    

