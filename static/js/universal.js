var map = L.map('map', {
  doubleClickZoom: true,
  dragging: true,
  scrollWheelZoom: true,
}).fitWorld()
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
