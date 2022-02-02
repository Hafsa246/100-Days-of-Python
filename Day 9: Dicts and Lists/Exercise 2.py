# Nesting Lists and Dicts
# {Key : [List], Key2 : {Dict}}

capitals = {"France" : "Paris", "Germany" : "Berlin"}

#Nesting a list in a Dictionary
travel_log = {"France": ["Paris", "Lille", "Dijon"]}

["A", "B", ["c", "D"]]

#Nest a dict in a dict
travel_log = {"France": {"cities_visite" : ["Paris", "Lille", "Dijon"]}, "Total_visited" : 12}


#Nesting a dict inside a list
travel_log = [
 {"Country" : "France",
 "cities_visited" : ["Paris", "Lille", "Dijon"], 
 "Total_visited" : 12},
 {"Country" : "Germany",
 "cities_visited" : ["Berlin", "Lille", "Dijon"], 
 "Total_visited" : 5}
]