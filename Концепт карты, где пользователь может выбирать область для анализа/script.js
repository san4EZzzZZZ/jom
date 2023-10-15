// Инициализация карты
var map = L.map('map').setView([51.505, -0.09], 13); // Установите начальные координаты и масштаб

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Объявите переменные для хранения координат углов области и прямоугольника
var topLeftCoords, bottomRightCoords, rectangle;

// Обработчик события клика на карте
map.on('click', function(e) {
    if (rectangle) {
        map.removeLayer(rectangle);
    }

    if (!topLeftCoords) {
        topLeftCoords = e.latlng;
    } else if (!bottomRightCoords) {
        bottomRightCoords = e.latlng;

        var lat1 = topLeftCoords.lat.toFixed(6);
        var lng1 = topLeftCoords.lng.toFixed(6);
        var lat2 = bottomRightCoords.lat.toFixed(6);
        var lng2 = bottomRightCoords.lng.toFixed(6);

        document.getElementById('coordinates').value = `Левый верхний угол: (${lat1}, ${lng1})\nПравый нижний угол: (${lat2}, ${lng1})\nЛевый верхний угол: (${lat1}, ${lng2})\nПравый верхний угол: (${lat2}, ${lng2})`;

        rectangle = L.rectangle([topLeftCoords, bottomRightCoords], { color: 'red', weight: 2 }).addTo(map);
        topLeftCoords = null;
        bottomRightCoords = null;
    }
});

// Установите начальные координаты
map.setView([51.505, -0.09], 13);
