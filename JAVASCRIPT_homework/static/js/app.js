// from data.js
var UFOsightings = data;

var submit = d3.select('#filter-btn');
var tableBody = d3.select("tbody");

// Handle data upon form submission
submit.on("click", function () {
    d3.event.preventDefault();

    var inputs = d3.selectAll(".form-control");
    var inputData = inputs.data("value")._groups[0];
    var inputValues = inputData.map(inD => inD.value);
    var keys = ['datetime', 'city', 'state', 'country', 'shape'];

    // Chained filtering for multiple form inputs
    var filteredData = [];
    for (var j = 0; j < inputValues.length; j++) {
        if ((inputValues[j] !== "") && 
            (filteredData === undefined || filteredData.length == 0)) {

            filteredData = UFOsightings.filter(sighting => 
                sighting[keys[j]] === inputValues[j]);
        }
        else if (inputValues[j] !== "") {
            filteredData = filteredData.filter(sighting => 
                sighting[keys[j]] === inputValues[j]);
        }
    };

    // Append to table
    tableBody.html("");
    filteredData.forEach(sighting => {
        var row = tableBody.append("tr")

        Object.entries(sighting).forEach(([key, value]) => {
            row.append("td").text(value)
        });
    });
});