
var map = L.map('map').setView([0.845917, 37.913818], 13);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiYW5rb21hcGJveCIsImEiOiJja3pwZDd0OG8zZ3luMnZvMGw2djM4M3Q1In0.vryS8JhJZB9IcZXwa8BsRg'
}).addTo(map);