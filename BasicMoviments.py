from djitellopy import tello
from time import sleep

# criando objeto tello
me = tello.Tello()
me.connect()
print(me.get_battery())