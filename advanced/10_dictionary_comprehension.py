# Dictionary comprehension = Create dictionaries using an expression
# Can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: expression for (key, value) in iterable if conditional}
# dictionary = {key: (if/else) for (key, value) in iterable}
# dictionary = {key: function(value) for (key, value) in iterable}

# ---
# Expression
cities_in_fahrenheit = {'New York': 32,
                        'Boston': 75,
                        'Los Angeles': 100,
                        'Huston': 102,
                        'Chicago': 50}

cities_in_celsius = {key: round((value - 32) * 5/9) for (key, value) in cities_in_fahrenheit.items()}

print(cities_in_celsius)

# ---
# Expression + if
weather = {'New York': 'snowing',
           'Boston': "sunny",
           'Los Angeles': "sunny",
           'Huston': "sunny",
           'Chicago': "cloudy"}

sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}

print(sunny_weather)

# ---
# Expression + if/else
cities = {'New York': 32,
          'Boston': 75,
          'Los Angeles': 100,
          'Huston': 102,
          'Chicago': 50}

desc_cities = {key: ("WARM" if value >= 50 else "COLD") for (key, value) in cities.items()}

print(desc_cities)


# ---
# Function
def check_temp(value):
    if value >= 75:
        return "HOT"
    elif 70 > value >= 50:
        return "WARM"
    else:
        return "COLD"


desc_cities_func = {key: check_temp(value) for (key, value) in cities.items()}
print(desc_cities_func)



