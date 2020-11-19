function HistogramData() {
    // 현재는 예시. 나중에 함수로 적용
    this.labels = ["10.7", "10.8", "10.9", "10.10", "10.11", "10.12", "10.13", "10.14", "10.15"];
    this.datasets = [
        {
            label: "확진",
            backgroundColor: "red",
            data: [134, 69, 54, 72, 58, 100, 91, 84, 110],
            datalabels: {
                align: 'end',
                anchor: 'end',
                color: 'red'
            }
        },
        {
            label: "사망",
            backgroundColor: "black",
            data: [3, 2, 1, 2, 2, 2, 1, 3, 4],
            datalabels: {
                align: 'end',
                anchor: 'end',
                color: 'black'
            }
        },
        {
            label: "격리해제",
            backgroundColor: "green",
            data: [251, 129, 106, 55, 69, 35, 134, 162, 52],
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
