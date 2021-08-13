data = {
    'success': 1,
    'page': 1,
    'result': [
        {
            'id': 1,
            'city': 'bangalore',
            'location': {
                'latitude': 12.12,
                'longitude': 13.12,
            }
        },
        {
            'id': 1,
            'city': 'mumbai',
            'location': {
                'latitude': 14.12,
                'longitude': 15.12,
            }
        },
    ],
}


for x in data['result']:
    city = x['city']
    location = x['location']
    print(f"{city} location is: {location['latitude']}, {location['longitude']}")
