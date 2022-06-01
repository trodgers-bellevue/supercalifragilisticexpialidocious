# Author: <Teresa Rodgers>
# Creation Date: <05-31-22>

#IMPORT LIBRARIES
import requests
import json

#FUNCTIONS
def zipcode():
    API_KEY = '1f77756c500ee73b6842f5bb0ae62a1a'
    zip_code = input("For what zip code would you like to find the weather    :")
    
    weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?zip={zip_code}&appid={API_KEY}&units=imperial')
    
    if weather_data.status_code == 200:
        print("Success is in our grasp!")
        city = weather_data.json()['name']
        weather = weather_data.json()['weather'][0]['description']
        temp = weather_data.json()['main']['temp']
        high_temp = weather_data.json()['main']['temp_max']
        low_temp = weather_data.json()['main']['temp_min']
        feels_like = weather_data.json()['main']['feels_like']
        humidity = weather_data.json()['main'] ['humidity']

        print("")
        print(f"It is currently {weather} in {city}.")
        print("")
        print(f"With a high of      : {high_temp}°F")
        print(f"And a low of        : {low_temp}°F")
        print(f"A real feel Temp of : {feels_like}°F")
        print(f"It is currently {temp}°F with {humidity}% humidity")
        question = input('Do you want to do another search ? Type Yes or No: ')
        if question == 'Yes':
            main()
        elif question == 'No':
            print("Thank you for using the program. Good Bye!")
            exit()

    elif weather_data.status_code == 404:
        print("Zip code not found")
    
    else:
        print("Try again next time.")



def city_weather():
    API_KEY = '1f77756c500ee73b6842f5bb0ae62a1a'

    user_city = input("What city would you like to know the weather for?    :")
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={API_KEY}&units=imperial")

    if weather_data.status_code == 200:
        print("Success is in our grasp!")
        weather = weather_data.json()['weather'][0]['description']
        temp = weather_data.json()['main']['temp']
        high_temp = weather_data.json()['main']['temp_max']
        low_temp = weather_data.json()['main']['temp_min']
        feels_like = weather_data.json()['main']['feels_like']
        humidity = weather_data.json()['main'] ['humidity']

        print("")
        print(f"It is currently {weather} in {user_city} today.")
        print("")
        print(f"With a high of      : {high_temp}°F")
        print(f"And a low of        : {low_temp}°F")
        print(f"A real feel Temp of : {feels_like}°F")
        print(f"It is currently {temp}°F with {humidity}% humidity")

        question = input('Do you want to do another search ? Type Yes or No: ')
        if question == 'Yes':
            main()
        elif question == 'No':
            print("Thank you for using the program. Good Bye!")
            exit()

    elif weather_data.status_code == 404:
        print("City Not Found")

    
    else:
        print("That didn't work, lets try again?")

API_KEY = '1f77756c500ee73b6842f5bb0ae62a1a'

#MAIN PROGRAM

def main():

    print("")
    welcome = input("Welcome to the Rodgers' Weather Report Program: Press Enter to Continue")
    while True:
        answer = input("Would you like to see the weather somewhere? Please type zip code or city: ")
        if answer == 'city':
            try:
                print("Let's look up the current weather by city.")
                city_weather()

            except Exception:
                print(" city was invalid. please Try again")
                city_weather()

        if answer == 'zip code':
            try:
                print("Let's look up the curren weather by the zip. ")
                zipcode()

            except Exception:
                print("zip code was invalid. please Try again")
                zipcode()

        else:
            print("not one of the options. please Try again.")
main()



