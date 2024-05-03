from vpython import *
import random
from math import *

class Satellite:
    def __init__(self, radius, color, distance, speed, inclination):
        self.radius = 0.1
        self.color = color
        self.distance = distance
        self.speed = speed
        self.inclination = inclination
        self.angle = random.uniform(0, 2 * pi)  # Случайный угол для начальной позиции спутника
        self.obj = sphere(radius=self.radius, color=self.color)

    def update_position(self):
        self.angle += self.speed
        x = self.distance * cos(self.angle)
        y = self.distance * sin(self.angle)
        z = self.distance * sin(self.inclination)  # Изменение высоты орбиты по инклинации
        self.obj.pos = vector(x, y, z)



# Создание сцены
scene = canvas(title='Rotating Earth with Satellites', width=1080, height=720, background=color.black)

# Создание планеты
#earth = Planet(radius=50, color=color.blue)
earth = sphere(pos=vector(0, 0, 0), radius=0.6371, texture=textures.earth)
rotation_speed = 0.02

# Создание кнопки для добавления спутников
button = button(text='Add Satellite', bind=lambda: add_satellite())

distance_text = label(text='', pos=vector(0, 250, 0), height=20, color=color.white)

# Список спутников
satellites = []

# Функция добавления спутника
def add_satellite():
    distance = random.uniform(1, 3)   # Расстояние спутника от центра Земли
    speed = random.uniform(0.01, 0.1)  # Скорость вращения спутника
    inclination = random.uniform(0, pi / 2)  # Угол наклона орбиты
    satellite = Satellite(radius=5, color=color.red, distance=distance, speed=speed, inclination=inclination)
    satellites.append(satellite)
    update_distance()
def update_distance():
    if len(satellites) >= 2:
        dist = sqrt((satellites[-1].obj.pos.x - satellites[-2].obj.pos.x) ** 2 + (satellites[-1].obj.pos.y - satellites[-2].obj.pos.y) ** 2 + satellites[-1].obj.pos.z - satellites[-2].obj.pos.z) ** 2
        distance_text.text = 'Distance between satellites: {:.2f}'.format(dist)
        # Основной цикл программы
        while True:
            rate(60)  # Ограничение частоты кадров    # Вращение Земли
            #earth.rotate(0.01)
            earth.rotate(angle=rotation_speed, axis=vector(0, 1, 0))

    # Обновление позиции спутников    
for satellite in satellites:
        satellite.update_position()

        satellite.up
