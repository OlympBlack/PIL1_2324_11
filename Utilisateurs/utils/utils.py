import requests
import math
def get_loca_coord(latitude, longitude):
    api_key = ""
    url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{longitude},{latitude}.json?access_token={api_key}'
    response = requests.get(url)
    data = response.json()
    
    if 'features' in data and len(data['features']) > 0:
        place = data['features'][0]['place_name']
        city = data['features'][0]['text']
        country = data['features'][0]['context'][0]['text']
        return city, country
    return None, None

def get_coord_city(city):
    api_key = ""
    url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{city}.json?access_token={api_key}'
    response = requests.get(url)
    data = response.json()
    
    if 'features' in data and len(data['features']) > 0:
        latitude = data['features'][0]['center'][1]
        longitude = data['features'][0]['center'][0]
        country = data['features'][0]['context'][0]['text']
        return latitude, longitude, country
    return None, None, None

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Rayon de la terre en km
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    
    return distance

