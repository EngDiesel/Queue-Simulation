window.onload = function () {
    "use strict";

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
        data: [{
                type: "stackedColumn",
                showInLegend: true,
                color: "#FF4C4C",
                name: "Client 1",
                dataPoints: [
                  {
                        y: 1,
                        x: 1
                            },
                    {
                        y: 0,
                        x: 2
                            },
                    {
                        y: 1,
                        x: 3
                            },
                    {
                        y: 0,
                        x: 4
                            },
                    {
                        y: 1,
                        x: 5
                            },
                    {
                        y: 0,
                        x: 6
                            },
                    {
                        y: 1,
                        x: 7
                            }
                        ]
                    },
            {
                type: "stackedColumn",
                showInLegend: true,
                name: "Client 2",
                color: "#5CDD5C",
                dataPoints: [{
                        y: 0,
                        x: 1
                            },
                    {
                        y: 1,
                        x: 2
                            },
                    {
                        y: 0,
                        x: 3
                            },
                    {
                        y: 1,
                        x: 4
                            },
                    {
                        y: 0,
                        x: 5
                            },
                    {
                        y: 1,
                        x: 6
                            },
                    {
                        y: 0,
                        x: 7
                            }
                        ]
                    },
            {
                type: "stackedColumn",
                showInLegend: true,
                name: "Client 3",
                color: "#FF9D4C",
                dataPoints: [{
                        y: 0,
                        x: 1
                            },
                    {
                        y: 1,
                        x: 2
                            },
                    {
                        y: 1,
                        x: 3
                            },
                    {
                        y: 0,
                        x: 4
                            },
                    {
                        y: 1,
                        x: 5
                            },
                    {
                        y: 0,
                        x: 6
                            },
                    {
                        y: 1,
                        x: 7
                            }
                        ]
                    },
            {
                type: "stackedColumn",
                showInLegend: true,
                name: "Client 4",
                color: "#168C8C",
                dataPoints: [{
                        y: 0,
                        x: 1
                            },
                    {
                        y: 1,
                        x: 2
                            },
                    {
                        y: 0,
                        x: 3
                            },
                    {
                        y: 1,
                        x: 4
                            },
                    {
                        y: 1,
                        x: 5
                            },
                    {
                        y: 0,
                        x: 6
                            },
                    {
                        y: 0,
                        x: 7
                            }
                        ]
                    }
                ]
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
