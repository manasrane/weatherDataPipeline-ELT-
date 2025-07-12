import requests
api_key = "676f1fba82624ce10cd82441bef55e62"
api_url = "http://api.weatherstack.com/current"
params = {
    'access_key': api_key,  # Your actual API key
    'query': 'New%20York'
}
"""# Example usage:
def requestApi():
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        print("Success")
        return response.json()
    except requests.exceptions.RequestException as e :
        print(f"ERROR :{e}")
        raise
requestApi()
"""
def requestApi():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-06-21 07:44', 'localtime_epoch': 1750491840, 'utc_offset': '-4.0'}, 'current': {'observation_time': '11:44 AM', 'temperature': 23, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0002_sunny_intervals.png'], 'weather_descriptions': ['Partly cloudy'], 'astro': {'sunrise': '05:25 AM', 'sunset': '08:31 PM', 'moonrise': '02:00 AM', 'moonset': '04:33 PM', 'moon_phase': 'Waning Crescent', 'moon_illumination': 26}, 'air_quality': {'co': '492.1', 'no2': '20.165', 'o3': '136', 'so2': '12.025', 'pm2_5': '22.94', 'pm10': '24.05', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 8, 'wind_degree': 313, 'wind_dir': 'NW', 'pressure': 1020, 'precip': 0, 'humidity': 61, 'cloudcover': 50, 'feelslike': 25, 'uv_index': 0, 'visibility': 16, 'is_day': 'yes'}}
requestApi()

