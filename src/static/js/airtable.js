// API key setup
require('dotenv').config();
const apiKey = process.env.API_KEY;
console.log(apiKey);

function filterAirtable(selectedOption) {
  const baseId = "YOUR_BASE_ID";
  const tableName = "YOUR_TABLE_NAME";

  const endpoint = `https://api.airtable.com/v0/${baseId}/${tableName}?api_key=${apiKey}`;

  fetch(endpoint)
    .then(response => response.json())
    .then(data => {
      const filteredData = data.records.filter(record => {
        // filter the data based on the selected dropdown option
        return record.fields["column-name"] === selectedOption;
      });
      
      // pass the filtered data to a function that will update the embedded table
      updateEmbeddedTable(filteredData);
    })
    .catch(error => {
      console.error(error);
    });
}

function updateEmbeddedTable(data) {
  const iframe = document.getElementById("airtable-embed");
  const message = {
    type: "update",
    records: data
  };
  
  // send a message to the embedded iframe with the filtered data
  iframe.contentWindow.postMessage(message, "https://airtable.com");
}

//Toggle dropdown event listener to update airtables
var dropdown = document.getElementById("location-dropdown");

dropdown.addEventListener("change", function() {
  var selectedValue = this.value;

  // Loop over each Airtable table and update its URL to include the selected filter value
  var tables = document.getElementsByClassName("airtable-embed");
  for (var i = 0; i < tables.length; i++) {
    var src = tables[i].getAttribute("src");
    var newSrc = src + "&filter_Field=" + selectedValue;
    tables[i].setAttribute("src", newSrc);
  }
});

