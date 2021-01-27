import bot_api.weather as w
import bot_api.exchange_rates as r


class Api:
    @staticmethod
    def weather(city):
        return w.get_weather(city)

    @staticmethod
    def beauty_weather(city):
        data = w.get_weather(city)
        data['temperature'] = str(data['temperature']) + ' ℃'
        data['feels_like'] = str(data['feels_like']) + ' ℃'
        data['pressure'] = str(data['pressure']) + ' мм рт. ст.'
        data['humidity'] = str(data['humidity']) + '%'
        data['wind_speed'] = str(data['wind_speed']) + ' м/с'
        if data['rain'] != 'Нет':
            data['rain'] = str(data['rain']) + '%'
        if data['snow'] != 'Нет':
            data['snow'] = str(data['snow']) + '%'
        data['clouds'] = str(data['clouds']) + '%'
        return data

    @staticmethod
    def rate():
        return r.rate()
