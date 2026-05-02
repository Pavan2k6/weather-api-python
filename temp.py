import requests

api_key = "2b7b889d67ae78c5de9c353445bb2e89"

while True:

    city = input("Enter the city(Press E to exit): ").capitalize()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    emo = ""
   
    if city == 'E':
        print("Thank you.")
        break
    
    if response.status_code == 200:
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        print(f"Weather report of {city}.")
        print("==========================")
        if temp > 30:
            emo = "🥵"
        elif temp < 30 and temp >= 21:
            emo = "😌"
        elif temp <= 20 and temp >= 11:
            emo = "😀"
        else:
            emo = "🥶"
        print(f"Temperature: {temp}°C{emo}.")
        print(f"Weather: {weather}.")
        print(f"Humidity: {humidity}%.")
        print("==========================")

    else:
        print(f"Data not found {response.status_code}.")
    
        
        
        

