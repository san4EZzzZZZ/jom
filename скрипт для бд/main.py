import xml.etree.ElementTree as ET
import mysql.connector

# Подключение к базе данных MySQL Необходимо указать свои данные!!!
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='gorod'
)

# Создание курсора для выполнения SQL-запросов
cursor = db_connection.cursor()

# Создание таблицы для хранения данных
cursor.execute('''
    CREATE TABLE IF NOT EXISTS points_of_interest (
        id INT AUTO_INCREMENT PRIMARY KEY,
        category VARCHAR(255),
        object_type VARCHAR(255),
        name VARCHAR(255),
        latitude DECIMAL(10, 6),
        longitude DECIMAL(10, 6)
    )
''')

# Функция для определения категории объекта
def get_category(object_type):
    educational_institutions = ["training", "university", "college", "technical_college", "vocational", "school", "kindergarten", "language_school", "music_school"]
    positive_points = ["swimming_pool", "stadium", "riding_sport", "fitness_centre", "sports_centre", "cycleway", "skating", "park", "pedestrian", "sports_pitch", "athletics", "marketplace", "farm_shop", "fresh_food"]
    negative_points = ["tobacco", "e-cigarette", "cigarettes", "bar", "beer_garden", "pub", "wine", "alcohol", "beverages", "fast_food", "food_court"]

    if object_type in educational_institutions:
        return "Образовательное учреждение"
    elif object_type in positive_points:
        return "Положительная точка"
    elif object_type in negative_points:
        return "Отрицательная точка"
    else:
        return "Неизвестная категория"

# Функция для поиска объектов и сохранения данных в базе данных

def search_objects(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for node in root.iter():
        if node.tag in ["way", "relation", "node"]:
            object_type = None
            for tag in node.iter("tag"):
                if (tag.attrib["k"] == "amenity" or tag.attrib["k"] == "building"):
                    object_type = tag.attrib["v"]
                    break

            if object_type:
                latitude = node.attrib.get("lat")
                longitude = node.attrib.get("lon")
                object_name = None

                for tag in node.iter("tag"):
                    if tag.attrib["k"] == "name":
                        object_name = tag.attrib["v"]
                        break

                if object_name:
                    category = get_category(object_type)
                    if category in ["Образовательное учреждение", "Положительная точка", "Отрицательная точка"]:
                        cursor.execute("INSERT INTO points_of_interest (category, object_type, name, latitude, longitude) VALUES (%s, %s, %s, %s, %s)",
                                       (category, object_type, object_name, latitude, longitude))
                        db_connection.commit()

# Путь к файлу .osm
file_path = "map.osm"

# Поиск и сохранение объектов
search_objects(file_path)

# Закрываем базу данных и курсор
cursor.close()
db_connection.close()
