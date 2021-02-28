planets = open('planets.txt').read().splitlines()
for planet in planets:
    print(planet, len(planet), len(planet)*2)
