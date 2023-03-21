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

// Add the heatmap layer to the container element
heatmapLayer.addTo(document.getElementById('heatmap-container'));
