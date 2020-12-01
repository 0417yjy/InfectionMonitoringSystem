function HistogramData(weekDate, diseased7, death7, cured7) {
    this.labels = weekDate;
    this.datasets = [
        {
            label: "확진",
            backgroundColor: "red",
            data: diseased7,
            datalabels: {
                align: 'end',
                anchor: 'end',
                color: 'red'
            }
        },
        {
            label: "사망",
            backgroundColor: "black",
            data: death7,
            datalabels: {
                align: 'end',
                anchor: 'end',
                color: 'black'
            }
        },
        {
            label: "완치",
            backgroundColor: "green",
            data: cured7,
            datalabels: {
                align: 'end',
                anchor: 'end',
                color: 'green'
            }
        }
    ];
}

function MakeHorizonData(period, type, src_data) {
    var result = [];

    if (period == "opt-all") {
        switch (type) {
            case "infected":
                for (var i = 1; i < src_data.length; i++) {
                    result.push(src_data[i].fields.no_infected);
                }
                break;
            case "deceased":
                for (var i = 1; i < src_data.length; i++) {
                    result.push(src_data[i].fields.no_deceased);
                }
                break;

            case "cured":
                for (var i = 1; i < src_data.length; i++) {
                    result.push(src_data[i].fields.no_offisolated);
                }
                break;
        }
    } else {
        switch (type) {
            case "infected":
                for (var i = 1; i < src_data.length; i++) {
                    result.push(src_data[i].fields.no_infected - src_data[i].fields.prev_no_infected);
                }
                break;
            case "deceased":
                for (var i = 1; i < src_data.length; i++) {
                    result.push(src_data[i].fields.no_deceased - src_data[i].fields.prev_no_deceased);
                }
                break;

            case "cured":
                for (var i = 1; i < src_data.length; i++) {
                    result.push(src_data[i].fields.no_offisolated - src_data[i].fields.prev_no_offisolated);
                }
                break;
        }
    }

    return result;
}

function HorizonBarData(arg_labels, arg_data, arg_type, arg_color) {
    // 현재는 예시. 나중에 함수로 적용
    this.labels = arg_labels;
    this.datasets = [
        {
            label: arg_type,
            backgroundColor: arg_color,
            data: arg_data,
            datalabels: {
                align: 'end',
                anchor: 'end',
                color: arg_color
            }
        }
    ];
}

