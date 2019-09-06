function buildMetadata(sample) {

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

    buildGauge(meta_data['WFREQ']);

  });
}

// Build Gauge Chart
function buildGauge(wfreq) {
  var data = [{
    domain: {
      x: [0, 1],
      y: [0, 1]
    },
    value: wfreq,
    title: {
      text: "<b>Belly Button Washing Frequency<b><br>" +
        "<span style='font-size:0.8em;color:gray'>Scrubs Per Week</span>"
    },
    type: "indicator", mode: "gauge+number", gauge:
    {
      axis: { range: [0, 9] },
      steps: [
        { range: [0, 1], color: "#ffffff" },
        { range: [1, 2], color: "#f5f5dc" },
        { range: [2, 3], color: "#eeeec3" },
        { range: [3, 4], color: "#c6ecd7" },
        { range: [4, 5], color: "#9fdfbc" },
        { range: [5, 6], color: "#79d2a1" },
        { range: [6, 7], color: "#80b380" },
        { range: [7, 8], color: "#609f60" },
        { range: [8, 9], color: "#4d804d" }
      ],
      bar: {color: "darkred", thickness: 0.2}, 
    }
  }];

  Plotly.newPlot("gauge", data);
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
