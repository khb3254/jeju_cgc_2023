// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Carrot_jeju 차트 표
var ctx = document.getElementById("CarrotJejuChart");
var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ["Mar 1", "Mar 2", "Mar 3", "Mar 13"],
    datasets: [{
      label: "양배추",
      lineTension: 0.3,
      backgroundColor: "#FAAC58",
      borderColor: "#04B404",
      pointRadius: 5,
      pointBackgroundColor: "#04B404",
      pointBorderColor: "#04B404",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "#04B404",
      pointHitRadius: 50,
      pointBorderWidth: 2,
      data: [100, 8787, 8263, 18394, 18287, 28682, 3],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 40000,
          maxTicksLimit: 5
        },
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }],
    },
    legend: {
      display: false
    }
  }
});