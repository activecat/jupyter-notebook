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
    print(f"{x['city']} location is: {', '.join([str(x[1]) for x in x['location'].items()])}")
