travel_log = [
 {"Country" : "France",
 "cities_visited" : ["Paris", "Lille", "Dijon"], 
 "Total_visited" : 12},
 {"Country" : "Germany",
 "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], 
 "Total_visited" : 5}
]

def add_new_country(Country, total_visited, cities_visited):
    new_country = {}
    new_country["Country"] = Country
    new_country["cities_visited"] = cities_visited
    new_country["Total_visited"] = total_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersberg"])
print(travel_log)