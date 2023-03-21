// Initialize the map
var map = L.map('map').setView([58.2017, -134.0142], 13);

// Set the map provider and attribution
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Function to create a marker with a popup
function createMarker(lat, lng, name) {
  var marker = L.marker([lat, lng]).addTo(map);
  marker.bindPopup(`<b>${name}</b><br>Click for more info.`);
}

function fetchBusinesses(south, west, north, east) {
  // Set the map view based on the dropdown selection
  map.setView([(north + south) / 2, (east + west) / 2], 13);

  // Overpass API URL
  var overpassUrl = `https://overpass-api.de/api/interpreter?data=[out:json];(node["amenity"="restaurant"](${south},${west},${north},${east}););out;`;

  // Fetch data from the Overpass API
  fetch(overpassUrl)
    .then((response) => response.json())
    .then((data) => {
      data.elements.forEach((element) => {
        if (element.lat && element.lon) {
          // Create a marker for each business
          createMarker(element.lat, element.lon, element.tags.name || 'Unknown');
        }
      });
    })
    .catch((error) => {
      console.error("Error fetching data from Overpass API:", error);
    });
}

// Function to fetch census data
function fetchCensusData() {
  fetch('/census_data')
    .then((response) => response.json())
    .then((data) => {
      // Update the pane or container with the new data
    })
    .catch((error) => {
      console.error("Error fetching Census data:", error);
    });
}

// Function to Adjust the map based on location of dropdown
function handleLocationSelect() {
  var dropdown = document.getElementById('location-dropdown');
  dropdown.addEventListener('change', function() {
    var location = dropdown.value.split(',');
    fetchBusinesses(location);
  });
  var selectedValue = dropdown.value;
  
  // Look up the corresponding bounding box coordinates
  var coordinates = getCoordinatesForLocation(selectedValue);
  
  // Call fetchBusinesses with the coordinates
  fetchBusinesses(coordinates);
}

// Event Listener to check when the user changes the dropdown selection
// and then change the coordinates for fetchbusinesses
document.getElementById("location-dropdown").addEventListener("change", function() {
  var location = this.value;
  var south, west, north, east;

  // Set the bounding box coordinates based on the selected location
  if (location === "port-angeles-wa") {
    south = 48.1000;
    west = -123.5000;
    north = 48.1300;
    east = -123.4100;
  } else if (location === "juneau-ak") {
    south = 58.2017;
    west = -134.4209;
    north = 58.5208;
    east = -134.0142;
  } else if (location === "port-townsend-wa") {
    south = 48.0967;
    west = -122.8531;
    north = 48.1539;
    east = -122.6944;
  }

  // Call the fetchBusinesses() function with the selected coordinates
  fetchBusinesses(south, west, north, east);
});