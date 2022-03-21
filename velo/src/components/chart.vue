<template>
  <div id="chart">
    <apexchart
      type="area"
      height="350"
      :options="wattageOptions"
      :series="wattageSeries"
      ref="Wattage"
    ></apexchart>
    <hr class="divider" />
    <apexchart
      type="area"
      height="350"
      :options="energyOptions"
      :series="energySeries"
      ref="Energy"
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
      latest: [],
      wattageSeries: [
        {
          name: "Power",
          data: [],
        },
      ],
      energySeries: [{ name: "Energy", data: [] }],
      wattageOptions: {
        chart: {
          height: 350,
          type: "area",
          foreColor: "#ffffff",
        },
        dataLabels: {
          enabled: false,
        },
        fill: {
          colors: ["#1A73E8"],
        },

        stroke: {
          curve: "smooth",
        },
        xaxis: {
          type: "numeric",
        },
      },
      energyOptions: {
        chart: {
          height: 350,
          type: "area",
          foreColor: "#ffffff",
        },
        dataLabels: {
          enabled: false,
        },
        fill: {
          colors: ["#51e031"],
        },

        stroke: {
          curve: "smooth",
          colors: ["#51e031"],
        },
        xaxis: {
          type: "numeric",
        },
      },
    };
  },
  methods: {
    async fetchData() {
      const res = await axios.get(
        "https://8s6uuofzza.execute-api.us-east-1.amazonaws.com/getLatestPower?BicycleID=1"
      );

      const time = res.data[0][0][0];
      for (let i in res.data[0]) {
        res.data[0][i][0] = res.data[0][i][0] - time;
        this.wattageSeries[0].data.push(res.data[0][i]);
      }
      for (let i in res.data[1]) {
        res.data[1][i][0] = res.data[1][i][0] - time;
        this.energySeries[0].data.push(res.data[1][i]);
      }
      this.$refs.Wattage.refresh();
      this.$refs.Energy.refresh();
    },
  },
  async created() {
    await this.fetchData();
  },
};
</script>

<style>
.apexcharts-text apexcharts-yaxis-label {
  fill: red !important;
}
.divider {
  margin-bottom: 2rem;
  margin-top: 2rem;
}
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background-color: #24252a;
  border-radius: 100px;
}

::-webkit-scrollbar-thumb {
  border-radius: 100px;
  border: 6px solid rgba(0, 0, 0, 0.18);
  border-left: 0;
  border-right: 0;
  background-color: #67d163;
}
</style>
