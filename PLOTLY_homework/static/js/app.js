function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel


  // Fetch and display metadata
  var meta_url = "/metadata/" + String(sample);
  d3.json(meta_url).then(meta_data => {
    metadata_panel = d3.select("#sample-metadata");
    metadata_panel.html("");

    for (let [key, value] of Object.entries(meta_data)) {
      var key_string = key.toUpperCase();
      metadata_panel.append("p").append("small").append("strong")
        .text(`${key_string}: ${value}`);
    };

  });

  // BONUS: Build the Gauge Chart
  buildGauge();
}

function buildGauge() {
  var data = [{
    domain: {
      x: [0, 1],
      y: [0, 1]
    },
    value: 450,
    title: { text: "Belly Button Washing Frequency" },
    type: "indicator", mode: "gauge+number+delta", delta: { reference: 380 }, gauge:
    {
      axis: { range: [null, 500] }, steps: [{ range: [0, 250], color: "lightgray" },
      { range: [250, 400], color: "gray" }], threshold: {
        line: { color: "red", width: 4 },
        thickness: 0.75, value: 490
      }
    }
  }];

  var layout = { width: 600, height: 500, margin: { t: 0, b: 0 } };
  Plotly.newPlot("gauge", data, layout);
}

function buildCharts(sample) {

  var samples_url = "/samples/" + String(sample);
  d3.json(samples_url).then(sample_data => {

    // Pie chart of top 10 samples
    var trace_pie = {
      values: sample_data['sample_values'].slice(0, 10),
      labels: sample_data['otu_ids'].slice(0, 10),
      names: sample_data['otu_labels'].slice(0, 10),
      hoverinfo: 'names',
      type: 'pie'
    };

    // Bubble chart for samples
    var trace_bubble = {
      x: sample_data['otu_ids'],
      y: sample_data['sample_values'],
      mode: 'markers',
      marker: {
        size: sample_data['sample_values'],
        color: sample_data['otu_ids'],
        text: sample_data['otu_lables']
      },
      text: sample_data['otu_labels']
    };

    var data_pie = [trace_pie];
    var data_bubble = [trace_bubble];

    var layout_bubble = {
      height: 600,
      width: 1500,
      xaxis: { title: { text: 'OTU ID' } }
    };

    Plotly.newPlot('pie', data_pie);
    Plotly.newPlot('bubble', data_bubble, layout_bubble);
  });
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
