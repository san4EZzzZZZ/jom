import math

def haversine_distance(lat1, lon1, lat2, lon2):
    # Радиус Земли в километрах
    earth_radius = 6371

    # Преобразование широт и долгот из градусов в радианы
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Разница между широтами и долготами
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Формула Гаверсинуса
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Расстояние между точками в километрах
    distance = earth_radius * c

    return distance

# Пример использования функции
lat1 = 47.226938  # Широта первой точки
lon1 = 39.704887  # Долгота первой точки
lat2 = 47.230707  # Широта второй точки
lon2 = 39.702570  # Долгота второй точки

distance = haversine_distance(lat1, lon1, lat2, lon2)
print(f'Расстояние между точками: {distance} км')