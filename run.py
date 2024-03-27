from colorama import Fore, Style
from time import sleep
from scraping import scrape_twitter_user

usernameArr = input('insert the usernames separated with a comma like this adam,ali....:\n').split(',')
targetTag = input('insert targeted tag:\n').upper()
time_input = input('insert desired time interval to run this script in minutes (if you want to run it once don\'t type any thing):\n')
base_time_interval = 0
if (time_input):
    base_time_interval = int(time_input)*60
    
time_interval_increment = base_time_interval
all_cashTags = []

def loop():
    for i, username in enumerate(usernameArr):
        print('\n\n')
        print(Fore.GREEN,f'[{i+1} of {len(usernameArr)}][scrapping: {username}]')
        print(Style.RESET_ALL)

        user_cashTags = scrape_twitter_user(username)
        if isinstance(user_cashTags,list):
            all_cashTags.extend(user_cashTags)
        print('\n\n')
        print(f'Result: {targetTag} was mentioned "{all_cashTags.count(targetTag)}" in the last {round(time_interval_increment/60,2)} minutes')
    
if(base_time_interval):
    while True:
        all_cashTags = []
        loop()
        sleep(time_interval_increment)
        time_interval_increment += base_time_interval
else:
    loop()


