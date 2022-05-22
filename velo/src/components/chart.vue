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
    <!-- <apexchart
      type="area"
      height="350"
      :options="energyOptions"
      :series="energySeries"
      ref="Energy"
    ></apexchart> -->
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
          name: "Voltage",
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
          // labels: {
          //   formatter: function(value, timestamp, opts) {
          //     return opts.dateFormatter(new Date(value)).format("dd MMM");
          //   },
          // },
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
        "https://8fbddwr1ga.execute-api.us-east-1.amazonaws.com/fetchPower?BicycleID=2"
      );

      if (
        res.data[0].length <= 1 ||
        res.data[0].length == this.wattageSeries[0].data.length
      )
        return;

      this.wattageSeries[0].data = [];
      this.energySeries[0].data = [];

      const time = res.data[0][0][0];

      for (let i in res.data[0]) {
        res.data[0][i][0] = res.data[0][i][0] - time;
        this.wattageSeries[0].data.push(res.data[0][i]);
      }
      for (let i in res.data[1]) {
        res.data[1][i][0] = res.data[1][i][0] - time;
        this.energySeries[0].data.push(res.data[1][i]);
      }
      this.updateSeriesLine();
      // this.$refs.Energy.refresh();
    },
    updateSeriesLine() {
      this.$refs.Wattage.updateSeries(
        [
          {
            data: this.wattageSeries[0].data,
          },
        ],
        true,
        false
      );
    },
  },
  async created() {
    await this.fetchData();
  },
  async mounted() {
    window.setInterval(() => {
      this.fetchData();
    }, 5000);
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
</style>
