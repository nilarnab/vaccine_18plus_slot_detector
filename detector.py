# you might need to install this
# pip install requests
import requests

from datetime import date
import time

# you might need to install this
# pip install beeply
# to learn more, you can go to https://www.geeksforgeeks.org/beeply-module-in-python/
import winsound

from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


today = date.today()
d1 = today.strftime("%d-%m-%Y")

print("DATE", d1)



iterations = 1

while True:
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=621&date=' + d1, headers = headers)

    found = False
    if r.status_code == 200:
        for center in r.json()['centers']:
            for session in center['sessions']:
                # print(center['name'], ':', 'DATE: ', session['date'], 'age limit', session['min_age_limit'], 'capacity', session['available_capacity'])
                if session['min_age_limit'] == 18 and session['available_capacity']:
                    # print('FOUND')
                    found = True
                else:
                    pass

                if session['min_age_limit'] == 18:
                    # print(center['name'], ':', 'DATE: ', session['date'], 'age limit', session['min_age_limit'], 'capacity', session['available_capacity'])
                    pass
    else:
        print('MAYBE THEIR SERVER IS DOWN')

    if found:
        print("CALLING BEEP")
        # frequency, duration(milisec)
        winsound.Beep(800, 3000)
    else:
        print("NOT FOUND", iterations)

        
    time.sleep(5)
    # print("ITERATIONS", iterations)
    iterations += 1
    clear()
