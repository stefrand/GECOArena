import random
import time
import os

#Room Values List!
arena = ["It is a circle with walls that go up at least 100 ft",
         "You almost slip and fall on the icy floor and you can see your breath",
         "The heat is intense and unbearable. \n You stare in shock at the moat of lava thatsurrounds you"]

#Creatures Tuple!

enemy = ("ninja","gladiator","zombie","giant cockroach")

#Adventurer Dictionary!
profile = {'Name':'Alexander The Mediocre','Weapon':'spork','HP':20}

#build a room with a function
def createarena():
    room = random.choice(arena)
    whatfighting = random.choice(enemy)
    print("Weapon: " + profile['Weapon'] + ", Health points: " + str(profile['HP']))
    print("You walk into the arena. " + room + ".")
    print()
    print("There is a " + whatfighting + " in the arena!")
    print()
    pass

#Start game code
print("Alexander the Mediocre goes battling!")
print()
#Enter the room
createarena()
#Exit the room
time.sleep(5)
