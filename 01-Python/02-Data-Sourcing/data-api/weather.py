'''entendendo esse exercicio'''
import sys
import requests

BASE_URI = "https://weather.lewagon.com"




def search_city(query):
    '''For return city'''

    url = 'https://weather.lewagon.com/geo/1.0/direct'
    params = {'q': query, 'limit': 5}
    response = requests.get(url, params=params).json()

    if response:
        if len(response) > 1:
            print("Multiple cities found:")
            for idx, city in enumerate(response):
                print(f"{idx + 1}. {city['name']}")
            choice = int(input("Please choose a city (enter the number): ")) - 1
            city = response[choice]
        else:
            city = response[0]
        print(f"City found: {city['name']}")
        return city

    print("City not found!")
    return None


def weather_forecast(lat, lon):
    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''

    url2 = 'https://weather.lewagon.com/data/2.5/forecast'
    params2 = {'lat': lat, 'lon': lon}
    response2 = requests.get(url2, params=params2).json()
    lista_completa = response2['list']
    datas = []
    resultado = []


    for item_lista in lista_completa:
        data_exata = item_lista['dt_txt'][:10]
        tempo = (item_lista['weather'][0]['description']).capitalize()
        temperatura = round((float(item_lista['main']['temp']) - 273.15),2)

        if data_exata not in datas and len(datas) < 5:
            datas.append(data_exata)
            resultado.append({'date':data_exata, 'weather':tempo, 'temperature': temperatura})

    for item in resultado:
        print(item)
    return resultado

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city_info = search_city(query)

    if city_info:
        lat = city_info['lat']
        lon = city_info['lon']
        weather_forecast(lat,lon)
    else:
        print("Please try again with a valid city.")


if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
