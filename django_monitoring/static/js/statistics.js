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

function HorizonBarData() {
    // 현재는 예시. 나중에 함수로 적용
    this.labels = ["서울", "경기", "부산", "검역", "대전", "인천", "충남", "강원", "전북", "대구", "전남", "충북", "광주", "경북", "울산", "경남", "제주", "세종",];
    this.datasets = [
        {
            label: "확진",
            backgroundColor: "red",
            data: [169, 163, 73, 53, 36, 31, 9, 8, 4, 4, 3, 3, 3, 3, 2, 2, 0, 0],
            datalabels: {
                align: 'end',
                anchor: 'end',
                color: 'red'
            }
        }
    ];
}

