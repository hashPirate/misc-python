import time
import pyautogui
from discord_webhook import DiscordWebhook



def findClickImage(image):
    targetImage = image
    for scrollCount in range(1):
        screenshot=pyautogui.screenshot()
        targetLocation = pyautogui.locateOnScreen(targetImage, confidence=0.8)
        if targetLocation is not None:
            targetCenter = pyautogui.center(targetLocation)
            pyautogui.click(targetCenter)
            break
        time.sleep(1)
    else:
        return 'Not Found'




def send_discord_webhook(webhookUrl: str,message: str):
    webhook = DiscordWebhook(url=webhookUrl,content=message)
    try:webhook.execute()
    except Exception as e:print(f"Error sending Discord webhook: {e}")

def getCount(filename):
        with open(filename, 'r') as file:
            content = file.read()
            integervalue = int(content)
            return integervalue

def addCount(filename, number):
    with open(filename, 'r') as file:
            count = int(file.read())
            file.close()
    newcount = count + number
    with open(filename, 'w') as file:
            file.write(str(newcount))
            file.close()  
successcount = 0
time.sleep(3)
while True:
    print('started')
    checkImage1 = findClickImage('refresh.png')
    time.sleep(9)
    checkImage2 = findClickImage('0.png')
    if(checkImage2 == 'Not Found'):
        send_discord_webhook('', f'[{successcount}] @everyone CLASS OPEN!')
        checkImage3 = findClickImage('register.png')
        time.sleep(4)
        checkImage4 = findClickImage('continue.png')
        send_discord_webhook('', f'[{successcount}] @everyone REGISTERED!')
        break
    time.sleep(1)
    addCount('successcount.txt', 1)
    successcount = getCount('successcount.txt')
    send_discord_webhook('', f'[{successcount}] NOT FREE YET!')
    print(f'{successcount} sent')
    time.sleep(300)






