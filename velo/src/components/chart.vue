<template>
  <div id="chart">
    <apexchart
      type="area"
      height="350"
      :options="chartOptions"
      :series="series"
      ref="myChart"
    ></apexchart>
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";
import axios from "axios";

export default {
  components: {
    apexchart: VueApexCharts,
  },
  data() {
    return {
      series: [
        {
          name: "Wattage",
          data: [],
        },
      ],
      chartOptions: {
        chart: {
          height: 350,
          type: "area",
        },
        dataLabels: {
          enabled: false,
        },
        stroke: {
          curve: "smooth",
        },
        xaxis: {
          type: "numeric",
          categories: [1, 2, 3, 4, 5, 6],
        },
      },
    };
  },
  methods: {
    async fetchData() {
      const res = await axios.get(
        "https://pbh9b34d7e.execute-api.us-east-1.amazonaws.com/Prod/veloapi?BicycleID=3"
      );
      let temp = [];
      for (let i in Object.keys(res.data)) {
        temp.push([
          parseInt(Object.keys(res.data)[i], 10),
          parseInt(res.data[Object.keys(res.data)[i]], 10),
        ]);
      }
      temp.sort(function(a, b) {
        return a[0] - b[0];
      });

      for (let i in temp) {
        this.chartOptions.xaxis.categories[i] = Math.round(
          (temp[i][0] - temp[0][0]) / 1000
        );
        this.series[0].data[i] = parseInt(temp[i][1], 10);
      }
      this.$refs.myChart.refresh();
    },
  },
  async created() {
    await this.fetchData();
  },
};
</script>

<style>
/* .apexcharts-toolbar {
  display: none !important; 
} */
</style>
