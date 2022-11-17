import pyautogui
import time
import keyboard

def cautare_google():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'C:\Users\calda\Desktop\imagini\cod.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'C:\Users\calda\Desktop\imagini\cod.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write('https://youtube.com')
        pyautogui.press('enter')
    else:
        print("Imaginea nu este pe ecran")

def cautare_youtube():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'C:\Users\calda\Desktop\imagini\cod2.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'C:\Users\calda\Desktop\imagini\cod2.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write('life of boris')
        pyautogui.press('enter')
    else:
        print("Imaginea nu este pe ecran")

def cautare_boris():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'C:\Users\calda\Desktop\imagini\cod3.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'C:\Users\calda\Desktop\imagini\cod3.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
    else:
        print("Imaginea nu este pe ecran")

def cautare_subscribe():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'C:\Users\calda\Desktop\imagini\cod4.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'C:\Users\calda\Desktop\imagini\cod4.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
    else:
        print("Imaginea nu este pe ecran")        

cautare_google()
cautare_youtube()
cautare_boris()
cautare_subscribe()