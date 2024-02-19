// Import the necessary libraries
const L = require('leaflet');

// Create a Leaflet map
const map = L.map('map').setView([51.505, -0.09], 13);

// Add a tile layer to the map (OpenStreetMap tiles)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

// Add a marker to the map
L.marker([51.505, -0.09]).addTo(map)
    .bindPopup('A sample marker.');

// You can add more Leaflet functionality or customize the map as needed.

// Optional: If you want to use this script with a web server, you may need to start the server.
// For example, if using Express:
// const express = require('express');
// const app = express();
// app.use(express.static('public')); // Assuming 'index.js' is in a 'public' folder
// app.listen(3000, () => console.log('Server running on http://localhost:3000/'));
