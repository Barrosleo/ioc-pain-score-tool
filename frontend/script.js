// Fetch processed IoC data from the backend API
fetch('http://localhost:5000/api/iocs')
  .then(response => response.json())
  .then(data => {
    // Extract IoC identifiers and their corresponding pain scores
    const labels = data.map(ioc => ioc.ioc);
    const painScores = data.map(ioc => ioc.pain_score);

    // Create a bar chart using Chart.js
    const ctx = document.getElementById('painChart').getContext('2d');
    const painChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Pain Score',
          data: painScores,
          backgroundColor: 'rgba(54, 162, 235, 0.6)',
          borderColor: 'rgba(54, 162, 235, 1)',
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            max: 7
          }
        }
      }
    });
  })
  .catch(error => console.error('Error fetching IoC data:', error));
