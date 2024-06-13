const express = require('express');
const bodyParser = require('body-parser');
const math = require('mathjs');
const Chart = require('chart.js');

const app = express();
app.use(bodyParser.json());

// Assuming the API sends data in the following format:
// [
//   {
//     "date_of_purchase": "2022-01-01",
//     "age_of_house": 10,
//     "city": "New York",
//     "county": "New York",
//     "state": "NY",
//     "address": "123 Main St",
//     "listing_price": 500000,
//     "sold_price": 450000,
//     "lifetime_equity_rise": 100000
//   },
//   ...
// ]

app.post('/analyze', (req, res) => {
  const data = req.body;

  // Calculate mean of listing prices
  const meanListingPrice = math.mean(data.map(item => item.listing_price));

  // Calculate regression fit for sold prices vs. listing prices
  const x = data.map(item => item.listing_price);
  const y = data.map(item => item.sold_price);
  const regression = math.regression.linear(x, y);
  const slope = regression.slope;
  const intercept = regression.intercept;

  // Calculate z-scores for lifetime equity rise
  const meanLifetimeEquityRise = math.mean(data.map(item => item.lifetime_equity_rise));
  const stdDevLifetimeEquityRise = math.std(data.map(item => item.lifetime_equity_rise));
  const zScores = data.map(item => (item.lifetime_equity_rise - meanLifetimeEquityRise) / stdDevLifetimeEquityRise);

  // Create a chart to display the trends
  const ctx = document.getElementById('chart').getContext('2d');
  const chart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: data.map(item => item.date_of_purchase),
      datasets: [
        {
          label: 'Listing Price',
          data: data.map(item => item.listing_price),
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1
        },
        {
          label: 'Sold Price',
          data: data.map(item => item.sold_price),
          backgroundColor: 'rgba(54, 162, 235, 0.2)',
          borderColor: 'rgba(54, 162, 235, 1)',
          borderWidth: 1
        },
        {
          label: 'Lifetime Equity Rise',
          data: zScores,
          backgroundColor: 'rgba(255, 206, 86, 0.2)',
          borderColor: 'rgba(255, 206, 86, 1)',
          borderWidth: 1
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Housing Market Trends'
      },
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true
            }
          }
        ]
      }
    }
  });

  res.send(`
    <html>
      <head>
        <title>Housing Market Trends</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
      </head>
      <body>
        <canvas id="chart" width="400" height="200"></canvas>
      </body>
    </html>
  `);
});

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});