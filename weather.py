def deg_to_sides(n):
    n = round(n / 45)
    if n == 8: n = 1
    return ['Север', 'Северо-восток', 'Восток', 'Юго-восток', 'Юг', 'Юго-запад', 'Запад', 'Северо-запад'][n]


def get_weather(city):
    try:
        city = city[0].upper() + city[1:]
        res = __import__('requests').get(
            f'http://api.openweathermap.org/data/2.5/find?q={city}&type=like&lang=ru&units=metric&APPID=632776fe531822c1da881d1ca73aba40').json()[
            'list'][0]
        temperature = res['main']
        wind = res['wind']
        rain = res['rain']
        if type(rain) == dict:
            rain = rain[list(rain.keys())[0]] * 100
        snow = res['snow']
        if type(snow) == dict:
            snow = snow[list(snow.keys())[0]] * 100
        clouds = res['clouds']

        fields = [
            'name',
            'temperature',
            'feels_like',
            'pressure',
            'humidity',
            'wind_speed',
            'wind_direction',
            'rain',
            'snow',
            'clouds'
        ]

        values = [
            res["name"],
            temperature["temp"],
            temperature["feels_like"],
            round(temperature["pressure"] * 100 / 133, 2),
            temperature["humidity"],
            wind["speed"],
            deg_to_sides(wind["deg"]),
            int(rain) if not rain is None else "Нет",
            int(snow) if not snow is None else "Нет",
            clouds["all"]
        ]
        data = dict(zip(fields, values))
    except:
        raise Exception('Invalid arguments')
    return data