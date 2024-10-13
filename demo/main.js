import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

let map;

// Function to initialize the map
function initMap() {
    // Create a map centered on Finland
    map = L.map('map').setView([65.5, 26], 4.5);

    // Add a base tile layer (you can choose a different one if you prefer)
    // L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    //     attribution: '© OpenStreetMap contributors'
    // }).addTo(map);

    // Load GeoJSON data
    // fetch('/data/daycare_data.geojson')
    fetch(new URL('/data/daycare_data.geojson', import.meta.url).href)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Log the JSON data
            console.log('GeoJSON data:', JSON.stringify(data, null, 2));

            // Add choropleth layer
            L.geoJSON(data, {
                style: style,
                onEachFeature: onEachFeature
            }).addTo(map);

            // Add legend
            addLegend(map);
        });
}

// Function to style the choropleth
function style(feature) {
    return {
        fillColor: getColor(feature.properties.foreign_language_share),
        weight: 1,
        opacity: 1,
        color: 'black',
        fillOpacity: 0.7
    };
}

// Function to get color based on foreign language share
function getColor(d) {
    return d >= 30 ? '#800026' :
           d >= 25 ? '#BD0026' :
           d >= 20 ? '#E31A1C' :
           d >= 15 ? '#FC4E2A' :
           d >= 10 ? '#FD8D3C' :
           d >= 5  ? '#FEB24C' :
           d >= 0  ? '#FED976' :
                     '#FFEDA0';
}

// Function to handle each feature (municipality)
function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
    });

    // Add tooltip
    layer.bindTooltip(feature.properties.area, {
        permanent: false,
        direction: 'center',
        className: 'leaflet-tooltip'
    });

    // Add popup
    const popupContent = `
        <strong>Kunta:</strong> ${feature.properties.area}<br>
        <strong>Väkiluku:</strong> ${feature.properties.population}<br>
        <strong>Lapsia varhaiskasvatuksessa:</strong> ${feature.properties.children}<br>
        <strong>Vieraskielisiä lapsia varhaiskasvatuksessa:</strong> ${feature.properties.foreign_language_children}<br>
        <strong>Vieraskielisten lasten osuus (prosenttia):</strong> ${feature.properties.foreign_language_share}
    `;
    layer.bindPopup(popupContent);
}

// Function to highlight feature on mouseover
function highlightFeature(e) {
    const layer = e.target;
    layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.7
    });
    layer.bringToFront();
}

// Function to reset highlight on mouseout
function resetHighlight(e) {
    const layer = e.target;
    layer.setStyle(style(layer.feature));
}

// Function to add legend
function addLegend(map) {
    const legend = L.control({position: 'bottomright'});

    legend.onAdd = function (map) {
        const div = L.DomUtil.create('div', 'info legend');
        const grades = [0, 5, 10, 15, 20, 25, 30];
        const labels = [];

        div.innerHTML = '<h4>Vieraskielisten lasten osuus (prosenttia)</h4>';

        for (let i = 0; i < grades.length; i++) {
            div.innerHTML +=
                '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
                grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
        }

        return div;
    };

    legend.addTo(map);
}

// Initialize the map when the DOM is ready
document.addEventListener('DOMContentLoaded', initMap);
