window.onload = function () {
  alert("Hello");

    var myData = [];
    var colors = ['#ff4c4c', '#168c8c', '#ff9d4c', '#5cdd5c', '#c45cdd']

    for(var i = 0; i < 5; i++){
      var myPoints =  [];

      var arrive = {{customers[i]}}, state = {{customers[i]}}

      for(int j = arrive; j =< state; j++){
        myPoints.push({x: j, y: 1});
      }

      var obj = {
              type: "stackedColumn",
              showInLegend: true,
              color: colors[i],
              name: "Client" + (i + 1),
              dataPoints: myPoints
          }
      myData.push(obj);
    }
    var chart = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,
        title: {
            text: "Queueing System Simulation Graph",
            fontFamily: "tahoma",
            fontColor: "#3d3d3d"
        },
        axisX: {
            interval: 1,
            intervalType: "Tic"
        },
        axisY: {
            valueFormatString: "#0 In The Queue",
            gridColor: "#ccc",
            tickColor: "#ccc"
        },
        toolTip: {
            shared: false,
            content: toolTipContent
        },
        data: myData
});
    chart.render();

    function toolTipContent(e) {
        var str = "";
        var total = 0;
        var str2, str3;
        for (var i = 0; i < e.entries.length; i++) {
            var str1 = "<span style= \"color:" + e.entries[i].dataSeries.color + "\"> " + e.entries[i].dataSeries.name + "</span>: $<strong>" + e.entries[i].dataPoint.y + "</strong>bn<br/>";
            total = e.entries[i].dataPoint.y + total;
            str = str.concat(str1);
        }
        str2 = "<span style = \"color:DodgerBlue;\"><strong>" + (e.entries[0].dataPoint.x).getFullYear() + "</strong></span><br/>";
        total = Math.round(total * 100) / 100;
        str3 = "<span style = \"color:Tomato\">Total:</span><strong> $" + total + "</strong>bn<br/>";
        return (str2.concat(str)).concat(str3);
    }
}
