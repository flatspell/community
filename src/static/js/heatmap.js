(function() {
  // Define the bounding box coordinates
  var south = 48.1000;
  var west = -123.5000;
  var north = 48.1300;
  var east = -123.4100;
  var bounds = [[south, west], [north, east]];

  // Generate the heatmap data
  var heatmapData = [
    {lat: 48.1184, lng: -123.4307, value: 0.8},
    {lat: 48.1190, lng: -123.4305, value: 0.5},
    {lat: 48.1195, lng: -123.4310, value: 0.2},
    // more data points...
  ];

  // Generate the heatmap layer
  var heatmapLayer = L.heatLayer(heatmapData, {
    radius: 20,
    blur: 15,
    maxZoom: 18,
    gradient: {
      0.4: 'blue',
      0.6: 'cyan',
      0.7: 'lime',
      0.8: 'yellow',
      1.0: 'red'
    }
  });

  // Add OpenStreetMap tiles as the tile layer
  var osmUrl='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
  var osmAttrib='Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors';
  var osm = new L.TileLayer(osmUrl, {attribution: osmAttrib}).addTo(map);

  // Create the map and center it on the bounding box
  var map = L.map('heatmap-container').fitBounds(bounds);

  // Add the heatmap layer to the map
  if (map && heatmapLayer) {
    heatmapLayer.addTo(map);
  }
})();
