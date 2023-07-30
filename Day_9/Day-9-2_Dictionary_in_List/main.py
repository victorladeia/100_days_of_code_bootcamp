

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities_visited": [ "Paris", "Lille", "Dijon" ],
    },
    {
        "country": "German",
        "visits": 5,
        "cities_visited": [ "Berlin", "Hamburg", "Stuttgart" ],
    }
]

def add_new_country(new_country, num_of_visits, cities_list):
    travel_log.append( {
        "country": new_country,
        "visits": num_of_visits,
        "cities_visited": cities_list
    })

add_new_country( "Russia", 2, [ "Moscow", "Saint Petersburg" ] )

print( travel_log )