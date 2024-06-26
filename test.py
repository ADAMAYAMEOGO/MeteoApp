import requests

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip_data = response.json()
    return ip_data['ip']

def get_location(ip_address):
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    location_data = response.json()
    return location_data

